# Ansible Lab Manager

Create running lab environments from Ansible inventory.

This tool reads [Ansible](https://www.ansible.com/) inventory and
outputs a [docker-compose](https://docs.docker.com/compose/) file to
turn the hosts in that inventory into something live.

Trying to learn Ansible?  Want to experiment with some examples?
Run `ansible-lab-manager` and `docker-compose up` and your lab
will be running in a few seconds.

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
