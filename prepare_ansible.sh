#!/bin/sh
# A shell script to prepare the Ansible control node for the VMC lab
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: May/17/2020
# -------------------------------------------------------------------------------------------------
sudo dnf -y install ansible
sudo dnf -y install krb5-devel krb5-workstation
pip install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git
# Needed for ldap_entry module (TODO: consider alternatives?)
dnf install python3-devel openldap-devel gcc -y
pip install python-ldap
# Needed for CredSSP authentication to Windows hosts
pip install ntlm-auth --upgrade
pip install pywinrm[credssp]
sed -i -r 's/^#(log_path.*)/\1/' /etc/ansible/ansible.cfg
