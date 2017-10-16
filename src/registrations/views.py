from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import RegistrationPersonalCreateForm, RegistrationAddressCreateForm, RegistrationPaymentCreateForm
# import models to access db data
from .models import RegistrationPersonal, RegistrationAddress, RegistrationPayment

# Create your views here.

class RegistredListview(ListView):
	template_name = 'registration_list.html'
	context_object_name = 'registered_lists'
	queryset =  RegistrationPayment.objects.all()

class RegistredDetailView(LoginRequiredMixin, DetailView):
	model = RegistrationPayment
	login_url = '/login/'
	template_name = 'registration_details.html'

def Registration_createview(request):
	personal_form = RegistrationPersonalCreateForm(prefix="personal") 
	address_form = RegistrationAddressCreateForm(prefix="address")
	payment_form = RegistrationPaymentCreateForm(prefix="payment")
	if request.POST:
		personal_form = RegistrationPersonalCreateForm(request.POST or None, request.FILES or None, prefix="personal")
		address_form = RegistrationAddressCreateForm(request.POST or None,prefix="address")
		payment_form = RegistrationPaymentCreateForm(request.POST or None,prefix="payment")
	per_errors = None
	add_errors = None
	pay_errors = None
	if personal_form.is_valid() and address_form.is_valid()and payment_form.is_valid():
		personal  = personal_form.save(commit=False)
		address   = address_form.save(commit=False)
		payment   = payment_form.save(commit=False)
		personal.save()
#Address Model Save
		#foreign Key Personal -> address
		address.registrationpersonal = personal
		address.mobilenumber = personal.mobilenumber

#Address Total Rate Mate = 2000, Spous = 7000, Guests = 7000, Kids = 700, Others = 500 
		grand_total = (int(address.mate) * 2000) + (int(address.spous) * 700) +  (int(address.guests) * 700) + (int(address.kids) * 700) + (int(address.others) * 500)
		address.total = str(grand_total)

		address.save()
#Payment Model Save
#foreign Key address -> Payment
		payment.registrationaddress = address
		payment.mobilenumber = address.mobilenumber
		payment.payableamount = address.total
		payment.save()
# Post Save
		return HttpResponseRedirect("/registration/")
	if personal_form.errors or address_form.errors or payment_form.errors:
		per_errors = personal_form.errors
		add_errors = address_form.errors
		pay_errors = payment_form.errors
	template_name = 'registration_create.html'
	context = {"personal_form": personal_form, "address_form": address_form, "per_errors": per_errors, "add_errors": add_errors, "pay_errors": pay_errors}
	return render(request, template_name, context)



class PaymentUpdate(LoginRequiredMixin, UpdateView):
	model = RegistrationPayment
	login_url = '/login/'
	template_name = 'payment_update.html'
	fields = [
	'mobilenumber', 'payableamount','paidamount', 'method', 'details', 'status', 'remarks'
	]
	success_url = '/registration/'


