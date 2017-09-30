from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#function based view
def home(request):
	return render (request, "base.html", {})

def home2(request):
	return render (request, "base.html", {})

def home3(request):
	return render (request, "base.html", {})

def home4(request):
	return render (request, "base.html", {})