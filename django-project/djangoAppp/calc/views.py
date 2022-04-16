from django.shortcuts import render

# import HttpResponse 
from django.http import HttpResponse 
from django.conf import settings
# Create your views here.

def home(request):
	
	
	return render(request, 'home.html', { 'name':'Calc Application'})


