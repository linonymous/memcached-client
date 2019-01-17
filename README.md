# memcached-client


First task is to install memcached server on linux/windows/mac and start the server. I used Redhat Linux 7.5 for the server.

##### How to install memcahced server and start the server?

1. install memcached using following command.
    `yum install memcached`
1. start the server 
    `systemctl start memcached`
1. check the port and service
    `ps -ef | grep memcached`
1. note the port number from the output of above command (11211 by default)
    `00:00:27 /usr/bin/memcached -u memcached -p 11211 -m 64 -c 1024`


##### How to install pymemcache?

1. activate the virtual environment and install pymemcache
    `pip install pymemcache`
1. now create an object of pymemcache.base.Client with ip address of the server and port number
1. perform set, get, add, delete and all the operations
1. Explore and Enjoy
