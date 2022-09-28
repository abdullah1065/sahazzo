from django.http.response import HttpResponse
from django.shortcuts import render
#from home.models import PersonTable

# Create your views here.
def home(request):
    #person = PersonTable.objects.all()
    return render(request, 'home/home.html')

def error(request):
    return render(request, 'home/error.html')