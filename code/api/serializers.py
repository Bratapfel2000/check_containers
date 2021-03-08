# api/serializers.py
from rest_framework import serializers
from containers.models import Container

class ContainerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Container
		fields = ('container_name', 'container_id', 'container_status')
