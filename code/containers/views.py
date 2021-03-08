# containers/views.py
from django.views.generic import ListView
from .models import Container
from django.shortcuts import render

from rest_framework.views import APIView
import docker

def homeView(request):
    return render(request, 'containers/home.html')

# creates json style data from container list
def container_to_json(container_list):
    data = []
    for i in range(len(container_list)):
        data.append({"container_name:": container_list[i].attrs['Config']['Image'],
                     "container_id:": container_list[i].id,
                     "container_status:": container_list[i].status})   
    return data

# creates container objects with create method in models.py
# because it would add them every time to db the function deletes first
# everything
def add_container_objects(container_list):
    Container.objects.all().delete()
    data = []
    for i in range(len(container_list)):
        data.append({"container_name": container_list[i].attrs['Config']['Image'],
                     "container_id": container_list[i].id,
                     "status": container_list[i].status})   
        cont = Container.create(container_list[i].attrs['Config']['Image'], container_list[i].id,container_list[i].status)
        cont.save()

#  execute function and create objects
add_container_objects(docker.from_env().containers.list(all))

class ContainerListView(ListView):
    model = Container
    template_name = 'container_list.html'

# optional to see the containers right now
# as add_container_objects-function needs to be updated with
# possibly updateview or refresh option
def liveContainerListView(request):
    client = docker.from_env()
    container_list = client.containers.list(all)
    data = container_to_json(container_list)
    context={'data':data}
    return render(request, 'containers/container_list_live.html',context)

class ContainerData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        client = docker.from_env()
        container_list = client.containers.list(all)

        data = container_to_json(container_list)
        return Response(data)
