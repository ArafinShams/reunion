from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
# import models to access db data
from .models import RegistrationPersonal, RegistrationAddress,RegistrationPayment
# Create your views here.

#function based view
# def home(request):
# 	return render (request, "home.html", {})

class RegistreView(TemplateView):
	template_name = 'registre.html'
	def get_context_data(self, *args, **kwargs):
		context = super(RegistreView, self).get_context_data(*args, **kwargs)
		return context

class RegistredView(TemplateView):
	template_name = 'registred.html'
	def get_context_data(self, *args, **kwargs):
		context = super(RegistredView, self).get_context_data(*args, **kwargs)
		return context

# class RegistredDetails(TemplateView):
# 	template_name = 'registreddetails.html'
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(RegistredDetails, self).get_context_data(*args, **kwargs)
# 		return context

# Showing Registered Data in templete Funciton Based View
# def Registred_Listview(request):
# 	template_name = 'registrations/registred_list.html'
# 	queryset =  RegistrationAddress.objects.all()
# 	context = {
# 	"object_list": queryset
# 	}
# 	return render(request, template_name, context)

# Showing Registered Data in templete Class Based View
# class RegistredListview(ListView):
# 	template_name = 'registrations/registred_list.html'
# 	model = Address
# 	def get_context_data(self,  *args,**kwargs):
# 		context = super(RegistredListview, self).get_context_data(*args, **kwargs)
# 		return context
# class RegistredListview(ListView):
# 	queryset =  RegistrationAddress.objects.all()

class RegistredListview(ListView):
	queryset =  RegistrationPayment.objects.all()


# #Detail View using priimary key
# class RegistredDetailView(DetailView):
# 	queryset =  RegistrationAddress.objects.all()

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(RegistredDetailView, self).get_context_data(*args, **kwargs)
# 		return context

#Detail View using priimary key
class RegistredDetailView(DetailView):
	queryset =  RegistrationPayment.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(RegistredDetailView, self).get_context_data(*args, **kwargs)
		return context
