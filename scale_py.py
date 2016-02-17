#!/usr/bin/env python
instance=3
high_threshold=50
low_threshold=20
while True:
    cpuUsage=[]
    cpuUsage=(sudo docker stats --no-stream | awk '{print $2}')
    break;
print (cpuUsage)

