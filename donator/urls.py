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
    path('SignupDonator/', views.SignupDonator, name='SignupDonator'),
    path('LoginDonator/', views.LoginDonator, name='LoginDonator'),
    path('donator_profile/', views.donator_profile, name='donator_profile'),
    path('event_details_d/', views.event_details_d, name='event_details_d'),
    path('donateHistory/', views.donateHistory, name='donateHistory'),
]


    
    