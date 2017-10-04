"""reunion URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from registrations.views import (
    RegistredListview, #ClassBases LIST view
    RegistredDetailView,#ClassBases DETAIL view
    # Registred_Listview, #Functionbased view 
    RegistreView,
    RegistredView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

# Static Pages
    url(r'^$', TemplateView.as_view(template_name='home.html')),
	url(r'^program/$', TemplateView.as_view(template_name ='program.html')),
	url(r'^contact/$', TemplateView.as_view(template_name ='contact.html')),

# New Registrations
    url(r'^registre/$', RegistreView.as_view(), name='registre'),

# Registered List
    #Using Functionbased View
    #url(r'^registredlist/', Registred_Listview), #FunctionBasedview 
    url(r'^registred/$', RegistredListview.as_view(), name='resistredlist'), #ClassBased view

# Registered Details
# # Details using Primary Key
    url(r'^registred/(?P<pk>\w*)/$', RegistredDetailView.as_view(), name='registreddetails')


]