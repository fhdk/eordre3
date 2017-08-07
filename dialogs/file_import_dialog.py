#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Frede Hundewadt <f@hundewadt.dk>
# Copyright: Frede Hundewadt <fh@uex.dk>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import os

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from configuration import config
from models import contact, customer, visit, visit_detail, report
from resources import file_import_dialog_rc


class Communication(QObject):
    """
    Broadcast signals
    """
    customersdone = pyqtSignal()


class FileImportDialog(QDialog, file_import_dialog_rc.Ui_FileImportDialog):
    """
    Dialog for importing CSV data
    """
    def __init__(self, contact, customer, employee, report, visit, visitdetail, tables, parent=None):
        """Initialize Dialog"""
        super(FileImportDialog, self).__init__(parent)
        self.setupUi(self)

        self.c = Communication()

        self.file_dialog = QFileDialog()  # Create FileDialog object
        self.employeeid = employee.employee["employeeid"]

        self.buttonImport.enabled = False
        # connect to signals
        self.comboImport.currentIndexChanged.connect(self.combo_current_index_changed_action)
        self.buttonBrowse.clicked.connect(self.button_browse_action)
        self.buttonImport.clicked.connect(self.button_import_action)
        self.buttonClose.clicked.connect(self.button_close_action)
        # Setup which tables can be imported
        for table_item in tables:
            self.comboImport.addItem(table_item[0], table_item[1])
            self.comboImport.setCurrentIndex(0)
        self.browseDir = config.HOME  # setup file import dir to home
        self.selectedFile = ""  # initalize selected file
        self.selectedTable = self.comboImport.itemData(0)  # initialize selected table
        # initialize objects
        self.contact = contact  # main contact object
        self.customer = customer  # main customer object
        self.visit = visit  # main visit object
        self.visitdetail = visitdetail  # main visit details object
        self.report = report  # main report object

    def button_browse_action(self):
        """Slot for buttonBrowse clicked signal"""
        # browse for import file
        data = self.file_dialog.getOpenFileName(self,
                                                "Vælg import fil",
                                                self.browseDir,
                                                "Text files (*.csv)")
        self.selectedFile = data[0]
        self.browseDir = os.path.dirname(data[0])
        self.txtSelectedFile.setText(self.selectedFile)

    def button_close_action(self):
        """Slot for buttonClose clicked signal"""
        self.done(False)

    def button_import_action(self):
        """Slot for buttonImport clicked signal"""
        # we dont want buttons to be activated twice during import
        self.buttonImport.enabled = False
        self.buttonBrowse.enabled = False
        self.buttonClose.enabled = False

        if self.selectedFile:
            # notice to create to list box
            notice = self.comboImport.currentText() + " er importeret."
            success = False
            # import selected file to contact table
            if self.selectedTable == "contact":
                success = self.contact.import_csv(self.selectedFile,
                                                  self.checkHeaders.isChecked())

            # import selected file to customer table
            if self.selectedTable == "customer":
                success = self.customer.import_csv(self.selectedFile,
                                                   self.checkHeaders.isChecked())

            # import selected file to ordervisit table
            if self.selectedTable == "visit":
                success = self.visit.import_csv(self.selectedFile,
                                                self.checkHeaders.isChecked())

            # import selected file to orderline table
            if self.selectedTable == "orderline":
                success = self.OrderLine.import_csv(self.selectedFile,
                                                    self.checkHeaders.isChecked())

            # import selected file to reportid table
            if self.selectedTable == "report":
                success = self.report.import_csv(self.selectedFile,
                                                 self.employeeid,
                                                 self.checkHeaders.isChecked())

            if success:
                self.listImported.addItem(notice)
            else:
                QMessageBox.information(self, "Doh!", "Der er opstået en fejl!", QMessageBox.Ok)
                return

            self.selectedFile = ""
            self.txtSelectedFile.clear()
            self.comboImport.removeItem(self.comboImport.currentIndex())
            self.comboImport.setCurrentIndex(0)

        self.buttonImport.enabled = False  # disable the button till next file is selected
        self.buttonBrowse.enabled = True  # enable browse button
        self.buttonClose.enabled = True  # enable close button

    def combo_current_index_changed_action(self):
        """Slot for ComboBox currentIndexChanged signal"""
        self.selectedTable = self.comboImport.itemData(self.comboImport.currentIndex())
