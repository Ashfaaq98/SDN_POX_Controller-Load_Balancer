#!/bin/bash
#Purpose: Retrieving the bandwidth information on remote servers and saving it in a text file
#Version:1.0
#Created date: Sun 17 Oct 2021 03:49:36 PM +0530
#START

rm -rf /home/pi/values
for i in `cat /home/pi/serverlist`
do
	
	bandwidth=`ssh $i bwm-ng -I eth0 -o plain -c 1 -d 1 | tail -n1 | awk '{print $4}' | awk -F. '{print $1}'`
	echo "$bandwidth" >> /home/pi/values
done


#END
