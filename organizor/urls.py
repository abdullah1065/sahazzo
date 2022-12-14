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
    path('SignupOrganizor/', views.SignupOrganizor,name='SignupOrganizor'),
    path('LoginOrganizor/', views.LoginOrganizor,name='LoginOrganizor'),
    path('organizor_profile/', views.organizor_profile,name='organizor_profile'),
    path('create_event/', views.create_event,name='create_event'),
    path('event_details_o/', views.event_details_o,name='event_details_o'),
    path('packages/', views.packages,name='packages'),
]

    
   