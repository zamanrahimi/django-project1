# Import path into your created URL
from django.urls import path 
from django.conf.urls.static import static
# Import views inside the app URLs 
from .import views 

# Mapp / create the urls bellow 

urlpatterns = [
	
	path('', views.home),
	path('delete/<int:id>/', views.deleteItem),


]