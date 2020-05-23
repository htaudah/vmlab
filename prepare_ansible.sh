#!/bin/sh
# A shell script to prepare the Ansible control node for the VMC lab
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: May/17/2020
# -------------------------------------------------------------------------------------------------
sudo dnf install ansible
sudo pip install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git
