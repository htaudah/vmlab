#!/bin/sh
# A shell script to prepare the Ansible control node for the VMC lab
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: May/17/2020
# -------------------------------------------------------------------------------------------------
sudo dnf install ansible -y
pip install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git
sed -i -r 's/^#(log_path.*)/\1/' /etc/ansible/ansible.cfg
