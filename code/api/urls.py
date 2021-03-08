# api/urls.py
from django.urls import path
from .views import ContainerAPIView

urlpatterns = [
	path('', ContainerAPIView.as_view(), name='api-container'),
]