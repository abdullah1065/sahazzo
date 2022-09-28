"""d_sahazzo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('LoginAdmin/', views.LoginAdmin, name='LoginAdmin'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('manageEvents/', views.manageEvents, name='manageEvents'),
    path('shopPayment/', views.shopPayment, name='shopPayment'),
    path('collectFund/', views.collectFund, name='collectFund'),
    path('donatorDatabase/', views.donatorDatabase, name='donatorDatabase'),
    path('organizorDatabase/', views.organizorDatabase, name='organizorDatabase'),
    path('volunteerDatabase/', views.volunteerDatabase, name='volunteerDatabase'),
    path('updatePerson/<str:id>', views.updatePerson, name='updatePerson'),
    path('deletePerson/<str:id>', views.deletePerson, name='deletePerson'),
    path('updateEvent/<str:id>', views.updateEvent, name='updateEvent'),
    path('deleteEvent/<str:id>', views.deleteEvent, name='deleteEvent'),
    path('paymentConfirm/<str:id>', views.paymentConfirm, name='paymentConfirm'),
    path('collectFundConfirm/<str:id>', views.collectFundConfirm, name='collectFundConfirm'),
]



    