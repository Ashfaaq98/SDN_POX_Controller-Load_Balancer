# SDN_POX_Controller-Load_Balancer

Software Defined Networks have changed the way networks operate. The traditional computer networks consisted of expensive network devices. One such device that is used to perform a network function is a load balancer. A load balancer distributes client requests between servers.

The algorithm is based on the least bandwidth of a server at a particle time. Servers will the send the bandwidth information on a timely configured basis through a wireless network to the controller and the controller will use this information to calculate the most suitable server. The application is built on the POX controller based on python. 

1) ip_loadbalancer.py

This module comes with the POX controller. The algorithm used in this module is random algorithm. 

2) ip_rr.py

This module contains the round robin algorithm.

3) ip_bw.py

This module contains the least bandwidth algorithm

All the load balancing modules require the virtual IP address and the IP address of the servers to be provided.
