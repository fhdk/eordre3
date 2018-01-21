#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Frede Hundewadt <echo "ZmhAdWV4LmRrCg==" | base64 -d>
# Copyright: Frede Hundewadt <echo "ZmhAdWV4LmRrCg==" | base64 -d>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Eordre application module
"""

import datetime
import sys

from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSplashScreen, \
    QTreeWidgetItem, QTableWidgetItem

from configuration import config, configfn
from dialogs.csv_import_dialog import CsvFileImportDialog
from dialogs.get_customers_dialog import GetCustomersDialog
from dialogs.get_pricelist_dialog import GetPricelistDialog
from dialogs.create_report_dialog import ReportDialogCreate
from models.contact import Contact
from models.customer import Customer
from models.orderline import OrderLine
from models.employee import Employee
from models.product import Product
from models.report import Report
from models.settings import Settings
from models.visit import Visit
from resources.main_window_rc import Ui_mainWindow
from resources import splash_rc
<<<<<<< HEAD
from util import utils, printFn as p
=======
from util import utils
from util import passwdFn
from util import printFn
>>>>>>> version-0.4.1
from util.rules import check_settings

__appname__ = "Eordre NG"
__module__ = "main.py"

PAGE_CUSTOMERS = 0
PAGE_CUSTOMER = 1
PAGE_CUSTOMER_VISITS = 2
PAGE_PRICELIST = 3
PAGE_REPORT = 4
PAGE_REPORTS = 5
PAGE_SETTINGS = 6
PAGE_INFO = 7
PAGE_VISIT = 8


class MainWindow(QMainWindow, Ui_mainWindow):
    """
    Main Application Window
    """

    def __init__(self, parent=None):
        """
        Initialize MainWindow class
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        thread = QThread()
        thread.currentThread().setObjectName(__appname__)
        configfn.check_config_folder()  # Check appdata folder in users home

        self.textWorkdate.setText(datetime.date.today().isoformat())  # initialize workdate to current date

        self._archivedOrderlines = OrderLine()  # Initialize Detail object
        self._archivedVisits = Visit()  # Initialize Visit object
        self._contacts = Contact()  # Initialize Contact object
        self._customers = Customer()  # Initialize Customer object
        self._employees = Employee()  # Initialize Employee object
        self._orderLines = OrderLine()
        self._products = Product()  # Initialize Product object
        self._reports = Report()  # Initialize Report object
        self._settings = Settings()  # Initialize Settings object
        self._visits = Visit()

        self.buttonArchiveContacts.clicked.connect(self.archive_contacts)
        self.buttonArchiveCustomer.clicked.connect(self.archive_customer)
        self.buttonArchiveVisit.clicked.connect(self.archive_visit)

        self.buttonCreateContact.clicked.connect(self.create_contact)
        self.buttonCreateCustomer.clicked.connect(self.create_customer)
        self.buttonCreateReport.clicked.connect(self.create_report)
        self.buttonCreateVisit.clicked.connect(self.load_visit)

        self.buttonGetCustomers.clicked.connect(self.get_customers)
        self.buttonGetPricelist.clicked.connect(self.get_pricelist)

        self.toolButtonArchiveSettings.clicked.connect(self.archive_settings)
        self.toolButtonCustomer.clicked.connect(self.show_page_customer)
        self.toolButtonCustomers.clicked.connect(self.show_page_customers)
        self.toolButtonCustomerVisits.clicked.connect(self.show_page_customer_visits)
        self.toolButtonExit.clicked.connect(self.app_exit)
        self.toolButtonInfo.clicked.connect(self.show_page_info)
        self.toolButtonPricelist.clicked.connect(self.show_page_pricelist)
        self.toolButtonReport.clicked.connect(self.show_page_report)
        self.toolButtonReports.clicked.connect(self.show_page_reports)
        self.toolButtonSettings.clicked.connect(self.show_page_settings)
        self.toolButtonCustomerVisit.clicked.connect(self.show_page_visit)

        self.toolButtonDeleteSalesData.clicked.connect(self.zero_database)
        self.toolButtonExportDatabase.clicked.connect(self.data_export)
        self.toolButtonImportCsvData.clicked.connect(self.show_csv_import_dialog)
        self.toolButtonImportDatabase.clicked.connect(self.data_import)

        self.widgetAppCustomers.currentItemChanged.connect(self.on_customer_changed)
        self.widgetAppCustomers.itemDoubleClicked.connect(self.on_customer_double_clicked)

        self.widgetArchivedVisits.currentItemChanged.connect(self.on_visit_changed)
        self.widgetArchivedVisits.setColumnHidden(0, True)

        self.widgetArchivedOrderLines.setColumnWidth(0, 30)
        self.widgetArchivedOrderLines.setColumnWidth(1, 30)
        self.widgetArchivedOrderLines.setColumnWidth(2, 100)
        self.widgetArchivedOrderLines.setColumnWidth(3, 150)
        self.widgetArchivedOrderLines.setColumnWidth(4, 60)
        self.widgetArchivedOrderLines.setColumnWidth(5, 40)

        self._reports.load_report(self.textWorkdate.text())

<<<<<<< HEAD
        # connect menu trigger signals
        self.actionAboutQt.triggered.connect(self.show_about_qt)
        self.actionAboutSoftware.triggered.connect(self.show_about_software)
        self.actionArchiveChanges.triggered.connect(self.archive_customer)
        self.actionContactsInfo.triggered.connect(self.show_contact_data_page)
        self.actionCreateCustomer.triggered.connect(self.create_customer)
        self.actionCreateVisit.triggered.connect(self.show_visit_dialog)
        self.actionImportCsvFiles.triggered.connect(self.show_csv_import_dialog)
        self.actionExit.triggered.connect(self.app_exit_slot)
        self.actionGetCatalogHttp.triggered.connect(self.show_http_products_dialog)
        self.actionGetCustomersHttp.triggered.connect(self.show_http_customers_dialog)
        self.actionMasterInfo.triggered.connect(self.show_master_data_page)
        self.actionReport.triggered.connect(self.show_create_report_dialog)
        self.actionReportList.triggered.connect(self.show_reports_dialog)
        self.actionSettings.triggered.connect(self.show_settings_dialog)
        self.actionVisitsInfo.triggered.connect(self.show_visit_data_page)
        self.actionZeroDatabase.triggered.connect(self.zero_database)
        # buttons on top
        self.btnAddCustomer.clicked.connect(self.create_customer)
        self.btnCreateReportDialog.clicked.connect(self.show_create_report_dialog)
        # buttons for paging data
        self.btnShowContacts.clicked.connect(self.show_contact_data_page)
        self.btnShowMasterdata.clicked.connect(self.show_master_data_page)
        self.btnShowVisits.clicked.connect(self.show_visit_data_page)
        # button on master data page
        self.btnArchiveMasterdata.clicked.connect(self.archive_customer)
        # buttons on contacts data page
        self.btnArchiveContacts.clicked.connect(self.archive_contacts_slot)
        self.btnAddContact.clicked.connect(self.add_contact_slot)
        # button visit data page
        self.btnVisitDialog.clicked.connect(self.show_visit_dialog)
        # connect list changes
        self.widgetCustomerList.currentItemChanged.connect(self.on_customer_changed)
        self.widgetVisitList.currentItemChanged.connect(self.on_visit_changed)
        # Hide the id column on visit list
        self.widgetVisitList.setColumnHidden(0, True)
        # Set header on visit details
        self.widgetVisitDetails.setColumnWidth(0, 30)
        self.widgetVisitDetails.setColumnWidth(1, 30)
        self.widgetVisitDetails.setColumnWidth(2, 100)
        self.widgetVisitDetails.setColumnWidth(3, 150)
        self.widgetVisitDetails.setColumnWidth(4, 60)
        self.widgetVisitDetails.setColumnWidth(5, 40)
        # load report for workdate if exist
        self._reports.get_(workdate=self.txtWorkdate.text())
        # display customerlist
        self.populate_customer_list()
        # set latest customer active
        if self._customers.lookup_by_id(self._settings.setting["cust_idx"]):
            try:
                phone = self._customers.customer["phone1"]
                self.widgetCustomerList.setCurrentIndex(
                    self.widgetCustomerList.indexFromItem(
                        self.widgetCustomerList.findItems(phone, Qt.MatchExactly, column=0)[0]))
            except KeyError:
                pass
        # set last info page used
        if self._settings.setting["page_idx"]:
            self.widgetCustomerInfo.setCurrentIndex(self._settings.setting["page_idx"])
=======
        self.populate_customer_list()

        if self._customers.lookup_by_id(self._settings.setting["cust_idx"]):
            try:
                phone = self._customers.customer["phone1"]
                self.widgetAppCustomers.setCurrentIndex(
                    self.widgetAppCustomers.indexFromItem(
                        self.widgetAppCustomers.findItems(phone, Qt.MatchExactly, column=1)[0]))
                self.toolButtonCustomer.click()
                return
            except KeyError:
                pass

        self.toolButtonCustomers.click()
>>>>>>> version-0.4.1

    def closeEvent(self, event):
        """
        Slot for close event signal
        Args:
            event:

        intended use is warning about unsaved data
        """
        # TODO handle close event
        self.app_exit()

    def display_sync_status(self):
        """
        Update status fields
        """
        self.textCustomerLocalDate.setText(self._settings.setting["lsc"])
        self.textCustomerServerDate.setText(self._settings.setting["sac"])
        self.textPricelistLocalDate.setText(self._settings.setting["lsp"])
        self.textPricelistServerDate.setText(self._settings.setting["sap"])

    def populate_archived_visit_details(self):
        """
        Populate the details list based on the line visit
        """
        self.widgetArchivedOrderLines.clear()

        self.labelArchivedApprovedText.setText("")
        self.labelArchivedSendText.setText("")
        self.textArchivedOrderPoNumber.setText("")
        self.textArchivedOrderSale.setText("")
        self.textArchivedOrderSas.setText("")
        self.textArchivedOrderTotal.setText("")
        self.textArchivedVisitNote.setText("")

        items = []
        try:
<<<<<<< HEAD
            self._settings.setting["cust_idx"] = self._customers.customer["customer_id"]
        except KeyError:
            self._settings.setting["cust_idx"] = 0
        # customer info page
        if not self._settings.setting["page_idx"]:
            self._settings.setting["page_idx"] = self.widgetCustomerInfo.currentIndex()
        # save setttings
        self._settings.update()
        app.quit()
=======
            self.labelArchivedSendText.setText(
                utils.bool2dk(utils.int2bool(
                    self._archivedVisits.visit["po_sent"])))
            self.labelArchivedApprovedText.setText(
                utils.bool2dk(utils.int2bool(
                    self._archivedVisits.visit["po_approved"])))
            self.textArchivedOrderPoNumber.setText(
                self._archivedVisits.visit["po_number"])
            self.textArchivedOrderSale.setText(
                str(self._archivedVisits.visit["po_sale"]))
            self.textArchivedOrderSas.setText(
                str(self._archivedVisits.visit["po_sas"]))
            self.textArchivedOrderTotal.setText(
                str(self._archivedVisits.visit["po_total"]))
            self.textArchivedVisitNote.setText(
                self._archivedVisits.visit["visit_note"])

            self._archivedOrderlines.list_ = self._archivedVisits.visit["visit_id"]
            for line in self._archivedOrderlines.list_:
                item = QTreeWidgetItem([line["linetype"],
                                        str(line["pcs"]),
                                        line["sku"],
                                        line["text"],
                                        str(line["price"]),
                                        str(line["discount"]),
                                        line["linenote"]])
                items.append(item)
        except KeyError:
            pass
        except IndexError:
            pass
>>>>>>> version-0.4.1

        self.widgetArchivedOrderLines.addTopLevelItems(items)

    def populate_archived_visits(self):
        """
        Populate the visitlist based on the active customer
        """
<<<<<<< HEAD
        self.txtCustLocal.setText(self._settings.setting["lsc"])
        self.txtCustServer.setText(self._settings.setting["sac"])
        self.txtProdLocal.setText(self._settings.setting["lsp"])
        self.txtProdServer.setText(self._settings.setting["sap"])
=======
        self.widgetArchivedVisits.clear()
        self.widgetArchivedVisits.setHeaderLabels(["Id", "Dato", "Navn", "Demo", "Salg", "Ordre note"])
        self.widgetArchivedVisits.setColumnWidth(0, 0)
        items = []
        try:
            self._archivedVisits.list_customer = self._customers.customer["customer_id"]

            for visit in self._archivedVisits.list_customer:
                item = QTreeWidgetItem([str(visit["visit_id"]),
                                        visit["visit_date"],
                                        visit["po_buyer"],
                                        visit["prod_demo"],
                                        visit["prod_sale"],
                                        visit["po_note"]])
                items.append(item)
                if visit["visit_date"] == self.textWorkdate.text():
                    self.toolButtonCustomerVisit.setEnabled(True)

        except IndexError:
            pass
        except KeyError:
            pass
        self.widgetArchivedVisits.addTopLevelItems(items)
>>>>>>> version-0.4.1

    def populate_contact_list(self):
        """
        Populate the contactlist based on currently selected customer
        """
        # load contacts
        self.widgetCustomerContacts.clear()
        items = []
        try:
            self._contacts.list_ = self._customers.customer["customer_id"]
            for c in self._contacts.list_:
                item = QTreeWidgetItem([c["name"],
                                        c["department"],
                                        c["phone"],
                                        c["email"]])
                items.append(item)
        except IndexError:
            pass
        except KeyError:
            pass

        self.widgetCustomerContacts.addTopLevelItems(items)

    def populate_customer_list(self):
        """
        Populate customer list
        """

        self.widgetAppCustomers.clear()  # shake the tree for leaves
        self.widgetAppCustomers.setColumnCount(6)  # set columns
        self.widgetAppCustomers.setHeaderLabels(["Konto", "Telefon", "Telefon", "Firma", "Post", "Bynavn"])
        items = []  # temporary list
        try:
            for c in self._customers.list_:
<<<<<<< HEAD
                item = QTreeWidgetItem([c["phone1"],
                                        c["company"]])
=======
                item = QTreeWidgetItem([c["account"], c["phone1"], c["phone2"], c["company"], c["zipcode"], c["city"]])
>>>>>>> version-0.4.1
                items.append(item)
        except (IndexError, KeyError):
            pass
        # assign Widgets to Tree
<<<<<<< HEAD
        self.widgetCustomerList.addTopLevelItems(items)
        self.widgetCustomerList.setSortingEnabled(True)  # enable sorting

    def populate_visit_orderlines_list(self):
        """
        Populate the details list based on the line visit
        """
        self.widgetVisitDetails.clear()
        self.txtPoNumber.setText("")
        self.txtSas.setText("")
        self.txtSale.setText("")
        self.txtTotal.setText("")
        self.lblApproved.setText("")
        self.lblSent.setText("")
        self.txtVisitInfoText.setText("")

        items = []
        try:
            self._orderlines.lines = self._visits.active["visit_id"]

            self.txtPoNumber.setText(self._visits.active["po_number"])
            self.txtSas.setText(str(self._visits.active["po_sas"]))
            self.txtSale.setText(str(self._visits.active["po_sale"]))
            self.txtTotal.setText(str(self._visits.active["po_total"]))
            self.lblSent.setText(utils.bool2dk(utils.int2bool(self._visits.active["po_sent"])))
            self.lblApproved.setText(utils.bool2dk(utils.int2bool(self._visits.active["po_approved"])))
            self.txtVisitInfoText.setText(self._visits.active["po_note"])

            for detail in self._orderlines.lines:
                item = QTreeWidgetItem([detail["linetype"],
                                        str(detail["pcs"]),
                                        detail["sku"],
                                        detail["text"],
                                        str(detail["price"]),
                                        str(detail["discount"]),
                                        detail["extra"]])
                items.append(item)
        except KeyError:
            pass
        except IndexError:
            pass
        self.widgetVisitDetails.addTopLevelItems(items)

    def populate_visit_list(self):
        """
        Populate the visitlist based on the active customer
        """
        # populate visit list table
        self.widgetVisitList.clear()
        # self.widgetVisitList.setColumnCount(5)
        self.widgetVisitList.setHeaderLabels(["Id", "Dato", "Navn", "Demo", "Salg"])
        self.widgetVisitList.setColumnWidth(0, 0)
        items = []
        try:
            self._visits.visit_list_customer = self._customers.customer["customer_id"]
            for visit in self._visits.visit_list_customer:
                item = QTreeWidgetItem([str(visit["visit_id"]),
                                        visit["visit_date"],
                                        visit["po_buyer"],
                                        visit["prod_demo"],
                                        visit["prod_sale"]])
                items.append(item)
        except IndexError:
            pass
        except KeyError:
            pass
        self.widgetVisitList.addTopLevelItems(items)
=======
        self.widgetAppCustomers.addTopLevelItems(items)
        self.widgetAppCustomers.setSortingEnabled(True)  # enable sorting

    # def populate_visit_list(self):
    #     """
    #     Populate
    #     """
    #     # populate visit list table
    #     self.widgetArchivedVisits.setHeaderLabels(["Id", "Dato", "Navn", "Demo", "Salg"])
    #     self.widgetArchivedVisits.setColumnWidth(0, 0)
    #     items = []
    #     try:
    #         self._archivedVisits.list_customer = self._customers.customer["customer_id"]
    #         for visit in self._archivedVisits.list_customer:
    #             item = QTreeWidgetItem([str(visit["visit_id"]),
    #                                     visit["visit_date"],
    #                                     visit["po_buyer"],
    #                                     visit["prod_demo"],
    #                                     visit["prod_sale"]])
    #             items.append(item)
    #             if visit["visit_date"] == self.textWorkdate.text():
    #                 self.load_visit()
    #
    #     except IndexError:
    #         pass
    #     except KeyError:
    #         pass
    #     self.widgetArchivedVisits.addTopLevelItems(items)

    def populate_settings_page(self):
        """
        Populate settings page
        :return: 
        """
        self.textAppUserMail.setText(self._settings.setting["usermail"])
        self.textAppUserPass.setText(self._settings.setting["userpass"])
        self.textAppUserCountry.setText(self._settings.setting["usercountry"])
        self.textAppDataServer.setText(self._settings.setting["http"])
        self.textAppMailServer.setText(self._settings.setting["smtp"])
        self.textAppMailServerPort.setText(str(self._settings.setting["port"]))
        self.textAppMailOrderTo.setText(self._settings.setting["mailto"])
        self.checkServerData.setChecked(utils.int2bool(self._settings.setting["sc"]))
        self.textExtMailServer.setText(self._settings.setting["mailserver"])
        self.textExtMailServerPort.setText(str(self._settings.setting["mailport"]))
        self.textExtMailServerUser.setText(self._settings.setting["mailuser"])
        self.textExtMailServerPass.setText(self._settings.setting["mailpass"])
>>>>>>> version-0.4.1

    def resizeEvent(self, event):
        """
        Slot for the resize event signal
        Args:
            event:
        intended use is resize content to window
        :param event:
        """
        # TODO handle resize event
        pass

    def run(self):
        """
        Setup database and basic configuration
        """
        # basic settings must be done
        is_set = check_settings(self._settings.setting)
        if is_set:
            try:
                _ = self._employees.employee["fullname"]
            except KeyError:
                msgbox = QMessageBox()
                msgbox.about(self,
                             __appname__,
                             "Der er en fejl i dine indstillinger.\nKontroller dem venligst.\nTak.")
        else:
            msgbox = QMessageBox()
            msgbox.about(self,
                         __appname__,
                         "App'en skal bruge nogle oplysninger.\nRing kontoret hvis du er i tvivl.\nTak.")

            self.show_page_settings()

        # if requested check server data
        if utils.int2bool(self._settings.setting["sc"]):
            # update sync status
            status = utils.refresh_sync_status(self._settings)
            self._settings.setting["sac"] = status[0][1].split()[0]
            self._settings.setting["sap"] = status[1][1].split()[0]
            self._settings.update()

        # display known sync data
        self.display_sync_status()

    def set_indexes(self, button: str):
        """
        Save page index to settings
        :param button:
        :return:
        """
        # customer id
        try:
            self._settings.setting["cust_idx"] = self._customers.customer["customer_id"]
        except KeyError:
            self._settings.setting["cust_idx"] = 0
        if not self._settings.setting["page_idx"]:
            self._settings.setting["page_idx"] = self.widgetAppPages.currentIndex()
        self._settings.setting["toolbutton"] = button
        self._settings.update()

    def set_input_enabled(self, arg: bool):
        """Enable inputs"""
        self.checkVisitSas.setEnabled(arg)
        self.comboOrderItem.setEnabled(arg)
        self.comboOrderSku.setEnabled(arg)
        self.textVisitPcs.setEnabled(arg)
        self.textVisitLinePrice.setEnabled(arg)
        self.textVisitLineDiscount.setEnabled(arg)

    @pyqtSlot(name="app_exit")
    def app_exit(self):
        """
        Exit - save current customer
        """
        # customer id
        try:
            self._settings.setting["cust_idx"] = self._customers.customer["customer_id"]
        except KeyError:
            self._settings.setting["cust_idx"] = 0
        self._settings.update()
        app.quit()

    @pyqtSlot(name="archive_contacts")
    def archive_contacts(self):
        """
        Save changes made to contacts
        """
        # TODO save changes made to contacts
        msgbox = QMessageBox()
        msgbox.information(self,
                           __appname__,
                           "# TODO save changes made to contacts",
                           QMessageBox.Ok)

    @pyqtSlot(name="archive_customer")
    def archive_customer(self):
        """
        Slot for updateCustomer triggered signal
        """
        if not self._customers.customer:
            # msgbox triggered if no current is selected
            msgbox = QMessageBox()
            msgbox.information(self,
                               __appname__,
                               "Det kan jeg ikke på nuværende tidspunkt!",
                               QMessageBox.Ok)
            return False
        # assign input field values to current object
<<<<<<< HEAD
        self._customers.customer["company"] = self.txtCompany.text()
        self._customers.customer["address1"] = self.txtAddress1.text()
        self._customers.customer["address2"] = self.txtAddress2.text()
        self._customers.customer["zipcode"] = self.txtZipCode.text()
        self._customers.customer["city"] = self.txtCityName.text()
        self._customers.customer["phone1"] = self.txtPhone1.text()
        self._customers.customer["phone2"] = self.txtPhone2.text()
        self._customers.customer["email"] = self.txtEmail.text()
        self._customers.customer["factor"] = self.txtFactor.text()
        self._customers.customer["infotext"] = self.txtCustomerInfoText.toPlainText()
        self._customers.customer["modified"] = 1
        self._customers.update_()
=======
        self._customers.customer["company"] = self.textCompany.text()
        self._customers.customer["address1"] = self.textAddress1.text()
        self._customers.customer["address2"] = self.textAddress2.text()
        self._customers.customer["zipcode"] = self.textZipCode.text()
        self._customers.customer["city"] = self.textCityName.text()
        self._customers.customer["phone1"] = self.textPhone1.text()
        self._customers.customer["phone2"] = self.textPhone2.text()
        self._customers.customer["email"] = self.textEmail.text()
        self._customers.customer["factor"] = self.textFactor.text()
        self._customers.customer["infotext"] = self.textCustomerInfoText.toPlainText()
        self._customers.customer["modified"] = 1
        self._customers.update()
>>>>>>> version-0.4.1

    @pyqtSlot(name="archive_settings")
    def archive_settings(self):
        """
        Archive settings
        :return:
        """
        checkok = True
        items = []
        if self.textAppUserMail.text() == "":
            items.append("Gruppe 'Sælger' -> 'Email'")
            checkok = False
        if self.textAppUserPass.text() == "":
            items.append("Gruppe 'Sælger' -> 'Adgangsfrase'")
            checkok = False
        if self.textAppUserCountry.text() == "":
            items.append("Gruppe: Sælger -> landekode")
            checkok = False
        if self.textAppMailServer.text() == "":
            items.append("Gruppe: Intern -> Mailserver")
            checkok = False
        if self.textAppMailServerPort.text() == "":
            items.append("Gruppe: Intern -> Port")
            checkok = False
        if self.textAppMailOrderTo == "":
            items.append("Gruppe: Intern -> Mail til")
            checkok = False
        if self.textAppDataServer == "":
            items.append("Gruppe: Intern -> Dataserver")
            checkok = False
        # inform user about settings validity
        msgbox = QMessageBox()
        if not checkok:
            msgbox.warning(self, __appname__,
                           "Der er mangler i dine indstillinger!\n{}".format("\n".join(items)),
                           QMessageBox.Ok)
            return False
        # update password in settings
        if len(self.textAppUserPass.text()) < 97:
            self._settings.setting["userpass"] = passwdFn.hash_password(self.textAppUserPass.text())
        if len(self.textExtMailServerPass.text()) < 97:
            self._settings.setting["mailpass"] = passwdFn.hash_password(self.textExtMailServerPass.text())
        self._settings.setting["usermail"] = self.textAppUserMail.text().lower()
        self._settings.setting["usercountry"] = self.textAppUserCountry.text()
        self._settings.setting["http"] = self.textAppDataServer.text()
        self._settings.setting["smtp"] = self.textAppMailServer.text()
        self._settings.setting["port"] = self.textAppMailServerPort.text()
        self._settings.setting["mailto"] = self.textAppMailOrderTo.text()
        self._settings.setting["sc"] = utils.bool2int(self.checkServerData.isChecked())
        self._settings.setting["mailserver"] = self.textExtMailServer.text().lower()
        self._settings.setting["mailport"] = self.textExtMailServerPort.text()
        self._settings.setting["mailuser"] = self.textExtMailServerUser.text()
        self._settings.update()
        self._employees.load(self._settings.setting["usermail"])
        msgbox.information(self, __appname__, "Indstillinger opdateret.", QMessageBox.Ok)

    @pyqtSlot(name="archive_visit")
    def archive_visit(self):
        """
        Slot for saving the visit
        """
        self.toolButtonCustomerVisit.setEnabled(False)
        # save visit head contents
        self._visits.visit["po_buyer"] = self.textVisitBuyer.text()
        self._visits.visit["po_number"] = self.textVisitPoNumber.text()
        self._visits.visit["po_company"] = self.textVisitDelCompany.text()
        self._visits.visit["po_address1"] = self.textDelAddress1.text()
        self._visits.visit["po_address2"] = self.textDelAddress2.text()
        self._visits.visit["po_postcode"] = self.textVisitDelZip.text()
        self._visits.visit["po_postofffice"] = self.textVisitDelCity.text()
        self._visits.visit["po_country"] = self._employees.employee["country"]
        self._visits.visit["po_note"] = self.textVisitOrderNote.text()
        self._visits.visit["prod_demo"] = self.textVisitProductDemo.text()
        self._visits.visit["prod_sale"] = self.textVisitProductSale.text()
        self._visits.visit["po_sas"] = self.textVisitSas.text()
        self._visits.visit["po_sale"] = self.textVisitSale.text()
        self._visits.visit["po_total"] = self.textVisitTotal.text()
        self._visits.visit["visit_note"] = self.textVisitInfo.toPlainText()

        # TODO: save visitdetails

    @pyqtSlot(name="create_contact")
    def create_contact(self):
        """
        Save changes made to contacts
        """
        # TODO add new contact
        msgbox = QMessageBox()
        msgbox.information(self,
                           __appname__,
                           "# TODO add new contact",
                           QMessageBox.Ok)

    @pyqtSlot(name="create_customer")
    def create_customer(self):
        """
        Slot for createCustomer triggered signal
        """
        if not self.textNewCompany.text() or not self.textNewPhone1.text():
            msgbox = QMessageBox()
            msgbox.information(self,
                               __appname__,
                               "Snap - Jeg mangler:\n Firma navn \n Telefon nummer",
                               QMessageBox.Ok)
        else:
            msgbox = QMessageBox()
            msgbox.information(self,
                               __appname__,
                               "Gem kunde til database\n\n" +
                               self.textNewCompany.text() + "\n" +
                               self.textNewPhone1.text(),
                               QMessageBox.Ok)

    @pyqtSlot(name="create_report")
    def create_report(self):
        """
        Slot for Report triggered signal
        """
        try:
            # check the report date
            # no report triggers KeyError which in turn launches the CreateReportDialog
            repdate = self._reports.report["rep_date"]
            if not repdate == self.textWorkdate.text():
                # if active report is not the same replace it with workdate
                self._reports.load_report(self.textWorkdate.text())
                # trigger a KeyError if no report is current which launches the CreateReportDialog
                repdate = self._reports.report["rep_date"]
                # check if the report is sent
                if self._reports.report["sent"] == 1:
                    # we do not allow visits to be created on a report which is closed
                    self.buttonCreateVisit.setEnabled(False)
                else:
                    self.buttonCreateVisit.setEnabled(True)
            infotext = "Rapport aktiv for: {}".format(repdate)
            msgbox = QMessageBox()
            msgbox.information(self, __appname__, infotext, QMessageBox.Ok)
            return True

        except KeyError:
            # Show report dialog
            create_report_dialog = ReportDialogCreate(self.textWorkdate.text())
            if create_report_dialog.exec_():
                # user chosed to create a report
                self.textWorkdate.setText(create_report_dialog.workdate)
                # try load a report for that date
                self._reports.load_report(self.textWorkdate.text())
                try:
                    # did the user choose an existing report
                    _ = self._reports.report["rep_date"]
                    infotext = "Eksisterende rapport hentet: {}".format(self.textWorkdate.text())
                except KeyError:
                    # create the report
                    self._reports.create(self._employees.employee, self.textWorkdate.text())
                    infotext = "Rapport oprettet for: {}".format(self.textWorkdate.text())
                msgbox = QMessageBox()
                msgbox.information(self, __appname__, infotext, QMessageBox.Ok)
                return True
            else:
                msgbox = QMessageBox()
                msgbox.information(self,
                                   __appname__,
                                   "Den aktive rapport er <strong>IKKE</strong> ændret!",
                                   QMessageBox.Ok)
                return False

    @pyqtSlot(name="create_visit")
    def load_visit(self):
        """
        Slot for launching the visit dialog
        """
        try:
            # do we have a report
            _ = self._reports.report["rep_date"]
            active_report = True
        except KeyError:
            active_report = self.create_report()

        if active_report:
            self._reports.load_report(self.textWorkdate.text())
            try:
                # do we have a customer
                _ = self._customers.customer["company"]
            except KeyError:
                msgbox = QMessageBox()
                msgbox.information(self,
                                   __appname__,
                                   "Ingen valgt kunde! Besøg kan ikke oprettes.",
                                   QMessageBox.Ok)
                return

        if self.textCustId.text() is not "" and \
                self.textCustId.text() is not self._customers.customer["customer_id"]:
            confirm = QMessageBox()
            val = confirm.question(self, __appname__,
                                   "Du har en uafsluttet sag på {}.<br/>Vil du slette den?".format(
                                       self.textVisitCompany.text()),
                                   confirm.Yes | confirm.No)
            if val == confirm.No:
                self._customers.lookup_by_id(self.textCustId.text())
            else:
                self._archivedVisits.delete(self.textVisitId.text())

        self.toolButtonCustomerVisit.setEnabled(True)
        self.widgetAppPages.setCurrentIndex(PAGE_VISIT)

        customer_pricelist = self._products
        workdate = self.textWorkdate.text()
        customerid = self._customers.customer["customer_id"]
        reportid = self._reports.report["report_id"]
        employeeid = self._employees.employee["employee_id"]

        self.textCustId.setText(str(customerid))
        self.textVisitDate.setText(self.textWorkdate.text())
        self.textVisitCompany.setText(self._customers.customer["company"])

        try:
            """
            load visits for workdate
            """
            self._visits.load_for_customer(customerid, workdate)
            self.textVisitId.setText(str(self._visits.visit["visit_id"]))
        except KeyError:
            self.textVisitId.setText(str(self._visits.add(reportid, employeeid, customerid, workdate)))
            self._visits.visit["visit_type"] = "R"
            if self._customers.customer["account"] == "NY":
                self._visits.visit["visit_type"] = "N"

        visit_id = self.textVisitId.text()
        self._orderLines = OrderLine()
        self._orderLines.load_visit(visit_id)

        self.widgetVisitOrderLines.setColumnWidth(0, 43)   # line_type D/N/S
        self.widgetVisitOrderLines.setColumnWidth(1, 44)   # pcs
        self.widgetVisitOrderLines.setColumnWidth(2, 44)   # item
        self.widgetVisitOrderLines.setColumnWidth(3, 123)  # sku
        self.widgetVisitOrderLines.setColumnWidth(4, 153)  # text
        self.widgetVisitOrderLines.setColumnWidth(5, 60)   # price
        self.widgetVisitOrderLines.setColumnWidth(6, 50)   # discount
        self.widgetVisitOrderLines.setColumnWidth(6, 60)   # amount
        self.widgetVisitOrderLines.setColumnWidth(7, 30)   # SAS

        lines = self._orderLines.list_
        self.widgetVisitOrderLines.setRowCount(len(lines) - 1)
        for idx, detail in enumerate(lines):
            # "line_id", "visit_id",
            # "pcs", "sku", "text", "price", "sas", "discount",
            # "linetype", "linenote", "item"
            amount = float(detail["pcs"]) * detail["price"] * detail["discount"] / 100
            row_number = idx + 1
            # self.widgetVisitOrderLines.setRowCount(row_number)
            # self.widgetVisitOrderLines.setRowHeight(row_number, 12)
            c1 = QTableWidgetItem()
            c1.setText(detail["linetype"])
            self.widgetVisitOrderLines.setItem(row_number, 0, c1)
            c2 = QTableWidgetItem()
            c2.setText(str(detail["pcs"]))
            self.widgetVisitOrderLines.setItem(row_number, 1, c2)
            c3 = QTableWidgetItem()
            c3.setText(str(detail["item"]))
            self.widgetVisitOrderLines.setItem(row_number, 2, c3)
            c4 = QTableWidgetItem()
            c4.setText(detail["sku"])
            self.widgetVisitOrderLines.setItem(row_number, 3, c4)
            c5 = QTableWidgetItem()
            c5.setText(detail["text"])
            self.widgetVisitOrderLines.setItem(row_number, 4, c5)
            c6 = QTableWidgetItem()
            c6.setText(str(detail["price"]))
            self.widgetVisitOrderLines.setItem(row_number, 5, c6)
            c7 = QTableWidgetItem()
            c6.setText(str(detail["discount"]))
            self.widgetVisitOrderLines.setItem(row_number, 6, c7)
            c8 = QTableWidgetItem()
            c8.setText(str(amount))
            self.widgetVisitOrderLines.setItem(row_number, 7, c8)
            c9 = QTableWidgetItem()
            c9.setText(utils.int2strdk(detail["sas"]))
            self.widgetVisitOrderLines.setItem(row_number, 8, c9)
            c10 = QTableWidgetItem()
            c10.setText(detail["linenote"])
            self.widgetVisitOrderLines.setItem(row_number, 9, c10)

        # Setup pricelist and selection combos
        factor = self._customers.customer["factor"]
        if not factor:
            factor = 0.0

        for item in customer_pricelist.list_:
            if factor is not 0.0:
                item["price"] = item["price"] * factor
                item["d2"] = item["d2"] * factor
                item["d3"] = item["d3"] * factor
                item["d4"] = item["d4"] * factor
                item["d6"] = item["d6"] * factor
                item["d8"] = item["d8"] * factor
                item["d12"] = item["d12"] * factor
                item["d24"] = item["d24"] * factor
                item["d48"] = item["d48"] * factor
                item["d96"] = item["d96"] * factor
                item["min"] = item["min"] * factor
                item["net"] = item["net"] * factor
            self.comboOrderItem.addItem(item["item"], [item["sku"], item["name1"], item])
            self.comboOrderSku.addItem(item["sku"], [item["item"], item["name1"], item])

        # connect to signals
        self.buttonArchiveVisit.clicked.connect(self.archive_visit)
        self.comboOrderItem.currentIndexChanged.connect(self.on_order_item_changed)
        self.comboOrderSku.currentIndexChanged.connect(self.on_order_sku_changed)
        self.comboOrderSku.editTextChanged.connect(self.on_order_sku_changed)
        self.comboVisitLineType.currentIndexChanged.connect(self.visit_line_type_changed)
        self.toolButtonVisitAppendLine.clicked.connect(self.visit_add_line)
        self.toolButtonVisitClearLine.clicked.connect(self.visit_clear_line)

    @pyqtSlot(name="data_export")
    def data_export(self):
        """
        Export Database backup file
        """
        # TODO: Opret CSV data backup
        msgbox = QMessageBox()
        msgbox.information(self,
                           __appname__,
                           "TODO: Create Database Backup File",
                           QMessageBox.Ok)

    @pyqtSlot(name="data_import")
    def data_import(self):
        """
        Import Database backup file
        """
        # TODO: Opret CSV data backup
        msgbox = QMessageBox()
        msgbox.information(self,
                           __appname__,
                           "TODO: Import Database Backup File",
                           QMessageBox.Ok)

    @pyqtSlot(name="get_customers")
    def get_customers(self):
        """
        Slot for getCustomers triggered signal
        """
        import_customers = GetCustomersDialog(app,
                                              customers=self._customers,
                                              employees=self._employees,
                                              settings=self._settings)
        import_customers.sig_done.connect(self.on_get_customers_done)
        import_customers.exec_()

    @pyqtSlot(name="get_pricelist")
    def get_pricelist(self):
        """
        Slot for getProducts triggered signal
        """
        import_product = GetPricelistDialog(app,
                                            products=self._products,
                                            settings=self._settings)
        import_product.sig_done.connect(self.on_get_products_done)
        import_product.exec_()

    @pyqtSlot(name="on_add_demo")
    def on_add_demo(self):
        """
        Add line to product demo table
        :return:
        """
        row_count = self.tableDemo.rowCount()
        self.tableDemo.setRowCount(row_count + 1)

    @pyqtSlot(name="on_add_sale")
    def on_add_sale(self):
        """
        Add line to product sale table
        :return:
        """
        row_count = self.tableSale.rowCount()
        self.tableSale.setRowCount(row_count + 1)

    @pyqtSlot(name="on_remove_demo")
    def on_remove_demo(self):
        """
        Remove line from product demo table
        :return:
        """

    @pyqtSlot(name="on_remove_sale")
    def on_remove_sale(self):
        """
        Remove line from product sale table
        :return:
        """

    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem, name="on_customer_changed")
    def on_customer_changed(self, current, previous):
        """
        Slot for treewidget current item changed signal
        Used to respond to changes in the customer list
        and update the related customer info

        Args:
            current: currently selected item
            previous: previous selected item
        """
        try:
            # account = current.text(0)
            phone = current.text(1)
            company = current.text(3)
            # move current customer
            # load customer
            self._customers.lookup(phone, company)
            # fields to line edits
<<<<<<< HEAD
            self.txtAccount.setText(self._customers.customer["account"])
            self.txtCompany.setText(self._customers.customer["company"])
            self.txtAddress1.setText(self._customers.customer["address1"])
            self.txtAddress2.setText(self._customers.customer["address2"])
            self.txtZipCode.setText(self._customers.customer["zipcode"])
            self.txtCityName.setText(self._customers.customer["city"])
            self.txtPhone1.setText(self._customers.customer["phone1"])
            self.txtPhone2.setText(self._customers.customer["phone2"])
            self.txtEmail.setText(self._customers.customer["email"])
            self.txtFactor.setText(str(self._customers.customer["factor"]))
            self.txtCustomerInfoText.setText(self._customers.customer["infotext"])
=======
            self.textAccount.setText(self._customers.customer["account"])
            self.textCompany.setText(self._customers.customer["company"])
            self.textAddress1.setText(self._customers.customer["address1"])
            self.textAddress2.setText(self._customers.customer["address2"])
            self.textZipCode.setText(self._customers.customer["zipcode"])
            self.textCityName.setText(self._customers.customer["city"])
            self.textPhone1.setText(self._customers.customer["phone1"])
            self.textPhone2.setText(self._customers.customer["phone2"])
            self.textEmail.setText(self._customers.customer["email"])
            self.textFactor.setText(str(self._customers.customer["factor"]))
            self.textCustomerInfoText.setText(self._customers.customer["infotext"])
>>>>>>> version-0.4.1
        except AttributeError:
            pass
        except KeyError:
            pass
        # load customer infos
        self.populate_contact_list()
<<<<<<< HEAD
        self.populate_visit_list()
        self.populate_visit_orderlines_list()
=======
        self.populate_archived_visits()
        self.populate_archived_visit_details()
>>>>>>> version-0.4.1

    @pyqtSlot(name="on_csv_import_done")
    def on_csv_import_done(self):
        """
        Slog for csv import done signal
        """
        self.populate_customer_list()

    @pyqtSlot(QTreeWidgetItem, name="on_customer_clicked")
    def on_customer_double_clicked(self, current):
        """
        Customer selected in
        :param current:
        :return:
        """
        self.toolButtonCustomer.click()

    @pyqtSlot(name="on_get_customers_done")
    def on_get_customers_done(self):
        """
        Slot for getCustomers finished signal
        """
        self.populate_customer_list()
        lsc = datetime.date.today().isoformat()
<<<<<<< HEAD
        self.txtCustLocal.setText(lsc)
=======
        self.textCustomerLocalDate.setText(lsc)
>>>>>>> version-0.4.1
        self._settings.setting["lsc"] = lsc
        self._settings.update()

    @pyqtSlot(name="on_get_products_done")
    def on_get_products_done(self):
        """
        Slot for getProducts finished signal
        """
        self._products.all()
        lsp = datetime.date.today().isoformat()
<<<<<<< HEAD
        self.txtProdLocal.setText(lsp)
        self._settings.setting["lsp"] = lsp
        self._settings.update()

    @pyqtSlot(name="on_settings_changed")
    def on_settings_changed(self):
        """
        load employee data
        :return:
        """
        self._settings.get()
        self._employees.load(self._settings.setting["usermail"])

=======
        self.textPricelistLocalDate.setText(lsp)
        self._settings.setting["lsp"] = lsp
        self._settings.update()

>>>>>>> version-0.4.1
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem, name="on_visit_changed")
    def on_visit_changed(self, current, previous):
        """
        Response to current visit changed
        Args:
            current:
            previous:
        """
        try:
            self._archivedVisits.find(current.text(0))
        except AttributeError:
            pass
        except KeyError:
            pass
<<<<<<< HEAD
        self.populate_visit_orderlines_list()

    @pyqtSlot(name="data_export")
    def data_export(self):
=======
        self.populate_archived_visit_details()

    @pyqtSlot(name="on_order_item_changed")
    def on_order_item_changed(self):
        """Update SKU combo when item changes"""
        self.comboOrderSku.setCurrentText(
            self.comboOrderItem.itemData(
                self.comboOrderItem.currentIndex())[0])
        self.update_orderline_text(self.comboOrderItem.itemData(
                self.comboOrderItem.currentIndex())[1])
        utils.item_price(
            self.comboOrderItem.itemData(
                self.comboOrderItem.currentIndex())[3], self.textVisitPcs.text())

    @pyqtSlot(name="on_order_sku_changed")
    def on_order_sku_changed(self):
        """Update ITEM combo when sku changes"""
        self.comboOrderItem.setCurrentText(
            self.comboOrderSku.itemData(
                self.comboOrderSku.currentIndex())[0])
        self.update_orderline_text(self.comboOrderSku.itemData(
                self.comboOrderSku.currentIndex())[1])
        utils.item_price(
            self.comboOrderSku.itemData(
                self.comboOrderSku.currentIndex()[3]), self.textVisitPcs.text())

    def update_orderline_text(self, text):
        self.textVisitLineText.setText(text)

    @pyqtSlot(name="show_csv_import_dialog")
    def show_csv_import_dialog(self):
>>>>>>> version-0.4.1
        """
        Slot for fileImport triggered signal
        """
        if self._customers.list_:
            msgbox = QMessageBox()
            msgbox.warning(self,
                           __appname__,
                           "<strong>Ved import slettes alle eksisterende data</strong>!<br/><br/>"
                           "Det er alt eller intet af hensyn til datas sammenhæng.<br/>"
                           "Du <strong>SKAL</strong> importere <strong>ALLE<strong> tabeller fra listen!<br/><br/>"
                           "<strong>Gør du ikke det giver det uløselige problemer</strong>!",
                           QMessageBox.Ok)
        # app, contact, customer, detail, employee, report, visit, tables
        import_dialog = CsvFileImportDialog(
            app, contacts=self._contacts, customers=self._customers,
            employees=self._employees, orderlines=self._archivedOrderlines,
            reports=self._reports, tables=config.CSV_TABLES, visits=self._archivedVisits)
        import_dialog.sig_done.connect(self.on_csv_import_done)
        import_dialog.exec_()

    @pyqtSlot(name="show_page_customer")
    def show_page_customer(self):
        """
        Show page with customer
        """
        self.set_indexes(button="toolButtonCustomer")
        self.widgetAppPages.setCurrentIndex(PAGE_CUSTOMER)

    @pyqtSlot(name="show_page_customer_visits")
    def show_page_customer_visits(self):
        """
        Show page with customer visits and orders
        """
        self.set_indexes(button="toolButtonCustomerVisits")
        self.widgetAppPages.setCurrentIndex(PAGE_CUSTOMER_VISITS)

    @pyqtSlot(name="show_page_customers")
    def show_page_customers(self):
        """
        Show page with customer list
        """
        self.set_indexes(button="toolButtonCustomers")
        self.widgetAppPages.setCurrentIndex(PAGE_CUSTOMERS)

    @pyqtSlot(name="show_page_info")
    def show_page_info(self):
        """
        Show page with about Qt and Eordre
        """
<<<<<<< HEAD
        try:
            # check the report date
            # no report triggers KeyError which in turn launches the CreateReportDialog
            repdate = self._reports.active["rep_date"]
            if not repdate == self.txtWorkdate.text():
                # if active report is not the same replace it with workdate
                self._reports.__load_report(self.txtWorkdate.text())
                # trigger a KeyError if no report is current which launches the CreateReportDialog
                repdate = self._reports.active["rep_date"]
                # check if the report is sent
                if self._reports.active["sent"] == 1:
                    # we do not allow visits to be created on a report which is closed
                    self.buttonCreateVisit.setEnabled(False)
                else:
                    self.buttonCreateVisit.setEnabled(True)
            infotext = "Rapport aktiv for: {}".format(repdate)
            msgbox = QMessageBox()
            msgbox.information(self, __appname__, infotext, QMessageBox.Ok)
            return True

        except KeyError:
            # Show report dialog
            create_report_dialog = ReportDialogCreate(self.txtWorkdate.text())
            if create_report_dialog.exec_():
                # user chosed to create a report
                self.txtWorkdate.setText(create_report_dialog.workdate)
                # try load a report for that date
                self._reports.__load_report(self.txtWorkdate.text())
                try:
                    # did the user choose an existing report
                    _ = self._reports.active["rep_date"]
                    infotext = "Eksisterende rapport hentet: {}".format(self.txtWorkdate.text())
                except KeyError:
                    # create the report
                    self._reports.create(self._employees.employee, self.txtWorkdate.text())
                    infotext = "Rapport oprettet for: {}".format(self.txtWorkdate.text())
                msgbox = QMessageBox()
                msgbox.information(self, __appname__, infotext, QMessageBox.Ok)
                return True
            else:
                msgbox = QMessageBox()
                msgbox.information(self,
                                   __appname__,
                                   "Den aktive rapport er <strong>IKKE</strong> ændret!",
                                   QMessageBox.Ok)
                return False

    @pyqtSlot(name="shoq_csv_import_dialog")
    def show_csv_import_dialog(self):
=======
        self.set_indexes(button="toolButtonInfo")
        self.widgetAppPages.setCurrentIndex(PAGE_INFO)

    @pyqtSlot(name="show_page_pricelist")
    def show_page_pricelist(self):
>>>>>>> version-0.4.1
        """
        Show page with pricelist
        """
<<<<<<< HEAD
        if self._customers.list_:
            msgbox = QMessageBox()
            msgbox.warning(self,
                           __appname__,
                           "<strong>Ved import slettes alle eksisterende data</strong>!<br/><br/>"
                           "Det er alt eller intet af hensyn til datas sammenhæng.<br/>"
                           "Du <strong>SKAL</strong> importere <strong>ALLE<strong> tabeller fra listen!<br/><br/>"
                           "<strong>Gør du ikke det giver det uløselige problemer</strong>!",
                           QMessageBox.Ok)
        # app, contact, customer, detail, employee, report, visit, tables
        import_dialog = CsvFileImportDialog(app, contacts=self._contacts, customers=self._customers,
                                            employees=self._employees, orderlines=self._orderlines,
                                            reports=self._reports, tables=config.CSV_TABLES, visits=self._visits)
        import_dialog.sig_done.connect(self.on_csv_import_done)
        import_dialog.exec_()
=======
        self.set_indexes(button="toolButtonPricelist")
        self.widgetAppPages.setCurrentIndex(PAGE_PRICELIST)
>>>>>>> version-0.4.1

    @pyqtSlot(name="show_page_report")
    def show_page_report(self):
        """
        Slot for masterData triggered signal
        """
        self.set_indexes(button="toolButtonReport")
        self.widgetAppPages.setCurrentIndex(PAGE_REPORT)

    @pyqtSlot(name="show_page_reports")
    def show_page_reports(self):
        """
        Show page with a report list
        """
        self.set_indexes(button="toolButtonReports")
        self.widgetAppPages.setCurrentIndex(PAGE_REPORTS)

    @pyqtSlot(name="show_page_settings")
    def show_page_settings(self):
        """
        Show page with settings
        """
        self.set_indexes(button="toolButtonSettings")
        self.populate_settings_page()
        self.widgetAppPages.setCurrentIndex(PAGE_SETTINGS)

    @pyqtSlot(name="show_page_visit")
    def show_page_visit(self):
        """
        Show page with visit
        """
        self.set_indexes(button="toolButtonVisit")
        self.widgetAppPages.setCurrentIndex(PAGE_VISIT)

    @pyqtSlot(name="visit_add_line")
    def visit_add_line(self):
        """
        Slot for Add Demo button clicked
        """
        new_row = self.widgetVisitOrderLines.rowCount() + 1
        self.widgetVisitOrderLines.setRowCount(new_row)
        self.widgetVisitOrderLines.setRowHeight(new_row, 20)

    @pyqtSlot(name="visit_clear_line")
    def visit_clear_line(self):
        """
        Clear visit line
        """
        # TODO clear the add visit line
        msgbox = QMessageBox()
        msgbox.information(self,
                           __appname__,
                           "# TODO clear the add visit line",
                           QMessageBox.Ok)

    @pyqtSlot(name="visit_line_type_changed")
    def visit_line_type_changed(self):
        """
        Changed linetype
        `D`emo `N`ysalg `S`alg `T`ekst
        :return: nothing
        """
<<<<<<< HEAD
        try:
            # do we have a report
            _ = self._reports.active["rep_date"]
            active_report = True
        except KeyError:
            active_report = self.show_create_report_dialog()

        if active_report:
            self._reports.__load_report(self.txtWorkdate.text())
            try:
                # do we have a customer
                _ = self._customers.customer["company"]
            except KeyError:
                msgbox = QMessageBox()
                msgbox.information(self,
                                   __appname__,
                                   "Ingen valgt kunde! Besøg kan ikke oprettes.",
                                   QMessageBox.Ok)
                return
            # Launch the visit dialog
            visit_dialog = VisitDialog(customers=self._customers,
                                       employees=self._employees,
                                       products=self._products,
                                       reports=self._reports,
                                       visits=self._visits)
            if visit_dialog.exec_():
                pass
=======
        if self.comboVisitLineType.currentText() == "T":
            self.set_input_enabled(False)
            return
        self.set_input_enabled(True)
>>>>>>> version-0.4.1

    @pyqtSlot(name="zero_database")
    def zero_database(self):
        """
        Slot for zeroDatabase triggered signal
        """
<<<<<<< HEAD
        self._contacts.recreate_table()
        self._customers.recreate_table()
        self._orderlines.recreate_table()
        self._visits.recreate_table()
        self._reports.recreate_table()

        self.populate_contact_list()
        self.populate_visit_orderlines_list()
        self.populate_visit_list()
        self.populate_customer_list()

        self._settings.setting["lsc"] = ""
        self._settings.setting["sac"] = ""
        self._settings.setting["lsp"] = ""
        self._settings.setting["sap"] = ""
        self._settings.update()
        self.display_sync_status()
=======
        confirm = QMessageBox()
        val = confirm.question(self, __appname__, "Alle salgsdata slettes<br/>Vil du fortsætte?", confirm.Yes | confirm.No)

        if val == confirm.Yes:
            self._contacts.recreate_table()
            self._customers.recreate_table()
            self._archivedOrderlines.recreate_table()
            self._archivedVisits.recreate_table()
            self._reports.recreate_table()

            self.populate_contact_list()
            self.populate_archived_visit_details()
            self.populate_archived_visits()
            self.populate_customer_list()

            self._settings.setting["lsc"] = ""
            self._settings.setting["sac"] = ""
            self._settings.setting["lsp"] = ""
            self._settings.setting["sap"] = ""
            self._settings.update()
            self.display_sync_status()
>>>>>>> version-0.4.1

            msgbox = QMessageBox()
            msgbox.information(self, __appname__, "Salgsdata er nulstillet!", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setAutoSipEnabled(True)
    # app.setDesktopSettingsAware(True)
    # app.setAttribute(Qt.AA_EnableHighDpiScaling)

    pixmap = QPixmap(":/splash/splash.png")
    splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
    splash.show()

    app.processEvents()

    window = MainWindow()
    window.show()

    QTimer.singleShot(1000, window.run)
    splash.finish(window)

    sys.exit(app.exec_())
