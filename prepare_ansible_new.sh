#!/bin/sh
# A shell script to prepare the Ansible control node for the VMC lab (run as root).
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: May/17/2020
# -------------------------------------------------------------------------------------------------
#dnf -y install epel-release
pip3 install ansible
git clone https://github.com/vmware/vsphere-automation-sdk-python.git /tmp/vsphere-sdk
pip3 install --upgrade -r /tmp/vsphere-sdk/requirements.txt --extra-index-url file:///tmp/vsphere-sdk/lib
pip3 install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git
# Needed for ldap_entry module (TODO: consider alternatives?)
#dnf install python3-devel openldap-devel gcc -y
#pip3 install python-ldap
# Needed for CredSSP authentication to Windows hosts
pip3 install ntlm-auth --upgrade
pip3 install pywinrm[credssp]
mkdir /etc/ansible
cp ./configuration/ansible.cfg /etc/ansible
# These collections provide additional functionality not yet available in base
ansible-galaxy collection install community.vmware
ansible-galaxy collection install ansible.windows
ansible-galaxy collection install community.windows
ansible-galaxy collection install community.general
ansible-galaxy collection install community.aws
ansible-galaxy collection install ansible.posix
rm -rf ~/.ansible/collections/ansible_collections/community/vmware/
rm -rf ~/.ansible/collections/ansible_collections/community/general/
git clone https://github.com/htaudah/vmware.git ~/.ansible/collections/ansible_collections/community/vmware
git clone https://github.com/htaudah/community.general.git ~/.ansible/collections/ansible_collections/community/general
pip3 install pyvmomi
# Needed for hashing and setting passwords for local Linux users
pip3 install passlib
# Needed for the json_query filter
pip3 install jmespath
