# Ansible Lab Manager

Create running lab environments from Ansible inventory.

This tool reads [Ansible](https://www.ansible.com/) inventory and
outputs a [docker-compose](https://docs.docker.com/compose/) file to
turn the hosts in that inventory into something live.

Trying to learn Ansible?  Want to experiment with some examples?
Run `ansible-lab-manager` and `docker-compose up` and your lab
will be running in a few seconds.

## Get Started

There are two approaches:  use all docker all the time, or use your
local system to initialize the environment.

### All Docker

This approach makes only one assumption about your local environment:
you have Docker and Docker Compose installed.

 ``` bash
docker run \
       --rm \
       --volume `pwd`:/home/ansible/project \
       --user root \
       timfreund/ansible-lab:alm \
       ansible-lab-manager \
       --inventory ./hosts
```

If you're brand new to docker you may wonder what that command does.
This is the same command but annotated:

``` bash
docker run \                                           # docker will run a container
       --rm \                                          # delete the container when it exits
       --volume `pwd`:/home/ansible/project \          # mount your current directory in the container at /home/ansible/project
       --user root \                                   # run as root so the command can write to the local directory
       timfreund/ansible-lab:alm \                     # the image docker will pull and run
       ansible-lab-manager \                           # the command to run
       --inventory ./hosts                             # the inventory file to transform
```

You should now see a `docker-compose.yml` file in your current
directory.  Feel free to check it out, or bring your environment
online:

``` bash
docker-compose up -d
```

Skip the "Local Initialization" section and resume reading at "How to Work"

### Local Initialization

``` bash
python3 -m venv venv
. venv/bin/activate
pip install -e git+https://github.com/timfreund/ansible-lab-manager.git#egg=ansible-lab-manager
ansible-lab-manager --inventory ./hosts
docker-compose up
```

## How to Work

Now that we have a `docker-compose.yml` file how do we do make changes
and test them in the environment?

### Access the ansible control container

``` bash
docker-compose exec ansible /bin/bash --login
```

That command tells docker-compose to exec(ute) a command in the
ansible container, and the command to execute is `/bin/bash --login`.

The first time it runs, you'll see ssh-keygen output similar to this:

``` bash
Generating public/private rsa key pair.
Your identification has been saved in /home/ansible/.ssh/id_rsa.
Your public key has been saved in /home/ansible/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:1wprfAi+vkERqhXroj5LWxUtSoCtAV61eF7pwH9fHoo ansible@ansible
The key's randomart image is:
+---[RSA 2048]----+
|+o .o..          |
|+ + o+o..        |
| + o+B.+         |
|. .++ B.   .     |
|  o..oooS.. .o   |
| . ..o o.=o.+ .  |
|.. .  o =Eoo .   |
|o.o    + .       |
| +o  .+.         |
+----[SHA256]-----+
ansible@ansible:~$
```

The login script created a new SSH key for you and distributed it to
all of the other containers in the project.

Your local directory is mounted in the ansible container at ~ansible/project.

## Warnings and Caveats

Docker containers are not virtual machines.  There will be a number of
corner cases where the dockerized environment won't behave exactly as
a "real" (physical or virtual) machine would.  But if you're just learning
or if you're experimenting with userland things this solution will likely
work well enough.

## Future Work

The tool only supports docker-compose as an output right now, but there's
no technical limitation.  This tool could support multiple outputs including

- [CloudFormation](https://aws.amazon.com/cloudformation/)
- [Terraform](https://www.terraform.io/)
- [LXD](https://linuxcontainers.org/lxd/introduction/)
- ... or many other solutions...

It only supports docker-compose right now because lightweight training
environments for engineers new to the tool is our primary goal.  Many
Ansible training resources suggest
[Vagrant](https://www.vagrantup.com/), but I felt that anyone learning
Ansible will also likely be learning docker, so they'd already have
Docker installed or it wouldn't take much convincing to do so.
