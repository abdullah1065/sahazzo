from operator import imod
from queue import Empty
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignupDonatorForm, LoginDonatorForm
from home.models import PersonTable
from organizor.models import EventTable
from .models import  DonatorTable, DonateTable, FundTable


# Create your views here.
def SignupDonator(request):
    form = SignupDonatorForm()
    if request.method == 'POST':
        data = SignupDonatorForm(request.POST)
        if data.is_valid():
            p_id = "D"
            first_name = data.cleaned_data['FIRST_NAME']
            last_name = data.cleaned_data['LAST_NAME']
            email = data.cleaned_data['EMAIL']
            contact = data.cleaned_data['CONTACT']
            nid = data.cleaned_data['NID']
            password = data.cleaned_data['PASSWORD']
            duplicate_checker = list(PersonTable.objects.filter(PersonType = p_id, EMAIL = email, NID = nid))
            if duplicate_checker == []:
                person_table = PersonTable(PersonType = p_id, FIRST_NAME = first_name, LAST_NAME = last_name, EMAIL = email, CONTACT = contact, NID = nid, PASSWORD = password)
                donator_table = DonatorTable(D_ID = p_id, EMAIL = email)
                person_table.save()
                donator_table.save()
            else:
                return render (request, 'home/error.html')
        else:
            return render (request, 'home/error.html')
        messages.success(request, 'Success')       
        return HttpResponseRedirect ('/home')
    return render (request, 'donator/SignupDonator.html', {'form':form})


def LoginDonator(request):
    form = LoginDonatorForm()
    if request.method == 'POST':
        data = LoginDonatorForm(request.POST)
        if data.is_valid():
            p_id = "D"
            email = data.cleaned_data['EMAIL']
            password = data.cleaned_data['PASSWORD']
            checker = PersonTable.objects.filter(PersonType = p_id, EMAIL = email, PASSWORD = password)
            if list(checker) != []:
                request.session['EMAIL'] = email
                request.session['PASSWORD'] = password
                return render (request, 'donator/donator_profile.html', {'checker':checker})
            else:
                return render (request, 'home/error.html')
    return render (request, 'donator/LoginDonator.html', {'form':form})

def donator_profile(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
    checker = PersonTable.objects.filter(PersonType = "D", EMAIL = email, PASSWORD = password)
    return render (request, 'donator/donator_profile.html', {'checker':checker})

def event_details_d(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        all_events = EventTable.objects.all()
        all_events_fund = FundTable.objects.all()
        all_events_dict = {}
        for event in all_events:
            for fund in all_events_fund:
                if fund.FUND_STATUS == "Not Fulfilled" and 'E'+str(event.id) == str(fund.EVENT_ID):
                    all_events_dict[f'E{event.id}'] = [fund.EVENT_ID, event.EVENT_NAME, event.LOCATION, event.BUDGET, int(event.BUDGET)-int(fund.COLLECTED_AMOUNT)]
        if request.method == 'POST':
            data = request.POST
            for keys,values in data.items():
                if keys == 'id': id_e = values
                if keys == 'amount': amount = values
            selected_event = EventTable.objects.filter(id = int(id_e[1:]))
            selected_event_fund = FundTable.objects.filter(EVENT_ID = id_e)
            
            if int(amount) > int(selected_event[0].BUDGET) - int(selected_event_fund[0].COLLECTED_AMOUNT):
                return render(request,"home/error.html")
            else:
                total_amount = int(amount) + int(selected_event_fund[0].COLLECTED_AMOUNT)
                if total_amount == int(selected_event[0].BUDGET):
                    status = "Fulfilled"
                else:
                    status = "Not Fulfilled"
                selected_event_fund.update(COLLECTED_AMOUNT = total_amount, FUND_STATUS = status)
                d_id = PersonTable.objects.filter(PersonType = "D", EMAIL = email, PASSWORD = password)
                donate_table = DonateTable(D_ID = 'D'+str(d_id[0].id), EVENT_ID = id_e, PAYMENT_DETAILS = 'bKash', PAYMENT = amount)
                donate_table.save()
                messages.success(request, 'Success')
                checker = PersonTable.objects.filter(PersonType = "D", EMAIL = email, PASSWORD = password)
                return render (request, 'donator/donator_profile.html', {'checker':checker})

    return render (request, 'donator/event_details_d.html', {'a_dict': all_events_dict})

def donateHistory(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "D", EMAIL = email, PASSWORD = password)
        d_id = 'D'+ str(checker[0].id)
        data = DonateTable.objects.filter(D_ID = d_id)
        return render (request, 'donator/donateHistory.html', {'data':data})
    else:
        return render (request, 'home/error.html')
    
