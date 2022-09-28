from operator import imod
from queue import Empty
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import SignupVolunteerForm, LoginVolunteerForm
from home.models import PersonTable
from organizor.models import EventTable
from .models import  VolunteerTable

# Create your views here.
def SignupVolunteer(request):
    form = SignupVolunteerForm()
    if request.method == 'POST':
        data = SignupVolunteerForm(request.POST)
        if data.is_valid():
            p_id = "V"
            first_name = data.cleaned_data['FIRST_NAME']
            last_name = data.cleaned_data['LAST_NAME']
            email = data.cleaned_data['EMAIL']
            contact = data.cleaned_data['CONTACT']
            nid = data.cleaned_data['NID']
            password = data.cleaned_data['PASSWORD']
            duplicate_checker = list(PersonTable.objects.filter(PersonType = p_id, EMAIL = email, NID = nid))
            if duplicate_checker == []:
                person_table = PersonTable(PersonType = p_id, FIRST_NAME = first_name, LAST_NAME = last_name, EMAIL = email, CONTACT = contact, NID = nid, PASSWORD = password)
                volunteer_table = VolunteerTable(V_ID = p_id, EMAIL = email, STATUS = 'Not in volunteering', VOLUNTARY = 'Null')
                person_table.save()
                volunteer_table.save()
            else:
                return render (request, 'home/error.html')
        else:
            return render (request, 'home/error.html')
        messages.success(request, 'Success')       
        return HttpResponseRedirect ('/home')
    return render (request, 'volunteer/SignupVolunteer.html', {'form':form})


def LoginVolunteer(request):
    form = LoginVolunteerForm()
    if request.method == 'POST':
        data = LoginVolunteerForm(request.POST)
        if data.is_valid():
            p_id = "V"
            email = data.cleaned_data['EMAIL']
            password = data.cleaned_data['PASSWORD']
            checker = PersonTable.objects.filter(PersonType = p_id, EMAIL = email, PASSWORD = password)
            getData = VolunteerTable.objects.filter(EMAIL = email)
            if list(checker) != []:
                request.session['EMAIL'] = email
                request.session['PASSWORD'] = password
                return render (request, 'volunteer/volunteer_profile.html', {'checker':checker, 'getData': getData})
            else:
                return render (request, 'home/error.html')
    return render (request, 'volunteer/LoginVolunteer.html', {'form':form})

def volunteer_profile(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        password = request.session['PASSWORD']
    checker = PersonTable.objects.filter(PersonType = "V", EMAIL = email, PASSWORD = password)
    getData = VolunteerTable.objects.filter(EMAIL = email)
    return render (request, 'volunteer/volunteer_profile.html', {'checker':checker, 'getData': getData})

def event_details_v(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        all_events = EventTable.objects.all()
        all_events_dict = {}
        for event in all_events:
          all_events_dict[f'E{event.id}'] = ['E'+str(event.id), event.EVENT_NAME, event.END_TIME, event.LOCATION]
        if request.method == 'POST':
            data = request.POST
            for keys,values in data.items():
                if keys == 'id': id_e = values
            selected_voluntary_event = VolunteerTable.objects.filter(EMAIL = email)
            if selected_voluntary_event[0].STATUS == 'Not in volunteering':
                selected_voluntary_event.update(STATUS = 'In volunteering', VOLUNTARY = id_e)
            else:
                return render(request,"home/error.html")
            return render (request, 'volunteer/volunteer_profile.html', {'checker':selected_voluntary_event})
    return render (request, 'volunteer/event_details_v.html', {'a_dict': all_events_dict})

def voluntaryHistory(request):
    if request.session.has_key('EMAIL') and request.session.has_key('PASSWORD'):
        email = request.session['EMAIL']
        selected_voluntary_event = VolunteerTable.objects.filter(EMAIL = email)
        if selected_voluntary_event[0].STATUS == 'In volunteering':
            return render (request, 'volunteer/voluntaryHistory.html', {'a_dict': selected_voluntary_event})
        else:
            return render(request,"home/error.html")
    else:
        return render (request, 'home/error.html')
   
