# VMC Lab Environment
A collection of scripts and Ansible playbooks required to provision a VMC lab environment. You
can find more detailed documentation on this repository [here](http://www.google.com).

## Customize strings.yml file
The `strings.yml` file contains some strings that will be unique to your lab. You should review
all options to ensure they conform to your requirements. Most importantly, ensure that:

1. userid is the unique value used to identify the user
2. domain\_name will be the name given to your Active Directory domain, and should be registered
to you on the Internet if you intend to expose some services externally.
3. network\_subnet is the subnet under which all your machines will reside.

## Create the ansible vault
The ansible vault file contains all the sensitive data that should not be left unencrypted
on the control node. There is a sample_vault.yml file that contains all the values
expected to exist by the playbooks in this project. Modify it with the correct values
for your environment then encrypt it and rename it to vault.yml:

`mv sample-vault.yml vault.yml
ansible-vault encrypt sample_vault.yml`

## Prepare Lab Environment
The following assumptions are made regarding the vSphere environment that will be hosting
this lab.
1. The PortGroup used by all machines follows the naming convention `john-192.168.70.0-24`.
2. A resource group with the same name as the userid selected in `strings.yml`.
3. A workload folder for your virtual machines with the same name as the userid selected in
`strings.yml`.

## Create a bootstrap ISO
Before running the playbooks for Windows and Linux template creation, generate the bootstrap ISO
from the source by running the following command from the repository root:

`mkisofs -l -relaxed-filenames -V OEMDRV -o /tmp/bootstrap.iso ./bootstrap/`

For creating both Windows and Linux templates, a response file is needed to provide answers to all
installation parameters that would normally be specified during a manual install. For Windows, that
takes the form of an autounattend.xml answer file, and for Linux that would be the anaconda-ks.cfg
kickstart file. Those files are included in the bootstrap directory of this repository. There are
two options for including these bootstrap files during installation:

(i) Modifying the installer ISO to include the bootstrap file
(ii) Creating a separate ISO with the bootstrap file and mounting it as a second disc

Option (i) allows us to make other useful customizations to the installer ISO that will make the
installation process even more automation-friendly, but the process is tedious and not worth the
added effort. The playbooks therefore assume a bootstrap.iso file exists in a specified datastore
and will take care of mounting it before booting the installation ISO. 

## Create the OS templates
To create the OS templates, run the create\_[OS]\_template.yml playbook corresponding to the OS
you're creating a template for. The playbook will take care of creating the virtual machine,
installing the OS per the bootstrap file specification in the bootstrap ISO, configuring the
machine hardware, and converting it into a template.

> :warning: **When creating a Windows template, the bootable Windows installation disc requires
a key to be pressed during the boot process in order to boot into the disc. For this reason,
the Windows template creation will**

## Run a playbook
To run any of the playbooks included in the project, the command to use will have the following
format:

`ansible-playbook -i inventory.ini --ask-vault-pass playbook.yml`

You will be prompted for the vault password you chose earlier.
