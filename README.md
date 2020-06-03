# VMC Lab Environment
A collection of scripts and Ansible playbooks required to provision a VMC lab environment.

## Create a bootstrap ISO
For creating both Windows and Linux templates, a response file is needed to provide answers to all
installation parameters that would normally be specified during a manual install. For Windows, that
takes the form of an autounattend.xml answer file, and for Linux that would be the anaconda-ks.cfg
kickstart file. Those files are included in the bootstrap directory of this repository. There are
two options for including these bootstrap files during installation:

(i) Modifying the installer ISO to include the bootstrap file
(ii) Creating a separate ISO with the bootstrap file and mounting it as a second disc

Option (i) allows us to make other useful customizations to the installer ISO that will make the
installation process even more automation-friendly, and that is the approach assumed in the
template creation playbooks. Preparing these modified ISOs would be most convenient on a Linux
machine that has a browser that can upload the ISOs back into the vSphere console. The
remaster script can be run from the bootstrap directory as follows:

> Windows:
`mkisofs -l -o /tmp/bootstrap.iso ./bootstrap/`
> Linux:
`mkisofs -l -o /tmp/bootstrap.iso ./bootstrap/`
