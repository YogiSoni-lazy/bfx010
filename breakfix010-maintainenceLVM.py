#
# Copyright (c) 2020 Red Hat Training <training@redhat.com>
#
# All rights reserved.
# No warranty, explicit or implied, provided.

from labs.common import userinterface
from labs.grading import Default


class Breakfix010Maintainencelvm(Default):
    __LAB__ = "breakfix010-maintainenceLVM"

    def start(self):
        items = []
        userinterface.Console(items).run_items(action="Starting")

    def grade(self):
        items = []
        ui = userinterface.Console(items)
        ui.run_items(action="Grading")
        ui.report_grade()

    def finish(self):
        items = []
        userinterface.Console(items).run_items(action="Finishing")
