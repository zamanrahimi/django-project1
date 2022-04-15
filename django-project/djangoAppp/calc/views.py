from django.shortcuts import render

# import HttpResponse 
from django.http import HttpResponse 
# Create your views here.

def home(request):
	return HttpResponse("Welcome to first application in Djanog")
