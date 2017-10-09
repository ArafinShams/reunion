from django import forms
from .models import RegistrationPersonal, RegistrationAddress, RegistrationPayment

# class PersonalCreateForm(forms.Form):
# 	name           = forms.CharField()
# 	spousname      = forms.CharField()
# 	gender         = forms.CharField()
# 	kids           = forms.CharField()
# 	mobilenumber   = forms.CharField()
# 	email          = forms.CharField()
# 	bloodgroup     = forms.CharField()
# 	profession     = forms.CharField()
# 	organization   = forms.CharField()


class RegistrationPersonalCreateForm(forms.ModelForm):
	class Meta:
		model = RegistrationPersonal
		fields = [
		'name',
		'spousname',
		'gender',
		'kids',
		'mobilenumber',
		'email',
		'bloodgroup',
		'profession',
		'organization',
		]
	def clean_name(self):
		name =self.cleaned_data.get("name")
		if name == "Hello":
			raise foirms.ValidationError("NOt a valid name")
		return name

class RegistrationAddressCreateForm(forms.ModelForm):
	class Meta:
		model = RegistrationAddress
		fields = [
		'address',
		'postcode',
		'thana',
		'district',
		'division',
		'mate',
		'spous',
		'kids',
		'guests',
		'others',
		'total',
		]
	def clean_name(self):
		name =self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("NOt a valid name")
		return name

class RegistrationPaymentCreateForm(forms.ModelForm):
	class Meta:
		model = RegistrationPayment
		fields = []
