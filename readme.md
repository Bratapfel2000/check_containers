
<h1>
Instructions
</h1>
<br>

<h2>Quick Overview</h2>
<p>
I) Django Rest Solution, running on local machine and displaying all docker containers<br>
II) Docker Image on dockerhub, running but not displaying containers.<br>
III) For Kubernetes I had not enough time.</p>
<br>


<h3>
I) Django Rest
</h3>
<ul>
1.) Start Docker
</ul>
<ul>
2.) install python 3.7 and pipenv
</ul>
<ul>
3.) git clone <a href="https://github.com/Bratapfel2000/check_containers.git">https://github.com/Bratapfel2000/check_containers.git</a>  or download  <a href="https://github.com/Bratapfel2000/check_containers/archive/master.zip">https://github.com/Bratapfel2000/check_containers/archive/master.zip</a>
</ul>
<ul>
4.) go to check_containers folder and create pipenv with windows command / linux shell /Mac terminal: pipenv install --python 3.7
</ul>
<ul>
5.) in same folder run: pipenv install -r requirements.txt
</ul>
<ul>
6.) run: pipenv shell
</ul>
<ul>
7.) navigate to folder check_containers\code and enter: python manage.py runserver 8080
</ul>
<ul>
8.) open in browser <a href="http://127.0.0.1:8080/">http://127.0.0.1:8080/</a>
</ul>
<ul>
9.) Three links are shown: i) Container infos as objects in json format and REST Api ii) Same objects displayed in html iii) Container infos directly displayed, without being saved in db
</ul>
<ul>
10.) to build docker image go to /code folder and enter command: docker build -t simple-django-on-docker -f Dockerfile .
</ul>


<br>
<h3>
 II) Docker Image 
</h3>
<p>Find the image here:</p>
<p>docker pull paufourdm/container-check-image-1:latest</p>
<a href="https://hub.docker.com/repository/docker/paufourdm/container-check-image-1">https://hub.docker.com/repository/docker/paufourdm/container-check-image-1</a><br>
<p>
    Problem: Docker Image does not display docker containers because when docker.from_env() is activated 
    the image breakes so I had to disable it. <br>Now it doesn't display actual docker containers.<br>
    Problem might be that docker-py module in Django is not working and could be related with localhost port.
    Solution could be to change host in django docker client to something like 'host.docker.internal'
</p>
<br><br>
