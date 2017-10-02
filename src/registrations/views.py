from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
#function based view
# def home(request):
# 	return render (request, "home.html", {})
class HomeView(TemplateView):
	template_name = 'home.html'
	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		return context

class ProgramView(TemplateView):
	template_name = 'program.html'
	def get_context_data(self, *args, **kwargs):
		context = super(ProgramView, self).get_context_data(*args, **kwargs)
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'
	def get_context_data(self, *args, **kwargs):
		context = super(ContactView, self).get_context_data(*args, **kwargs)
		return context

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