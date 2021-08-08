#!/bin/sh
# A root-owned shell script to run the playbooks from an API server using a non-root account.
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: Aug/03/2021
# -------------------------------------------------------------------------------------------------
echo "${@: 2}" > /tmp/output
#ansible-playbook -i inventory.ini --vault-password-file /tmp/vault-pass --extra-vars "${@: 2}" "$1"
