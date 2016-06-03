#Auto Scaling Project

##About
`scale` is a bash script that spawns and de-spawns docker containers depending on the current average cpu utilization of each of all the docker containers.
###Features:
  - Spawns new docker conatiners when average cpu utilisation goes above `hight_hreshold`
  - De-spawn docker containers when average cpu utilisation goes below `low_threshold`. But at all times, the initial setup (shown below) remains intact.
  - In order to have high availabiltiy, it also supports failover feature for haproxy.

##Intial set-up
![alt tag](https://github.com/voley55/Auto-Scaling-Project/blob/master/AutoScale.png)

##Installation and Usage

###Requirements
-Install haproxy(load balancer) on the host machine. Change the haproxy.cfg depending on your set
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
