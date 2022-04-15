from django.shortcuts import render

# import HttpResponse 
from django.http import HttpResponse 
# Create your views here.

def home(request):


	return render(request, 'home.html', { 'name':'Calc Application'})