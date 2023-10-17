#
# Copyright (c) 2020 Red Hat Training <training@redhat.com>
#
# All rights reserved.
# No warranty, explicit or implied, provided.

from labs import labconfig
from labs.grading import Default
from labs.common import steps, labtools, userinterface

SKU = labconfig.get_course_sku().upper()

_targets = ["servera"]
_servera = "servera"

class Breakfix010Maintainencelvm(Default):
    __LAB__ = "breakfix010-maintainenceLVM"

    def start(self):
        items = [
            {
                "label": "Checking lab systems",
                "task": labtools.check_host_reachable,
                "hosts": _targets,
                "fatal": True,
            },
            steps.run_command(
                label="Configuring " + _servera,
                hosts=[_servera],
                command='''
                pvcreate /dev/vdb;
                vgcreate vg01 /dev/vdb;
                lvcreate -L 800M -n lv01 vg01;
                mkfs.xfs /dev/vg01/lv01;
                mkdir /mnt/data;
                mount /dev/vg01/lv01 /mnt/data;
                echo '/dev/vg01/lv01 /mnt/data xfs defaults 0 0' | sudo  tee -a /etc/fstab;
                (echo o # Create a new empty DOS partition table
                echo n # Add a new partition
                echo p # Primary partition
                echo 1 # Partition number
                echo   # First sector (Accept default: 1)
                echo   # Last sector (Accept default: varies)
                echo w # Write changes
                ) | sudo fdisk /dev/vdb
                ''',
                shell=True,
            ),
        ]
        userinterface.Console(items).run_items(action="Starting")

    def grade(self):
        items = []
        ui = userinterface.Console(items)
        ui.run_items(action="Grading")
        ui.report_grade()

    def finish(self):
        items = [
            {
                "label": "Checking lab systems",
                "task": labtools.check_host_reachable,
                "hosts": _targets,
                "fatal": True,
            },
            steps.run_command(
                label="Removing the settings from " + _servera,
                hosts=[_servera],
                command='''
                umount /mnt/data;
                rm -rf /mnt/data;
                lvremove /dev/vg01/lv01;
                vgremove vg01;
                pvremove /dev/vdb1;
                egrep -v -e '/dev/vg01/lv01 /mnt/data xfs defaults 0 0' /etc/fstab > /tmp/fstab && mv -f /tmp/fstab /etc/fstab;
                # fix;
                # mount -o remount,rw /;
                # parted /dev/vdb rm 1;
                # partprobe;
                # pvscan --cache;
                # vgchange -ay;
                # mount -a;
                ''',
                shell=True,
            ),
        ]
        userinterface.Console(items).run_items(action="Finishing")
