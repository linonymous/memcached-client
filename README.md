# Memcached


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


##### What is memcached ?

Memcached is free & open source, high performance distributed memory object caching system. It is used to decrease database load for scalable system architectures.

##### How does it work ?

* based on client-server architecture
* default port 11211
* stores key-value pairs 
* servers keep the data in RAM and discards the oldest data when RAM is full

##### Advantages

* Distributed Memory Architecture
* Data store on server
* Has a session handler
* Runs across platforms such as Linux/Unix/Mac
* Easy to use

##### Disadvantages

* Volatile storage, i.e. when server crashes, data in memory is lost
* Demands large memory, subjective to requirements
* Security, i.e. there is no authentication mechanism provided by memcached
* Not enough documentation

##### When to use ?

* To scale the database, cache the data which is queried more frequently.

