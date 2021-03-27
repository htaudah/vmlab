#!/bin/sh
# A shell script to prepare the bootstrap ISOs allowing for unattended OS installations.
# Written by: Hani Audah <ht.aramco@gmail.com>
# Last updated on: Mar/27/2021
# -------------------------------------------------------------------------------------------------
mkdir /tmp/bootstraps
mkisofs -l -relaxed-filenames -V OEMDRV -o /tmp/bootstraps/bootstrap_centos.iso ./bootstrap/centos
mkisofs -l -relaxed-filenames -V OEMDRV -o /tmp/bootstraps/bootstrap_win_10.iso ./bootstrap/win_10
mkisofs -l -relaxed-filenames -V OEMDRV -o /tmp/bootstraps/bootstrap_win_2019.iso ./bootstrap/win_2019
