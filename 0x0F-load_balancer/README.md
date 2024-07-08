# Project Overview

A load balancer is a hardware or software components that distributes the load
(HTTP traffic) from the clients computer to the servers in the backend. 
This distribution is dependent upon the algorithm implemented.

This project focusses on the installation and configuration of HAproxy load
balancer.

## Two web servers
Two web servers are provided to remove the single point of failure. The round
robin algorithm is applied to ensure that each of the servers handle the request
 its choice ensures that we are able to test if the requests are distributed
between them.

The two identical servers have been installed and configured from the previous project.