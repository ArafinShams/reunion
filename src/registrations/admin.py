from django.contrib import admin

# Register your models here.
from .models import Personal, Address, Number

admin.site.register(Personal)
admin.site.register(Address)
admin.site.register(Number)