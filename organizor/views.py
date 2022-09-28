from operator import imod
from queue import Empty
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignupOrganizorForm, LoginOrganizorForm
from home.models import PersonTable
from donator.models import FundTable
from .models import  OrganizorTable, EventTable, ShopTable

# Create your views here.

def SignupOrganizor(request):
    form = SignupOrganizorForm()
    if request.method == 'POST':
        data = SignupOrganizorForm(request.POST)
        if data.is_valid():
            p_id = "O"
            first_name = data.cleaned_data['FIRST_NAME']
            last_name = data.cleaned_data['LAST_NAME']
            email = data.cleaned_data['EMAIL']
            contact = data.cleaned_data['CONTACT']
            nid = data.cleaned_data['NID']
            password = data.cleaned_data['PASSWORD']
            duplicate_checker = list(PersonTable.objects.filter(PersonType = p_id, EMAIL = email, NID = nid))
            if duplicate_checker == []:
                person_table = PersonTable(PersonType = p_id, FIRST_NAME = first_name, LAST_NAME = last_name, EMAIL = email, CONTACT = contact, NID = nid, PASSWORD = password)
                organizor_table = OrganizorTable(O_ID= p_id, EMAIL = email)
                person_table.save()
                organizor_table.save()
            else:
                return render (request, 'home/error.html')
        else:
            return render (request, 'home/error.html')
        messages.success(request, 'Success')       
        return HttpResponseRedirect ('/home')
    return render (request, 'organizor/SignupOrganizor.html', {'form':form}) 


def LoginOrganizor(request):
    form = LoginOrganizorForm()
    if request.method == 'POST':
        data = LoginOrganizorForm(request.POST)
        if data.is_valid():
            p_id = "O"
            email = data.cleaned_data['EMAIL']
            password = data.cleaned_data['PASSWORD']
            checker = PersonTable.objects.filter(PersonType = p_id, EMAIL = email, PASSWORD = password)
            if list(checker) != []:
                request.session['EMAIL'] = email
                request.session['PASSWORD'] = password
                return render (request, 'organizor/organizor_profile.html', {'checker':checker})
            else:
                return render (request, 'home/error.html')
    return render (request, 'organizor/LoginOrganizor.html', {'form':form})
    
def organizor_profile(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
    checker = PersonTable.objects.filter(PersonType = "O", EMAIL = email, PASSWORD = password)
    return render (request, 'organizor/organizor_profile.html', {'checker':checker})

def create_event(request):
    if request.method == 'POST':
        data = request.POST
        if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
            email = request.session['EMAIL']
            password = request.session['PASSWORD']
            for keys,values in data.items():
                if keys == 'Event_Name': Event_Name = values
                if keys == 'Start_Time': Start_Time = values
                if keys == 'End_Time': End_Time = values
                if keys == 'Location': Location = values
                if keys == 'Budget': Budget = values
                if keys == 'Shop': Shop = values
                if keys == 'Items': Items = values
                if keys == 'Quantity': Quantity = values
                if keys == 'Event_For': Event_For = values
            checker = EventTable.objects.filter(EVENT_NAME = Event_Name, LOCATION = Location, ITEMS = Items, EVENT_FOR = Event_For)
            if list(checker) == []:
                event_table = EventTable(EVENT_NAME = Event_Name, START_TIME = Start_Time, END_TIME = End_Time, LOCATION = Location, BUDGET = Budget, SHOP = Shop, ITEMS = Items, QUANTITY = Quantity, EVENT_FOR   = Event_For, CREATED_BY = email)
                shop_table = ShopTable(SHOP_NAME = Shop, PAY_DEMAND = Budget, DELIVERY_STATUS = 'Pending')
                event_table.save()
                shop_table.save()
                data = EventTable.objects.filter(CREATED_BY = email)
                for d in data:
                    fund_table = FundTable(EVENT_ID = 'E'+str(d.id), COLLECTED_AMOUNT = 0, FUND_STATUS = "Not Fulfilled", FUND_TAKEN_BY = 'Not Taken')
                    fund_table.save()
                messages.success(request, 'Success')
            else:
                return render (request, 'home/error.html')
    return render (request, 'organizor/create_event.html')

def event_details_o(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        checker = EventTable.objects.filter(CREATED_BY = email)
        return render (request, 'organizor/event_details_o.html', {'checker':checker})
    else:
        return render (request, 'home/error.html')

def packages(request):
    return render (request, 'organizor/packages.html')

