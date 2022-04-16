# Import path into your created URL
from django.urls import path 

# Import views inside the app URLs 
from .import views 

# Mapp / create the urls bellow 

urlpatterns = [
	
	path('', views.home),
	# path('', views.studentList)

]