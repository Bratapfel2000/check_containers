# containers/urls.py
from django.urls import path
from .views import ContainerListView, liveContainerListView, homeView
from . import views

urlpatterns = [
	path('', views.homeView, name='home'),
	path('all/', ContainerListView.as_view(), name='all'),
	path('live/', views.liveContainerListView, name='live-container'),
]