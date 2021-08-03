#!/bin/sh
# A root-owned shell script to run the playbooks from an API server using a non-root account.
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: Aug/03/2021
# -------------------------------------------------------------------------------------------------
ansible-playbook -i inventory.ini
