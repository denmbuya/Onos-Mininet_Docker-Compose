# Onos-Mininet Docker-compose
The following docker-compose.yml file is used to create, run and make interacting two docker containers: one for ONOS SDN controller, and the other one for Mininet.
Works on Windows/MacOS/Linux.

### How does it work?
First you need Docker compose, which relies on Docker engine, and so they both need to be installed.

Let's firstly procede with the environment setup
```
$ git clone https://gerrit.onosproject.org/onos
$ cd onos
$ cat << EOF >> ~/.bash_profile
export ONOS_ROOT="`pwd`"
source $ONOS_ROOT/tools/dev/bash_profile
EOF
$ . ~/.bash_profile
$ cd onos
```
Then clone this repository with the following command:
```
git clone https://github.com/Alepacox/Onos-Mininet_Docker-Compose.git
```
After that, move into the cloned folder and run 
```
docker-compose up
```
This will download and run both the containers.

Then, if you wish to create a random topology**, run in another term window:
```
docker exec -it mininet-c python topology.py
```
I also provided a start.sh script that asks directily if you want to create a new topology** while starting the containers.
(the script refers to gnome terminal: if you don't have it, just replace it with the one that you use)  

** **This requires that the following app are enabled at the Onos controller (disabled by default): OpenFlow Agent, OpenFlow Base Provider and OpenFlow Provider Suite** 


- ONOS Docker image --> [onosproject/onos](https://hub.docker.com/r/onosproject/onos/)
- Mininet Docker image --> [iwaseyusuke/mininet](https://hub.docker.com/r/iwaseyusuke/mininet/)
