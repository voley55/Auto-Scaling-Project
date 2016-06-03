#Auto Scaling Project

##About
`scale` is a bash script that spawns and de-spawns docker containers depending on the current average cpu utilization of each of all the docker containers.
####Features:
  - Spawns new docker conatiners when average cpu utilisation goes above `high_threshold`
  - De-spawn docker containers when average cpu utilisation goes below `low_threshold`. But at all times, the initial setup (shown below) remains intact.
  - In order to have high availabiltiy, it also supports failover feature for HAproxy.

##Intial set-up
![alt tag](https://github.com/voley55/Auto-Scaling-Project/blob/master/AutoScale.png)

##Installation and Usage

####Requirements:
- HAproxy 1.6  (http://www.haproxy.org/)
- Docker (https://docs.docker.com/engine/installation/)
- Keepalived (http://www.keepalived.org/software/)

####Steps:
After installing all of the above requirements do the following:
-  Edit the `haproxy.cfg` and define the appropriate frontend and backends. A sample `haproxy.cfg` is provided in the repository.
-  From inside the `Apache` folder of the repository,run the following command to build a web server image.
  `docker build -t my-apache2 .`
  -  For more information on the apache docker image: (https://hub.docker.com/_/httpd/)
- Start the docker service and spawn two docker containers with static IPs in the docker ip range. This can be checked by spawning one test docker and inspect it to check it's IP. Also, these two docker IPs should be mentioned under backends in the `haproxy.cfg`
```
sudo docker run -it --ip==static_ip1 my-apache2
sudo docker run -it --ip==static_ip2 my-apache2
```
- Start the haproxy service.
- Check that your infrastructure is up and running by requesting an index page from the HAproxy frontend IP.
- Run the `scale` script.
```
./scale
```
- Perform AB-testing on the haproxy, to check how your infrastructure is scaling.

##Limitations
- Statically assign IP addresses to the initial two docker containers as mentioned in the haproxy.conf
- In case of distributed architecture using keepalived, this script doesn't utilize the resources of the systems except on which it is running.

##License
GNU GPLv3
