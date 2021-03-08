# api/views.py
from rest_framework import generics
from containers.models import Container
from .serializers import ContainerSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters

class ContainerAPIView(generics.ListAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['container_name']
