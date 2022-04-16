from django.shortcuts import render

# import HttpResponse 
from django.http import HttpResponse 
from django.conf import settings
from django.shortcuts import redirect
# The model should be imported here, otherwise 
# it will not work
from .models import Student
# Create your views here.

class Hero:
	def __init__(self, name, fname):
		self.name = name
		self.fname = fname


def home(request):
	
	if request.method == "POST":
		name = request.POST['name']
		fname = request.POST['fname']
		st = Student(name =name, fname=fname)
		st.save()

	studentList = Student.objects.all()

	return render(request, 'home.html', { 'studentList':studentList})

def deleteItem(request, id):

	Student.objects.filter(id=id).delete()
	return redirect('/')


def editItem(request, id):
	editItem = Student.objects.get(id=id)
	studentList = Student.objects.all()
	editData ={
		'editItem': editItem,
		'studentList': studentList
	}
	return render(request, 'home.html', editData)

def updateItem(request, id):
	if request.method =='POST':
		up = Student.objects.get(id=id)
		up.name = request.POST['name']
		up.fname = request.POST['fname']
		up.save()
		return redirect('/')