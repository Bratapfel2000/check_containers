# container_project/urls.py
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('containers.urls')), 
	path('api/', include('api.urls')),
]