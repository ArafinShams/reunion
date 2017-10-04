from django.db import models

# Create your models here.
class RegistrationPersonal(models.Model):
	name           = models.CharField(max_length=120) 
	spousname      = models.CharField(max_length=120, null=True, blank=True)
	gender         = models.CharField(max_length=120)
	kids           = models.CharField(max_length=120, null=True, blank=True)
	mobilenumber   = models.CharField(max_length=30)
	email          = models.CharField(max_length=120, null=True, blank=True)
	bloodgroup     = models.CharField(max_length=120, null=True, blank=True)
	profession     = models.CharField(max_length=120, null=True, blank=True)
	organization   = models.CharField(max_length=120, null=True, blank=True)
	timestamp      = models.DateTimeField(auto_now_add=True)
	updated        = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "%s %s" %(self.mobilenumber, self.name)

class RegistrationAddress(models.Model):
	addserial         = models.ForeignKey(RegistrationPersonal, on_delete=models.CASCADE)
	mobilenumber      = models.CharField(max_length=30)
	address           = models.CharField(max_length=200)
	postcode          = models.CharField(max_length=10)
	thana             = models.CharField(max_length=120)
	district          = models.CharField(max_length=120)
	division          = models.CharField(max_length=120)
	mate              = models.CharField(max_length=10)
	spous             = models.CharField(max_length=10)
	kids              = models.CharField(max_length=10)
	guests            = models.CharField(max_length=10)
	others            = models.CharField(max_length=10)
	total             = models.CharField(max_length=100)
	note              = models.CharField(max_length=100)
	timestamp         = models.DateTimeField(auto_now_add=True)
	updated           = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "%s %s %s" %(self.mobilenumber, self.total, self.district)


class RegistrationPayment(models.Model):
	payserial         = models.ForeignKey(RegistrationAddress, on_delete=models.CASCADE)
	mobilenumber      = models.CharField(max_length=30)
	amount            = models.CharField(max_length=200)
	method            = models.CharField(max_length=10)
	details           = models.CharField(max_length=120)
	remarks           = models.CharField(max_length=120)
	timestamp         = models.DateTimeField(auto_now_add=True)
	updated           = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "%s %s" %(self.mobilenumber, self.amount)
