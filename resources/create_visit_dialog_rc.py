# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_visit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createVisitDialog(object):
    def setupUi(self, createVisitDialog):
        createVisitDialog.setObjectName("createVisitDialog")
        createVisitDialog.resize(636, 568)
        self.formLayoutWidget = QtWidgets.QWidget(createVisitDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 321, 252))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formVisit = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formVisit.setContentsMargins(0, 0, 0, 0)
        self.formVisit.setObjectName("formVisit")
        self.txtOrderVisitDate = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtOrderVisitDate.setEnabled(False)
        self.txtOrderVisitDate.setObjectName("txtOrderVisitDate")
        self.formVisit.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtOrderVisitDate)
        self.txtBuyer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtBuyer.setObjectName("txtBuyer")
        self.formVisit.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtBuyer)
        self.txtPurchaseOrder = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPurchaseOrder.setObjectName("txtPurchaseOrder")
        self.formVisit.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPurchaseOrder)
        self.txtProductDemo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtProductDemo.setReadOnly(True)
        self.txtProductDemo.setObjectName("txtProductDemo")
        self.formVisit.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtProductDemo)
        self.txtProductSale = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtProductSale.setReadOnly(True)
        self.txtProductSale.setObjectName("txtProductSale")
        self.formVisit.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtProductSale)
        self.txtNote = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtNote.setObjectName("txtNote")
        self.formVisit.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtNote)
        self.visitWidget = QtWidgets.QTableWidget(createVisitDialog)
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
        self.formLayoutWidget_2 = QtWidgets.QWidget(createVisitDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(339, 40, 291, 206))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formDeliveryAddress = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formDeliveryAddress.setContentsMargins(0, 0, 0, 0)
        self.formDeliveryAddress.setObjectName("formDeliveryAddress")
        self.txtDeliverCompany = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtDeliverCompany.setObjectName("txtDeliverCompany")
        self.formDeliveryAddress.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtDeliverCompany)
        self.txtDeliverAddress1 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtDeliverAddress1.setObjectName("txtDeliverAddress1")
        self.formDeliveryAddress.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtDeliverAddress1)
        self.txtDeliverAddress2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtDeliverAddress2.setObjectName("txtDeliverAddress2")
        self.formDeliveryAddress.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtDeliverAddress2)
        self.txtZipCode = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtZipCode.setObjectName("txtZipCode")
        self.formDeliveryAddress.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtZipCode)
        self.txtCityName = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtCityName.setObjectName("txtCityName")
        self.formDeliveryAddress.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtCityName)
        self.txtDeliverCountry = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtDeliverCountry.setObjectName("txtDeliverCountry")
        self.formDeliveryAddress.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtDeliverCountry)
        self.gridLayoutWidget = QtWidgets.QWidget(createVisitDialog)
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
        self.txtOrderSale = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtOrderSale.setEnabled(False)
        self.txtOrderSale.setObjectName("txtOrderSale")
        self.gridTotals.addWidget(self.txtOrderSale, 1, 1, 1, 1)
        self.txtOrderSas = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtOrderSas.setEnabled(False)
        self.txtOrderSas.setObjectName("txtOrderSas")
        self.gridTotals.addWidget(self.txtOrderSas, 1, 3, 1, 1)
        self.lableTotal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lableTotal.setObjectName("lableTotal")
        self.gridTotals.addWidget(self.lableTotal, 1, 4, 1, 1)
        self.txtOrderTotal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtOrderTotal.setEnabled(False)
        self.txtOrderTotal.setObjectName("txtOrderTotal")
        self.gridTotals.addWidget(self.txtOrderTotal, 1, 5, 1, 1)
        self.line = QtWidgets.QFrame(createVisitDialog)
        self.line.setGeometry(QtCore.QRect(330, 40, 16, 250))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(createVisitDialog)
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
        self.txtCompany.setObjectName("txtCompany")
        self.gridCustomerVisit.addWidget(self.txtCompany, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(createVisitDialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 520, 621, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridOrderButtons = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridOrderButtons.setContentsMargins(0, 0, 0, 0)
        self.gridOrderButtons.setObjectName("gridOrderButtons")
        self.buttonAddSale = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.buttonAddSale.setDefault(True)
        self.buttonAddSale.setObjectName("buttonAddSale")
        self.gridOrderButtons.addWidget(self.buttonAddSale, 0, 1, 1, 1)
        self.buttonSaveVisit = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.buttonSaveVisit.setObjectName("buttonSaveVisit")
        self.gridOrderButtons.addWidget(self.buttonSaveVisit, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.gridOrderButtons.addWidget(self.pushButton, 0, 0, 1, 1)

        self.retranslateUi(createVisitDialog)
        QtCore.QMetaObject.connectSlotsByName(createVisitDialog)
        createVisitDialog.setTabOrder(self.txtOrderVisitDate, self.txtBuyer)
        createVisitDialog.setTabOrder(self.txtBuyer, self.txtPurchaseOrder)
        createVisitDialog.setTabOrder(self.txtPurchaseOrder, self.txtProductDemo)
        createVisitDialog.setTabOrder(self.txtProductDemo, self.txtProductSale)
        createVisitDialog.setTabOrder(self.txtProductSale, self.txtNote)
        createVisitDialog.setTabOrder(self.txtNote, self.txtDeliverCompany)
        createVisitDialog.setTabOrder(self.txtDeliverCompany, self.txtDeliverAddress1)
        createVisitDialog.setTabOrder(self.txtDeliverAddress1, self.txtDeliverAddress2)
        createVisitDialog.setTabOrder(self.txtDeliverAddress2, self.txtZipCode)
        createVisitDialog.setTabOrder(self.txtZipCode, self.txtCityName)
        createVisitDialog.setTabOrder(self.txtCityName, self.txtDeliverCountry)
        createVisitDialog.setTabOrder(self.txtDeliverCountry, self.txtOrderSale)
        createVisitDialog.setTabOrder(self.txtOrderSale, self.txtOrderSas)
        createVisitDialog.setTabOrder(self.txtOrderSas, self.txtOrderTotal)
        createVisitDialog.setTabOrder(self.txtOrderTotal, self.visitWidget)
        createVisitDialog.setTabOrder(self.visitWidget, self.buttonAddSale)

    def retranslateUi(self, createVisitDialog):
        _translate = QtCore.QCoreApplication.translate
        createVisitDialog.setWindowTitle(_translate("createVisitDialog", "Besøg / Indkøbs ordre"))
        self.txtOrderVisitDate.setPlaceholderText(_translate("createVisitDialog", "Ordre dato"))
        self.txtBuyer.setPlaceholderText(_translate("createVisitDialog", "Indkøber"))
        self.txtPurchaseOrder.setPlaceholderText(_translate("createVisitDialog", "Rekvisition"))
        self.txtProductDemo.setPlaceholderText(_translate("createVisitDialog", "Produkt demo"))
        self.txtProductSale.setPlaceholderText(_translate("createVisitDialog", "Produkt salg"))
        item = self.visitWidget.horizontalHeaderItem(0)
        item.setText(_translate("createVisitDialog", "d/n/s"))
        item = self.visitWidget.horizontalHeaderItem(1)
        item.setText(_translate("createVisitDialog", "Antal"))
        item = self.visitWidget.horizontalHeaderItem(2)
        item.setText(_translate("createVisitDialog", "Produkt"))
        item = self.visitWidget.horizontalHeaderItem(3)
        item.setText(_translate("createVisitDialog", "Varenr"))
        item = self.visitWidget.horizontalHeaderItem(4)
        item.setText(_translate("createVisitDialog", "Tekst"))
        item = self.visitWidget.horizontalHeaderItem(5)
        item.setText(_translate("createVisitDialog", "Pris"))
        item = self.visitWidget.horizontalHeaderItem(6)
        item.setText(_translate("createVisitDialog", "%"))
        item = self.visitWidget.horizontalHeaderItem(7)
        item.setText(_translate("createVisitDialog", "Beløb"))
        item = self.visitWidget.horizontalHeaderItem(8)
        item.setText(_translate("createVisitDialog", "SAS"))
        item = self.visitWidget.horizontalHeaderItem(9)
        item.setText(_translate("createVisitDialog", "Note"))
        self.txtDeliverCompany.setPlaceholderText(_translate("createVisitDialog", "Leveres til"))
        self.txtDeliverAddress1.setPlaceholderText(_translate("createVisitDialog", "Leverings adresse 1"))
        self.txtDeliverAddress2.setPlaceholderText(_translate("createVisitDialog", "Leverings adresse 2"))
        self.txtZipCode.setPlaceholderText(_translate("createVisitDialog", "Leverings adresse postnummer"))
        self.txtCityName.setPlaceholderText(_translate("createVisitDialog", "Leverings adresse bynavn"))
        self.txtDeliverCountry.setPlaceholderText(_translate("createVisitDialog", "Leverings adresse land"))
        self.labelSale.setText(_translate("createVisitDialog", "Salg"))
        self.labelSAS.setText(_translate("createVisitDialog", "SAS"))
        self.lableTotal.setText(_translate("createVisitDialog", "Total"))
        self.lblCompany.setText(_translate("createVisitDialog", "Kunde "))
        self.buttonAddSale.setText(_translate("createVisitDialog", "Nyt salg"))
        self.buttonSaveVisit.setText(_translate("createVisitDialog", "Arkiver"))
        self.pushButton.setText(_translate("createVisitDialog", "Opret demo"))
