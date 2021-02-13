#!/bin/sh
# A shell script to prepare the Ansible control node for the VMC lab
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: May/17/2020
# -------------------------------------------------------------------------------------------------
sudo dnf -y install epel-release
sudo dnf -y install ansible
git clone https://github.com/vmware/vsphere-automation-sdk-python.git /tmp/vsphere-sdk
pip3 install --upgrade -r /tmp/vsphere-sdk/requirements.txt --extra-index-url file:///temp/vsphere-sdk/lib
pip3 install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git
# Needed for ldap_entry module (TODO: consider alternatives?)
dnf install python3-devel openldap-devel gcc -y
pip3 install python-ldap
# Needed for CredSSP authentication to Windows hosts
pip3 install ntlm-auth --upgrade
pip3 install pywinrm[credssp]
sed -i -r 's/^#(log_path.*)/\1/' /etc/ansible/ansible.cfg
# These collections provide additional functionality not yet available in base
# TODO: switching to AWS; no longer need vmware collections
