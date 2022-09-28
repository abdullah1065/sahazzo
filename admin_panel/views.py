from http.client import CREATED
from operator import imod
from queue import Empty
from selectors import EVENT_READ
from django.db.models import Sum
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import LoginAdminForm
from home.models import PersonTable
from donator.models import DonatorTable, DonateTable, FundTable
from organizor.models import OrganizorTable, EventTable, ShopTable
from volunteer.models import VolunteerTable


# Create your views here.
def LoginAdmin(request):
    form = LoginAdminForm()
    if request.method == 'POST':
        data = LoginAdminForm(request.POST)
        if data.is_valid():
            p_id = "A"
            email = data.cleaned_data['EMAIL']
            password = data.cleaned_data['PASSWORD']
            checker = PersonTable.objects.filter(PersonType = p_id, EMAIL = email, PASSWORD = password)
            if list(checker) != []:
                request.session['EMAIL'] = email
                request.session['PASSWORD'] = password
                return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
            else:
                return render (request, 'home/error.html')
    return render (request, 'admin_panel/LoginAdmin.html', {'form':form})

def admin_profile(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
    checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
    return render (request, 'admin_panel/admin_profile.html', {'checker':checker})

def manageEvents(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        total_events = EventTable.objects.all().count()
        cat1 = EventTable.objects.filter(EVENT_FOR = 'Myself').count()
        cat2 = EventTable.objects.filter(EVENT_FOR = 'My family').count()
        cat3 = EventTable.objects.filter(EVENT_FOR = 'People of my area').count()
        events_info = EventTable.objects.all()
        dashboard_dict, event_database_dict = {'INFO':[total_events,cat1,cat2,cat3]}, {}
        for event_info in events_info:
            fund_info = FundTable.objects.get(EVENT_ID = 'E'+str(event_info.id))
            event_database_dict[event_info.id] = ['E'+str(event_info.id), event_info.EVENT_NAME, event_info.LOCATION, event_info.BUDGET, event_info.CREATED_BY, fund_info.COLLECTED_AMOUNT, event_info.SHOP]
    return render (request, 'admin_panel/manageEvents.html', {'dashboard_dict': dashboard_dict, 'event_database_dict': event_database_dict})

def shopPayment(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        total_shops = ShopTable.objects.values('SHOP_NAME').distinct().count()
        total_payment = ShopTable.objects.filter(DELIVERY_STATUS = 'Processing').aggregate(Sum('PAY_DEMAND'))['PAY_DEMAND__sum']
        total_pay_demand = ShopTable.objects.filter(DELIVERY_STATUS = 'Pending').aggregate(Sum('PAY_DEMAND'))['PAY_DEMAND__sum']
        orders_info = ShopTable.objects.all()
        dashboard_dict, order_database_dict = {'INFO':[total_shops,total_payment,total_pay_demand]}, {}
        for order_info in orders_info:
            order_database_dict[order_info.id] = [order_info.SHOP_NAME,'E'+str(order_info.id), order_info.PAY_DEMAND, order_info.DELIVERY_STATUS]
    return render (request, 'admin_panel/shopPayment.html', {'dashboard_dict': dashboard_dict, 'order_database_dict': order_database_dict})

def collectFund(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        total_fund = FundTable.objects.values('EVENT_ID').distinct().count()
        total_fund_amount = FundTable.objects.aggregate(Sum('COLLECTED_AMOUNT'))['COLLECTED_AMOUNT__sum']
        pending_fund = FundTable.objects.filter(FUND_STATUS = 'Not Fulfilled').count()
        complete_fund = FundTable.objects.filter(FUND_STATUS = 'Fulfilled').count()
        funds_info = EventTable.objects.all()
        dashboard_dict, fund_database_dict = {'INFO':[total_fund,total_fund_amount,pending_fund,complete_fund]}, {}
        for fund_info in funds_info:
            fund_table_info = FundTable.objects.get(EVENT_ID ='E'+str(fund_info.id))
            fund_database_dict[fund_info.id] = ['E'+str(fund_info.id), fund_info.EVENT_NAME, fund_info.BUDGET, fund_table_info.COLLECTED_AMOUNT, fund_table_info.FUND_TAKEN_BY]
    return render (request, 'admin_panel/collectFund.html', {'dashboard_dict': dashboard_dict, 'fund_database_dict': fund_database_dict})

def donatorDatabase(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        total_donators = DonatorTable.objects.values('EMAIL').distinct().count()
        active_donators = DonateTable.objects.values('D_ID').distinct().count()
        idle_donators = total_donators - active_donators
        total_donations = FundTable.objects.aggregate(Sum('COLLECTED_AMOUNT'))['COLLECTED_AMOUNT__sum']
        donators_info = PersonTable.objects.filter(PersonType = "D")
        dashboard_dict, d_database_dict = {'INFO':[total_donators,active_donators,idle_donators,total_donations]}, {}
        for d_info in donators_info:
            d_database_dict[d_info.EMAIL] = ['D'+str(d_info.id), d_info.FIRST_NAME+' '+d_info.LAST_NAME, d_info.CONTACT, d_info.NID, d_info.EMAIL]
    return render (request, 'admin_panel/donatorDatabase.html', {'dashboard_dict': dashboard_dict, 'd_database_dict': d_database_dict})

def organizorDatabase(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        total_organizors = OrganizorTable.objects.values('EMAIL').distinct().count()
        active_organizors = EventTable.objects.values('CREATED_BY').distinct().count()
        idle_organizors = total_organizors - active_organizors
        organizors_info = PersonTable.objects.filter(PersonType = "O")
        dashboard_dict, o_database_dict = {'INFO':[total_organizors,active_organizors,idle_organizors]}, {}
        for o_info in organizors_info:
            o_database_dict[o_info.EMAIL] = ['O'+str(o_info.id), o_info.FIRST_NAME+' '+o_info.LAST_NAME, o_info.CONTACT, o_info.NID, o_info.EMAIL]
    return render (request, 'admin_panel/organizorDatabase.html', {'dashboard_dict': dashboard_dict, 'o_database_dict': o_database_dict})

def volunteerDatabase(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        total_volunteers = VolunteerTable.objects.values('EMAIL').distinct().count()
        active_volunteers = VolunteerTable.objects.filter(STATUS= 'In volunteering').count()
        idle_volunteers = total_volunteers - active_volunteers
        volunteers_info = PersonTable.objects.filter(PersonType = "V")
        dashboard_dict, v_database_dict = {'INFO':[total_volunteers,active_volunteers,idle_volunteers]}, {}
        for v_info in volunteers_info:
            volunteer_table_info = VolunteerTable.objects.get(EMAIL = v_info.EMAIL)
            v_database_dict[v_info.EMAIL] = ['V'+str(v_info.id), v_info.FIRST_NAME+' '+v_info.LAST_NAME, v_info.CONTACT, v_info.NID, v_info.EMAIL, volunteer_table_info.STATUS, volunteer_table_info.VOLUNTARY]
    return render (request, 'admin_panel/volunteerDatabase.html', {'dashboard_dict': dashboard_dict, 'v_database_dict': v_database_dict})

def updatePerson(request, id):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
        person_info = PersonTable.objects.get(PersonType = id[0], id = id[1:])
        database_dict = {}
        if person_info.PersonType == 'V':
            volunteer_table_info = VolunteerTable.objects.get(EMAIL = person_info.EMAIL)
            all_event_id = ['Null']
            events = EventTable.objects.all()
            for event in events:
                all_event_id.append('E'+str(event.id))
            database_dict[person_info.EMAIL] = [str(person_info.PersonType)+str(person_info.id), person_info.FIRST_NAME, person_info.LAST_NAME, person_info.NID, person_info.CONTACT, person_info.EMAIL, volunteer_table_info.STATUS, volunteer_table_info.VOLUNTARY, all_event_id]
        else:
            database_dict[person_info.EMAIL] = [str(person_info.PersonType)+str(person_info.id), person_info.FIRST_NAME, person_info.LAST_NAME, person_info.NID, person_info.CONTACT, person_info.EMAIL]
        if request.method == 'POST':
            data = request.POST
            for keys,values in data.items():
                if keys == 'FIRST_NAME': FIRST_NAME = values
                if keys == 'LAST_NAME': LAST_NAME = values
                if keys == 'EMAIL': EMAIL = values
                if keys == 'CONTACT': CONTACT = values
                if keys == 'NID': NID = values
                if keys == 'STATUS': STATUS = values
                if keys == 'VOLUNTARY': VOLUNTARY = values
            person_info.FIRST_NAME, person_info.LAST_NAME, person_info.NID, person_info.CONTACT, person_info.EMAIL = FIRST_NAME, LAST_NAME, NID, CONTACT, EMAIL
            person_info.save()
            if 'V' in id:
                if STATUS == 'In volunteering' and VOLUNTARY == 'Null':
                    return render(request,"home/error.html")
                elif VOLUNTARY != 'Null':
                    STATUS = 'In volunteering'
                elif STATUS == 'Not in volunteering':
                    VOLUNTARY = 'Null'
                volunteer_table_info.STATUS, volunteer_table_info.VOLUNTARY = STATUS, VOLUNTARY
                volunteer_table_info.save()
            messages.success(request, 'Success')
            return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
    return render (request, 'admin_panel/updatePerson.html', {'database_dict': database_dict})

def deletePerson(request, id):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
        person_info = PersonTable.objects.get(PersonType = id[0], id = id[1:])
        database_dict = {}
        if person_info.PersonType == 'V':
            volunteer_table_info = VolunteerTable.objects.get(EMAIL = person_info.EMAIL)
            all_event_id = ['Null']
            events = EventTable.objects.all()
            for event in events:
                all_event_id.append('E'+str(event.id))
            database_dict[person_info.EMAIL] = [str(person_info.PersonType)+str(person_info.id), person_info.FIRST_NAME, person_info.LAST_NAME, person_info.NID, person_info.CONTACT, person_info.EMAIL, volunteer_table_info.STATUS, volunteer_table_info.VOLUNTARY, all_event_id]
        else:
            database_dict[person_info.EMAIL] = [str(person_info.PersonType)+str(person_info.id), person_info.FIRST_NAME, person_info.LAST_NAME, person_info.NID, person_info.CONTACT, person_info.EMAIL]
        if request.method == 'POST':
            if 'D' in id:
                DonatorTable.objects.get(EMAIL = person_info.EMAIL).delete()
                DonateTable.objects.filter(D_ID = 'D'+str(person_info.id)).delete()
                person_info.delete()
            if 'O' in id:
                OrganizorTable.objects.get(EMAIL = person_info.EMAIL).delete()
                # ShopTable.objects.get(id = EventTable.objects.get(CREATED_BY = person_info.EMAIL).id).delete()
                # EventTable.objects.get(CREATED_BY = person_info.EMAIL).delete()
                person_info.delete()
            if 'V' in id:
                volunteer_table_info.delete()
                person_info.delete()
            messages.success(request, 'Success')
            return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
    return render (request, 'admin_panel/deletePerson.html', {'database_dict': database_dict})

def updateEvent(request, id):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
        event_info = EventTable.objects.get(id = id[1:])
        fund_info = FundTable.objects.get(EVENT_ID = 'E'+str(event_info.id))
        database_dict = { event_info.id : ['E'+str(event_info.id), event_info.EVENT_NAME, event_info.LOCATION, event_info.BUDGET, event_info.CREATED_BY, fund_info.COLLECTED_AMOUNT, event_info.SHOP]}
        if request.method == 'POST':
            data = request.POST
            for keys,values in data.items():
                if keys == 'EVENT_NAME': EVENT_NAME = values
                if keys == 'LOCATION': LOCATION = values
                if keys == 'BUDGET': BUDGET = values
                if keys == 'CREATED_BY': CREATED_BY = values
                if keys == 'COLLECTED_AMOUNT': COLLECTED_AMOUNT = values
                if keys == 'SHOP': SHOP = values
            event_info.EVENT_NAME, event_info.LOCATION, event_info.BUDGET, event_info.CREATED_BY, event_info.SHOP = EVENT_NAME, LOCATION, BUDGET, CREATED_BY, SHOP
            event_info.save()
            shop_info = ShopTable.objects.get(id = id[1:])
            shop_info.SHOP_NAME = SHOP
            shop_info.save()
            messages.success(request, 'Success')
            return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
    return render (request, 'admin_panel/updateEvent.html', {'database_dict': database_dict})

def deleteEvent(request, id):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
        event_info = EventTable.objects.get(id = id[1:])
        fund_info = FundTable.objects.get(EVENT_ID = 'E'+str(event_info.id))
        shop_info = ShopTable.objects.get(id = id[1:])
        database_dict = { event_info.id : ['E'+str(event_info.id), event_info.EVENT_NAME, event_info.LOCATION, event_info.BUDGET, event_info.CREATED_BY, fund_info.COLLECTED_AMOUNT, event_info.SHOP]}
        if request.method == 'POST':
            shop_info.delete()
            fund_info.delete()
            event_info.delete()
            messages.success(request, 'Success')
            return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
    return render (request, 'admin_panel/deleteEvent.html', {'database_dict': database_dict})

def paymentConfirm(request, id):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
        event_info = EventTable.objects.get(id = id[1:])
        fund_info = FundTable.objects.get(EVENT_ID = 'E'+str(event_info.id))
        shop_info = ShopTable.objects.get(id = id[1:])
        database_dict = { event_info.id : [shop_info.SHOP_NAME, event_info.EVENT_NAME, 'E'+str(event_info.id), shop_info.PAY_DEMAND]}
        if request.method == 'POST':
            if fund_info.FUND_STATUS == "Fulfilled":
                shop_info.DELIVERY_STATUS = "Processing"
                shop_info.save()
                messages.success(request, 'Success')
                return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
            else:
                return render(request,"home/error.html")
    return render (request, 'admin_panel/paymentConfirm.html', {'database_dict': database_dict})

def collectFundConfirm(request, id):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
        checker = PersonTable.objects.filter(PersonType = "A", EMAIL = email, PASSWORD = password)
        event_info = EventTable.objects.get(id = id[1:])
        fund_info = FundTable.objects.get(EVENT_ID = 'E'+str(event_info.id))
        shop_info = ShopTable.objects.get(id = id[1:])
        database_dict = { event_info.id : ['E'+str(event_info.id), event_info.EVENT_NAME, event_info.BUDGET, fund_info.COLLECTED_AMOUNT]}
        if request.method == 'POST':
            if fund_info.COLLECTED_AMOUNT == event_info.BUDGET:
                fund_info.FUND_TAKEN_BY = email
                fund_info.save()
                shop_info.DELIVERY_STATUS = "Pending Payment Confirmation"
                shop_info.save()
                messages.success(request, 'Success')
                return render (request, 'admin_panel/admin_profile.html', {'checker':checker})
            else:
                return render(request,"home/error.html")
    return render (request, 'admin_panel/collectFundConfirm.html', {'database_dict': database_dict})

