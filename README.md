# VMC Lab Environment
A collection of scripts and Ansible playbooks required to provision a VMC lab environment. You
can find more detailed documentation on this repository [here](http://www.google.com).

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
and will take care of mounting it before booting the installation ISO. To create the bootstrap.iso
file, simply run the following command from the repository root directory:

## Create the OS templates
To create the OS templates, run the create\_[OS]\_template.yml playbook corresponding to the OS
you're creating a template for. The playbook will take care of creating the virtual machine,
installing the OS per the bootstrap file specification in the bootstrap ISO, configuring the
machine hardware, and converting it into a template.

> :warning: **When creating a Windows template, the bootable Windows installation disc requires
a key to be pressed during the boot process in order to boot into the disc. For this reason,
the Windows template creation will**
