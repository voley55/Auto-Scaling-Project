****************************************Auto Scaling Project***************************************

Intial set-up:
Haproxy---------->Web-Server1---------Web-Server2
Haproxy runs on the host machine and both the web servers are running instances of docker containers.

AIM:
Depending on the current load (requests), our infrastructure should be able to scaleup and down i.e.
spawning and de-spawning of docker containers.

Solution:
For scaling the infrastructure, I have a written a script 'scale', which calculates average CPU util-
isation after every two seconds.And if Average CPU utilisation is above high_threshold (currently set
as 40%),it spawns a new docker instance and add it's IP to the haproxy.cfg and reloads it. This adds
the new web-server in to the running infrastructure.Similarly,if Average CPU utilisation goes below 
low_threshold (currently set as 5%) continuously for 10 seconds, it de-spawns a running web server.

At anytime, we do not stop our initial set up. This can be turned off manually only.When we stop the
script (scale) by pressing ctrl+c, it de-spawns all the added web servers (other than initial set up) 
and restores the initial haproxy.cfg settings.

Steps for initial set up and get things running:
1. Install haproxy(load balancer) on the host machine. Change the haproxy.cfg depending on your set
up.Sample haproxy.cfg is provided in the project repository.
2. Install docker on the host machine. From inside the Apache folder of repository,run the following 
command to build a web server image.
Note: index.html file can be changed depending on what you want to display.
>docker build -t my-apache2 .
For more information on the apache docker image: https://hub.docker.com/_/httpd/
3. Run two instances of the apache docker image. Use the following command:
>sudo docker run -it my-apache2
Note: Number of web servers running initially can be changed, depending on the backend defined in the
haproxy.cfg
4. Start the haproxy service.
5. Now you can check that your infrastructure is up and running by requesting an index page from the
haproxy frontend IP.
6. Run the scale script.
7. Perform AB-testing on the haproxy, to check how your infrastructure is scaling.
