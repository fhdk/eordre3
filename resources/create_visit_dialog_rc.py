# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_visit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_visitDialog(object):
    def setupUi(self, visitDialog):
        visitDialog.setObjectName("visitDialog")
        visitDialog.resize(636, 568)
        self.formLayoutWidget = QtWidgets.QWidget(visitDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 321, 252))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formVisit = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formVisit.setContentsMargins(0, 0, 0, 0)
        self.formVisit.setObjectName("formVisit")
        self.txtVisitDate = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtVisitDate.setEnabled(True)
        self.txtVisitDate.setReadOnly(True)
        self.txtVisitDate.setObjectName("txtVisitDate")
        self.formVisit.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtVisitDate)
        self.txtPoBuyer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPoBuyer.setObjectName("txtPoBuyer")
        self.formVisit.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPoBuyer)
        self.txtPoNumber = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPoNumber.setObjectName("txtPoNumber")
        self.formVisit.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPoNumber)
        self.txtProductDemo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtProductDemo.setReadOnly(True)
        self.txtProductDemo.setObjectName("txtProductDemo")
        self.formVisit.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtProductDemo)
        self.txtProductSale = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtProductSale.setReadOnly(True)
        self.txtProductSale.setObjectName("txtProductSale")
        self.formVisit.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtProductSale)
        self.txtInfoText = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtInfoText.setObjectName("txtInfoText")
        self.formVisit.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtInfoText)
        self.visitWidget = QtWidgets.QTableWidget(visitDialog)
        self.visitWidget.setGeometry(QtCore.QRect(10, 296, 620, 220))
        self.visitWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.visitWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.visitWidget.setObjectName("visitWidget")
        self.visitWidget.setColumnCount(10)
        self.visitWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitWidget.setHorizontalHeaderItem(9, item)
        self.visitWidget.horizontalHeader().setDefaultSectionSize(70)
        self.visitWidget.horizontalHeader().setMinimumSectionSize(10)
        self.visitWidget.verticalHeader().setStretchLastSection(True)
        self.formLayoutWidget_2 = QtWidgets.QWidget(visitDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(339, 40, 291, 206))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formDeliveryAddress = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formDeliveryAddress.setContentsMargins(0, 0, 0, 0)
        self.formDeliveryAddress.setObjectName("formDeliveryAddress")
        self.txtPoCompany = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtPoCompany.setObjectName("txtPoCompany")
        self.formDeliveryAddress.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPoCompany)
        self.txtPoAddress1 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtPoAddress1.setObjectName("txtPoAddress1")
        self.formDeliveryAddress.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPoAddress1)
        self.txtPoAddress2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtPoAddress2.setObjectName("txtPoAddress2")
        self.formDeliveryAddress.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPoAddress2)
        self.txtPoPostcode = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtPoPostcode.setObjectName("txtPoPostcode")
        self.formDeliveryAddress.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtPoPostcode)
        self.txtPoPostoffice = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtPoPostoffice.setObjectName("txtPoPostoffice")
        self.formDeliveryAddress.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtPoPostoffice)
        self.txtPoCountry = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtPoCountry.setObjectName("txtPoCountry")
        self.formDeliveryAddress.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtPoCountry)
        self.gridLayoutWidget = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(340, 260, 290, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridTotals = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridTotals.setContentsMargins(0, 0, 0, 0)
        self.gridTotals.setObjectName("gridTotals")
        self.labelSale = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelSale.setObjectName("labelSale")
        self.gridTotals.addWidget(self.labelSale, 1, 0, 1, 1)
        self.labelSAS = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelSAS.setObjectName("labelSAS")
        self.gridTotals.addWidget(self.labelSAS, 1, 2, 1, 1)
        self.txtVisitSale = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtVisitSale.setEnabled(True)
        self.txtVisitSale.setReadOnly(True)
        self.txtVisitSale.setObjectName("txtVisitSale")
        self.gridTotals.addWidget(self.txtVisitSale, 1, 1, 1, 1)
        self.txtVisitSas = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtVisitSas.setEnabled(True)
        self.txtVisitSas.setReadOnly(True)
        self.txtVisitSas.setObjectName("txtVisitSas")
        self.gridTotals.addWidget(self.txtVisitSas, 1, 3, 1, 1)
        self.lableTotal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lableTotal.setObjectName("lableTotal")
        self.gridTotals.addWidget(self.lableTotal, 1, 4, 1, 1)
        self.txtVisitTotal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtVisitTotal.setEnabled(True)
        self.txtVisitTotal.setReadOnly(True)
        self.txtVisitTotal.setObjectName("txtVisitTotal")
        self.gridTotals.addWidget(self.txtVisitTotal, 1, 5, 1, 1)
        self.line = QtWidgets.QFrame(visitDialog)
        self.line.setGeometry(QtCore.QRect(330, 40, 16, 250))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 621, 35))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridCustomerVisit = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridCustomerVisit.setContentsMargins(0, 0, 0, 0)
        self.gridCustomerVisit.setObjectName("gridCustomerVisit")
        self.lblCompany = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblCompany.setFont(font)
        self.lblCompany.setObjectName("lblCompany")
        self.gridCustomerVisit.addWidget(self.lblCompany, 0, 0, 1, 1)
        self.txtCompany = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtCompany.setFont(font)
        self.txtCompany.setReadOnly(True)
        self.txtCompany.setObjectName("txtCompany")
        self.gridCustomerVisit.addWidget(self.txtCompany, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 520, 621, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridOrderButtons = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridOrderButtons.setContentsMargins(0, 0, 0, 0)
        self.gridOrderButtons.setObjectName("gridOrderButtons")
        self.btnAddSale = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btnAddSale.setDefault(True)
        self.btnAddSale.setObjectName("btnAddSale")
        self.gridOrderButtons.addWidget(self.btnAddSale, 0, 1, 1, 1)
        self.buttonArchiveVisit = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.buttonArchiveVisit.setObjectName("buttonArchiveVisit")
        self.gridOrderButtons.addWidget(self.buttonArchiveVisit, 0, 2, 1, 1)
        self.btnAddDemo = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btnAddDemo.setObjectName("btnAddDemo")
        self.gridOrderButtons.addWidget(self.btnAddDemo, 0, 0, 1, 1)

        self.retranslateUi(visitDialog)
        QtCore.QMetaObject.connectSlotsByName(visitDialog)
        visitDialog.setTabOrder(self.txtVisitDate, self.txtPoBuyer)
        visitDialog.setTabOrder(self.txtPoBuyer, self.txtPoNumber)
        visitDialog.setTabOrder(self.txtPoNumber, self.txtProductDemo)
        visitDialog.setTabOrder(self.txtProductDemo, self.txtProductSale)
        visitDialog.setTabOrder(self.txtProductSale, self.txtInfoText)
        visitDialog.setTabOrder(self.txtInfoText, self.txtPoCompany)
        visitDialog.setTabOrder(self.txtPoCompany, self.txtPoAddress1)
        visitDialog.setTabOrder(self.txtPoAddress1, self.txtPoAddress2)
        visitDialog.setTabOrder(self.txtPoAddress2, self.txtPoPostcode)
        visitDialog.setTabOrder(self.txtPoPostcode, self.txtPoPostoffice)
        visitDialog.setTabOrder(self.txtPoPostoffice, self.txtPoCountry)
        visitDialog.setTabOrder(self.txtPoCountry, self.txtVisitSale)
        visitDialog.setTabOrder(self.txtVisitSale, self.txtVisitSas)
        visitDialog.setTabOrder(self.txtVisitSas, self.txtVisitTotal)
        visitDialog.setTabOrder(self.txtVisitTotal, self.visitWidget)
        visitDialog.setTabOrder(self.visitWidget, self.btnAddSale)

    def retranslateUi(self, visitDialog):
        _translate = QtCore.QCoreApplication.translate
        visitDialog.setWindowTitle(_translate("visitDialog", "Besøg / Indkøbs ordre"))
        self.txtVisitDate.setPlaceholderText(_translate("visitDialog", "Ordre dato"))
        self.txtPoBuyer.setPlaceholderText(_translate("visitDialog", "Indkøber"))
        self.txtPoNumber.setPlaceholderText(_translate("visitDialog", "Rekvisition"))
        self.txtProductDemo.setPlaceholderText(_translate("visitDialog", "Produkt demo"))
        self.txtProductSale.setPlaceholderText(_translate("visitDialog", "Produkt salg"))
        item = self.visitWidget.horizontalHeaderItem(0)
        item.setText(_translate("visitDialog", "d/n/s"))
        item = self.visitWidget.horizontalHeaderItem(1)
        item.setText(_translate("visitDialog", "Antal"))
        item = self.visitWidget.horizontalHeaderItem(2)
        item.setText(_translate("visitDialog", "Produkt"))
        item = self.visitWidget.horizontalHeaderItem(3)
        item.setText(_translate("visitDialog", "Varenr"))
        item = self.visitWidget.horizontalHeaderItem(4)
        item.setText(_translate("visitDialog", "Tekst"))
        item = self.visitWidget.horizontalHeaderItem(5)
        item.setText(_translate("visitDialog", "Pris"))
        item = self.visitWidget.horizontalHeaderItem(6)
        item.setText(_translate("visitDialog", "%"))
        item = self.visitWidget.horizontalHeaderItem(7)
        item.setText(_translate("visitDialog", "Beløb"))
        item = self.visitWidget.horizontalHeaderItem(8)
        item.setText(_translate("visitDialog", "SAS"))
        item = self.visitWidget.horizontalHeaderItem(9)
        item.setText(_translate("visitDialog", "Note"))
        self.txtPoCompany.setPlaceholderText(_translate("visitDialog", "Leveres til"))
        self.txtPoAddress1.setPlaceholderText(_translate("visitDialog", "Leverings adresse 1"))
        self.txtPoAddress2.setPlaceholderText(_translate("visitDialog", "Leverings adresse 2"))
        self.txtPoPostcode.setPlaceholderText(_translate("visitDialog", "Leverings adresse postnummer"))
        self.txtPoPostoffice.setPlaceholderText(_translate("visitDialog", "Leverings adresse bynavn"))
        self.txtPoCountry.setPlaceholderText(_translate("visitDialog", "Leverings adresse land"))
        self.labelSale.setText(_translate("visitDialog", "Salg"))
        self.labelSAS.setText(_translate("visitDialog", "SAS"))
        self.lableTotal.setText(_translate("visitDialog", "Total"))
        self.lblCompany.setText(_translate("visitDialog", "Kunde "))
        self.btnAddSale.setText(_translate("visitDialog", "Nyt salg"))
        self.buttonArchiveVisit.setText(_translate("visitDialog", "Arkiver"))
        self.btnAddDemo.setText(_translate("visitDialog", "Opret demo"))

