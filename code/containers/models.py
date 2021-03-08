# containers/models.py
from django.db import models

class Container(models.Model):
    container_name = models.CharField(max_length=250)
    container_id = models.CharField(max_length=50)
    container_status = models.CharField(max_length=50)

    @classmethod
    def create(cls, container_name, container_id, container_status):
        cont = cls(container_name=container_name, container_id=container_id, container_status=container_status)
        return cont

    def __str__(self):
    	return self.container_name
