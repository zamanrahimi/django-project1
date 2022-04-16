from django.shortcuts import render

# import HttpResponse 
from django.http import HttpResponse 
from django.conf import settings
# The model should be imported here, otherwise 
# it will not work
from .models import Student
# Create your views here.

def home(request):
	
	studentList = Student.objects.all()

	return render(request, 'home.html', { 'studentList':studentList})


