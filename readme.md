
<h1>
Docker image with REST Api to show all docker images
</h1>
<br>


<h3>
Instructions
</h3>
<ul>
1.) Start Docker
</ul>
<ul><br>
2.) Enter in command line: <br> <br>
<code>&nbsp;
docker pull paufourdm/container-check-image-1:2</code><br><br>

&nbsp;&nbsp;link to  dockerhub:
<a href="https://hub.docker.com/r/paufourdm/container-check-image-1">https://hub.docker.com/repository/docker/paufourdm/container-check-image-1:2</a><br>
<br> <br>
</ul>
<ul>
3.) enter in command line: <br> <br>
&nbsp;<code>
docker container run -d -p 8888:8888 -v /var/run/docker.sock:/var/run/docker.sock paufourdm/container-check-image-1:2docker ps
</code>
</ul>

<ul><br>
4.) open in browser <a href="http://localhost:8888/">http://localhost:8888/</a>
</ul>


<ul><br>
5.) 3 options show up:
<ul>
	i. ) will show containers with REST API and all containers saved in DB
	
</ul>
<ul>
	ii. ) all containers shown in html format
	
</ul>
<ul>
	iii. ) all containers shown directly without being saved in DB
	
</ul>
</ul>

