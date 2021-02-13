#!/bin/sh
# A shell script to prepare the Ansible control node for the VMC lab
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: May/17/2020
# -------------------------------------------------------------------------------------------------
sudo dnf -y install epel-release
sudo dnf -y install ansible
# Needed for ldap_entry module (TODO: consider alternatives?)
sudo dnf install gcc python3-devel openldap-devel -y
pip3 install python-ldap
# Needed for CredSSP authentication to Windows hosts
pip3 install ntlm-auth --upgrade
pip3 install pywinrm[credssp]
# Needed to interact with AWS
pip3 install boto3
sudo sed -i -r 's/^#(log_path.*)/\1/' /etc/ansible/ansible.cfg
# These collections provide additional functionality not yet available in base
ansible-galaxy collection install community.aws
