#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Frede Hundewadt <f@hundewadt.dk>
# Copyright: Frede Hundewadt <fh@uex.dk>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Visit Dialog Module
"""
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from models.detail import Detail
from resources.visit_dialog_rc import Ui_visitDialog


class VisitDialog(QDialog, Ui_visitDialog):
    """
    Dialog for creating a new current
    """

    def __init__(self, customers, employees, products, reports, visits, parent=None):
        """
        Initialize
        Args:
            customers: main current object
            employees: main current object
            products: main products object
            reports: main current object
            visits: main current object
            parent:
        """
        super(VisitDialog, self).__init__(parent)
        self.setupUi(self)
        self.customerid = customers.active["customer_id"]
        self.employeeid = employees.active["employee_id"]
        self.reportid = reports.active["report_id"]
        self.workdate = reports.active["repdate"]
        self.products = products.product_list
        self.txtVisitDate.setText(self.workdate)
        if customers.active["account"] == "NY":
            self.visitType = "N"
        else:
            self.visitType = "R"

        self.visits = visits
        self.visits.add(self.reportid, self.employeeid, self.customerid, self.workdate)
        self.visits.active["visit_type"] = self.visitType

        self.details = Detail()
        self.details.load(self.visits.active["visit_id"])
        # for idx, detail in enumerate(self.details.details):
        self.widgetVisit.setRowCount(10)
        self.widgetVisit.setColumnCount(len(self.details.model["fields"]))
        for i in range(10):
            item = QTableWidgetItem("item {}".format(i + 1))
            self.widgetVisit.setSortingEnabled(False)
            self.widgetVisit.setItem(i, 1, item)

        # If customer needs special settings on prices
        factor = customers.active["factor"]
        if factor > 0.0:
            for item in self.products:
                item["price"] = item["price"] * factor
                if not item["d2"] == 0.0:
                    item["d2"] = item["d2"] * factor
                if not item["d3"] == 0.0:
                    item["d3"] = item["d3"] * factor
                if not item["d4"] == 0.0:
                    item["d4"] = item["d4"] * factor
                if not item["d6"] == 0.0:
                    item["d6"] = item["d6"] * factor
                if not item["d8"] == 0.0:
                    item["d8"] = item["d8"] * factor
                if not item["d12"] == 0.0:
                    item["d12"] = item["d12"] * factor
                if not item["d24"] == 0.0:
                    item["d24"] = item["d24"] * factor
                if not item["d2"] == 0.0:
                    item["d48"] = item["d48"] * factor
                if not item["d96"] == 0.0:
                    item["d96"] = item["d96"] * factor
                if not item["min"] == 0.0:
                    item["min"] = item["min"] * factor
                if not item["net"] == 0.0:
                    item["net"] = item["net"] * factor
        # Set info banner
        self.txtCompany.setText(customers.active["company"])
        # connect to signals
        self.btnInsertDemo.clicked.connect(self.button_add_demo_action)
        self.btnInsertSale.clicked.connect(self.button_add_sale_action)
        self.btnArchiveVisit.clicked.connect(self.button_save_visit_action)

    def button_add_demo_action(self):
        """Slot for Add Demo button clicked"""

        pass

    def button_add_sale_action(self):
        """Slot for Add Sale button clicked"""
        pass

    def button_save_visit_action(self):
        """
        Slot for saving the visit
        """
        self.visits.active["po_buyer"] = self.txtPoBuyer.text()
        self.visits.active["po_number"] = self.txtPoNumber.text()
        self.visits.active["po_company"] = self.txtPoCompany.text()
        self.visits.active["po_address1"] = self.txtPoAddress1.text()
        self.visits.active["po_address2"] = self.txtPoAddress2.text()
        self.visits.active["po_postcode"] = self.txtPoPostcode.text()
        self.visits.active["po_postofffice"] = self.txtPoPostoffice.text()
        self.visits.active["po_country"] = self.txtPoCountry.text()
        self.visits.active["info_text"] = self.txtInfoText.toPlainText()
        self.visits.active["prod_demo"] = self.txtProductDemo.text()
        self.visits.active["prod_sale"] = self.txtProductSale.text()
        self.visits.active["sas"] = self.txtVisitSas.text()
        self.visits.active["sale"] = self.txtVisitSale.text()
        self.visits.active["total"] = self.txtVisitTotal.text()