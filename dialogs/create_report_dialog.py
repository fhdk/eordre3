#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Frede Hundewadt <f@hundewadt.dk>
# Copyright: Frede Hundewadt <fh@uex.dk>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""Order dialog"""
import datetime

from PyQt5.QtWidgets import QDialog, QMessageBox

from resources.create_report_dialog_rc import Ui_CreateReportDialog


class CreateReportDialog(QDialog, Ui_CreateReportDialog):
    def __init__(self, workdate, parent=None):
        """Initialize Dialog"""
        super(CreateReportDialog, self).__init__(parent)
        self.setupUi(self)
        self.workdate = workdate  # assign date
        self.lineEdit.setText(workdate)  # set workdate in lineedit
        # connect to signals
        self.buttonBox.accepted.connect(self.buttonbox_accepted_action)
        self.buttonBox.rejected.connect(self.buttonbox_rejected_action)

    def buttonbox_accepted_action(self):
        """Slot for buttonbox accepted signal"""
        try:
            # validate if it is ISO format
            datetime.datetime.strptime(self.lineEdit.text(), '%Y-%m-%d')
            self.workdate = self.lineEdit.text()
            self.done(True)
        except ValueError:
            msgbox = QMessageBox
            msgbox.warning(self,
                           "Eordre",
                           "Forkert format, skal være <strong>ÅÅÅÅ-MM-DD</strong>!",
                           QMessageBox.Ok)
            return False

    def buttonbox_rejected_action(self):
        """Slot for buttonbox rejected signal"""
        self.done(False)
