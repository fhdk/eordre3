# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_visitDialog(object):
    def setupUi(self, visitDialog):
        visitDialog.setObjectName("visitDialog")
        visitDialog.resize(800, 600)
        visitDialog.setMinimumSize(QtCore.QSize(800, 600))
        self.widgetVisitDetails = QtWidgets.QTableWidget(visitDialog)
        self.widgetVisitDetails.setGeometry(QtCore.QRect(10, 410, 780, 180))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widgetVisitDetails.setFont(font)
        self.widgetVisitDetails.setLocale(QtCore.QLocale(QtCore.QLocale.Danish, QtCore.QLocale.Denmark))
        self.widgetVisitDetails.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.widgetVisitDetails.setAlternatingRowColors(True)
        self.widgetVisitDetails.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.widgetVisitDetails.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.widgetVisitDetails.setCornerButtonEnabled(False)
        self.widgetVisitDetails.setColumnCount(11)
        self.widgetVisitDetails.setObjectName("widgetVisitDetails")
        self.widgetVisitDetails.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.widgetVisitDetails.setHorizontalHeaderItem(8, item)
        self.widgetVisitDetails.horizontalHeader().setCascadingSectionResizes(True)
        self.widgetVisitDetails.horizontalHeader().setDefaultSectionSize(50)
        self.widgetVisitDetails.horizontalHeader().setMinimumSectionSize(10)
        self.widgetVisitDetails.verticalHeader().setMinimumSectionSize(20)
        self.widgetVisitDetails.verticalHeader().setStretchLastSection(True)
        self.gridLayoutWidget = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(410, 10, 380, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridTotals = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridTotals.setContentsMargins(0, 0, 0, 0)
        self.gridTotals.setObjectName("gridTotals")
        self.lblSale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSale.setFont(font)
        self.lblSale.setObjectName("lblSale")
        self.gridTotals.addWidget(self.lblSale, 1, 0, 1, 1)
        self.lblSas = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSas.setFont(font)
        self.lblSas.setObjectName("lblSas")
        self.gridTotals.addWidget(self.lblSas, 1, 2, 1, 1)
        self.txtVisitSale = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtVisitSale.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtVisitSale.setFont(font)
        self.txtVisitSale.setReadOnly(True)
        self.txtVisitSale.setObjectName("txtVisitSale")
        self.gridTotals.addWidget(self.txtVisitSale, 1, 1, 1, 1)
        self.txtVisitSas = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtVisitSas.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtVisitSas.setFont(font)
        self.txtVisitSas.setReadOnly(True)
        self.txtVisitSas.setObjectName("txtVisitSas")
        self.gridTotals.addWidget(self.txtVisitSas, 1, 3, 1, 1)
        self.lblTotal = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTotal.setFont(font)
        self.lblTotal.setObjectName("lblTotal")
        self.gridTotals.addWidget(self.lblTotal, 1, 4, 1, 1)
        self.txtVisitTotal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtVisitTotal.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtVisitTotal.setFont(font)
        self.txtVisitTotal.setReadOnly(True)
        self.txtVisitTotal.setObjectName("txtVisitTotal")
        self.gridTotals.addWidget(self.txtVisitTotal, 1, 5, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 380, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridCustomerVisit = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridCustomerVisit.setContentsMargins(0, 0, 0, 0)
        self.gridCustomerVisit.setObjectName("gridCustomerVisit")
        self.txtCompany = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCompany.setFont(font)
        self.txtCompany.setReadOnly(True)
        self.txtCompany.setObjectName("txtCompany")
        self.gridCustomerVisit.addWidget(self.txtCompany, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 280, 780, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget_3.setFont(font)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridOrderButtons = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridOrderButtons.setContentsMargins(0, 0, 0, 0)
        self.gridOrderButtons.setObjectName("gridOrderButtons")
        self.btnInsertLine = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnInsertLine.setFont(font)
        self.btnInsertLine.setAutoDefault(False)
        self.btnInsertLine.setObjectName("btnInsertLine")
        self.gridOrderButtons.addWidget(self.btnInsertLine, 0, 0, 1, 1)
        self.btnArchiveVisit = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnArchiveVisit.setFont(font)
        self.btnArchiveVisit.setAutoDefault(False)
        self.btnArchiveVisit.setObjectName("btnArchiveVisit")
        self.gridOrderButtons.addWidget(self.btnArchiveVisit, 0, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 380, 221))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.widgetVisitHead = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.widgetVisitHead.setContentsMargins(0, 0, 0, 0)
        self.widgetVisitHead.setObjectName("widgetVisitHead")
        self.txtProductDemo = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtProductDemo.setFont(font)
        self.txtProductDemo.setReadOnly(True)
        self.txtProductDemo.setObjectName("txtProductDemo")
        self.widgetVisitHead.addWidget(self.txtProductDemo, 3, 0, 1, 1)
        self.txtVisitDate = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.txtVisitDate.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtVisitDate.setFont(font)
        self.txtVisitDate.setReadOnly(True)
        self.txtVisitDate.setObjectName("txtVisitDate")
        self.widgetVisitHead.addWidget(self.txtVisitDate, 0, 0, 1, 1)
        self.txtPoAddress2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoAddress2.setFont(font)
        self.txtPoAddress2.setObjectName("txtPoAddress2")
        self.widgetVisitHead.addWidget(self.txtPoAddress2, 2, 1, 1, 1)
        self.txtPoNumber = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoNumber.setFont(font)
        self.txtPoNumber.setObjectName("txtPoNumber")
        self.widgetVisitHead.addWidget(self.txtPoNumber, 2, 0, 1, 1)
        self.txtPoAddress1 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoAddress1.setFont(font)
        self.txtPoAddress1.setObjectName("txtPoAddress1")
        self.widgetVisitHead.addWidget(self.txtPoAddress1, 1, 1, 1, 1)
        self.txtPoCompany = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoCompany.setFont(font)
        self.txtPoCompany.setObjectName("txtPoCompany")
        self.widgetVisitHead.addWidget(self.txtPoCompany, 0, 1, 1, 1)
        self.txtProductSale = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtProductSale.setFont(font)
        self.txtProductSale.setReadOnly(True)
        self.txtProductSale.setObjectName("txtProductSale")
        self.widgetVisitHead.addWidget(self.txtProductSale, 4, 0, 1, 1)
        self.txtPoPostoffice = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoPostoffice.setFont(font)
        self.txtPoPostoffice.setObjectName("txtPoPostoffice")
        self.widgetVisitHead.addWidget(self.txtPoPostoffice, 4, 1, 1, 1)
        self.txtPoPostcode = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoPostcode.setFont(font)
        self.txtPoPostcode.setObjectName("txtPoPostcode")
        self.widgetVisitHead.addWidget(self.txtPoPostcode, 3, 1, 1, 1)
        self.txtPoBuyer = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoBuyer.setFont(font)
        self.txtPoBuyer.setObjectName("txtPoBuyer")
        self.widgetVisitHead.addWidget(self.txtPoBuyer, 1, 0, 1, 1)
        self.txtPoCountry = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPoCountry.setFont(font)
        self.txtPoCountry.setObjectName("txtPoCountry")
        self.widgetVisitHead.addWidget(self.txtPoCountry, 5, 1, 1, 1)
        self.formLayoutWidget = QtWidgets.QWidget(visitDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(410, 50, 380, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.widgetInfos = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.widgetInfos.setContentsMargins(0, 0, 0, 0)
        self.widgetInfos.setObjectName("widgetInfos")
        self.lblOrderInfo = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblOrderInfo.setFont(font)
        self.lblOrderInfo.setObjectName("lblOrderInfo")
        self.widgetInfos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblOrderInfo)
        self.txtOrderInfo = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtOrderInfo.setFont(font)
        self.txtOrderInfo.setAcceptRichText(False)
        self.txtOrderInfo.setObjectName("txtOrderInfo")
        self.widgetInfos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtOrderInfo)
        self.lblVisitInfo = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblVisitInfo.setFont(font)
        self.lblVisitInfo.setObjectName("lblVisitInfo")
        self.widgetInfos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblVisitInfo)
        self.txtVisitInfo = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtVisitInfo.setFont(font)
        self.txtVisitInfo.setObjectName("txtVisitInfo")
        self.widgetInfos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtVisitInfo)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(visitDialog)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 340, 700, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget_5.setFont(font)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.cboProduct = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.cboProduct.setMinimumSize(QtCore.QSize(80, 0))
        self.cboProduct.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboProduct.setFont(font)
        self.cboProduct.setObjectName("cboProduct")
        self.cboProduct.addItem("")
        self.cboProduct.addItem("")
        self.cboProduct.addItem("")
        self.cboProduct.addItem("")
        self.cboProduct.addItem("")
        self.cboProduct.addItem("")
        self.cboProduct.addItem("")
        self.gridLayout.addWidget(self.cboProduct, 1, 2, 1, 1)
        self.lblPrice = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPrice.setFont(font)
        self.lblPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPrice.setObjectName("lblPrice")
        self.gridLayout.addWidget(self.lblPrice, 0, 5, 1, 1)
        self.txtPcs = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.txtPcs.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPcs.setFont(font)
        self.txtPcs.setMaxLength(4)
        self.txtPcs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtPcs.setObjectName("txtPcs")
        self.gridLayout.addWidget(self.txtPcs, 1, 1, 1, 1)
        self.lblPcs = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPcs.setFont(font)
        self.lblPcs.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPcs.setObjectName("lblPcs")
        self.gridLayout.addWidget(self.lblPcs, 0, 1, 1, 1)
        self.cboDns = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.cboDns.setMinimumSize(QtCore.QSize(5, 0))
        self.cboDns.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboDns.setFont(font)
        self.cboDns.setMaxCount(3)
        self.cboDns.setObjectName("cboDns")
        self.cboDns.addItem("")
        self.cboDns.addItem("")
        self.cboDns.addItem("")
        self.gridLayout.addWidget(self.cboDns, 1, 0, 1, 1)
        self.lblDemoNotSold = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDemoNotSold.setFont(font)
        self.lblDemoNotSold.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDemoNotSold.setObjectName("lblDemoNotSold")
        self.gridLayout.addWidget(self.lblDemoNotSold, 0, 0, 1, 1)
        self.lblLineSum = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLineSum.setFont(font)
        self.lblLineSum.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLineSum.setObjectName("lblLineSum")
        self.gridLayout.addWidget(self.lblLineSum, 0, 7, 1, 1)
        self.cboSku = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.cboSku.setMinimumSize(QtCore.QSize(120, 0))
        self.cboSku.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboSku.setFont(font)
        self.cboSku.setObjectName("cboSku")
        self.cboSku.addItem("")
        self.cboSku.addItem("")
        self.cboSku.addItem("")
        self.gridLayout.addWidget(self.cboSku, 1, 3, 1, 1)
        self.lblSku = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSku.setFont(font)
        self.lblSku.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSku.setObjectName("lblSku")
        self.gridLayout.addWidget(self.lblSku, 0, 3, 1, 1)
        self.lblProduct = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblProduct.setFont(font)
        self.lblProduct.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProduct.setObjectName("lblProduct")
        self.gridLayout.addWidget(self.lblProduct, 0, 2, 1, 1)
        self.txtLineDiscount = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.txtLineDiscount.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txtLineDiscount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtLineDiscount.setObjectName("txtLineDiscount")
        self.gridLayout.addWidget(self.txtLineDiscount, 1, 6, 1, 1)
        self.txtLineText = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.txtLineText.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtLineText.setFont(font)
        self.txtLineText.setObjectName("txtLineText")
        self.gridLayout.addWidget(self.txtLineText, 1, 4, 1, 1)
        self.lblText = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblText.setFont(font)
        self.lblText.setAlignment(QtCore.Qt.AlignCenter)
        self.lblText.setObjectName("lblText")
        self.gridLayout.addWidget(self.lblText, 0, 4, 1, 1)
        self.txtLinePrice = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.txtLinePrice.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtLinePrice.setFont(font)
        self.txtLinePrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtLinePrice.setObjectName("txtLinePrice")
        self.gridLayout.addWidget(self.txtLinePrice, 1, 5, 1, 1)
        self.txtLineSum = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.txtLineSum.setMinimumSize(QtCore.QSize(80, 0))
        self.txtLineSum.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txtLineSum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtLineSum.setObjectName("txtLineSum")
        self.gridLayout.addWidget(self.txtLineSum, 1, 7, 1, 1)
        self.chkSas = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.chkSas.setMinimumSize(QtCore.QSize(20, 25))
        self.chkSas.setMaximumSize(QtCore.QSize(20, 25))
        self.chkSas.setText("")
        self.chkSas.setObjectName("chkSas")
        self.gridLayout.addWidget(self.chkSas, 1, 8, 1, 1)
        self.lblCheckSas = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblCheckSas.setFont(font)
        self.lblCheckSas.setObjectName("lblCheckSas")
        self.gridLayout.addWidget(self.lblCheckSas, 0, 8, 1, 1)
        self.lblDiscount = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDiscount.setFont(font)
        self.lblDiscount.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDiscount.setObjectName("lblDiscount")
        self.gridLayout.addWidget(self.lblDiscount, 0, 6, 1, 1)

        self.retranslateUi(visitDialog)
        self.cboDns.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(visitDialog)
        visitDialog.setTabOrder(self.txtVisitSale, self.txtVisitSas)
        visitDialog.setTabOrder(self.txtVisitSas, self.txtVisitTotal)
        visitDialog.setTabOrder(self.txtVisitTotal, self.widgetVisitDetails)

    def retranslateUi(self, visitDialog):
        _translate = QtCore.QCoreApplication.translate
        visitDialog.setWindowTitle(_translate("visitDialog", "Besøg / Indkøbs ordre"))
        item = self.widgetVisitDetails.horizontalHeaderItem(0)
        item.setText(_translate("visitDialog", "*"))
        item = self.widgetVisitDetails.horizontalHeaderItem(1)
        item.setText(_translate("visitDialog", "Antal"))
        item = self.widgetVisitDetails.horizontalHeaderItem(2)
        item.setText(_translate("visitDialog", "Produkt"))
        item = self.widgetVisitDetails.horizontalHeaderItem(3)
        item.setText(_translate("visitDialog", "Varenr"))
        item = self.widgetVisitDetails.horizontalHeaderItem(4)
        item.setText(_translate("visitDialog", "Tekst"))
        item = self.widgetVisitDetails.horizontalHeaderItem(5)
        item.setText(_translate("visitDialog", "Pris"))
        item = self.widgetVisitDetails.horizontalHeaderItem(6)
        item.setText(_translate("visitDialog", "%"))
        item = self.widgetVisitDetails.horizontalHeaderItem(7)
        item.setText(_translate("visitDialog", "Beløb"))
        item = self.widgetVisitDetails.horizontalHeaderItem(8)
        item.setText(_translate("visitDialog", "SAS"))
        self.lblSale.setText(_translate("visitDialog", "Salg"))
        self.lblSas.setText(_translate("visitDialog", "SAS"))
        self.lblTotal.setText(_translate("visitDialog", "Total"))
        self.btnInsertLine.setText(_translate("visitDialog", "Tilføj linje"))
        self.btnArchiveVisit.setText(_translate("visitDialog", "Arkiver"))
        self.txtProductDemo.setPlaceholderText(_translate("visitDialog", "Produkt demo"))
        self.txtVisitDate.setPlaceholderText(_translate("visitDialog", "Ordre dato"))
        self.txtPoAddress2.setPlaceholderText(_translate("visitDialog", "Lev. adresse 2"))
        self.txtPoNumber.setPlaceholderText(_translate("visitDialog", "Rekvisition"))
        self.txtPoAddress1.setPlaceholderText(_translate("visitDialog", "Lev. adresse 1"))
        self.txtPoCompany.setPlaceholderText(_translate("visitDialog", "Lev. til"))
        self.txtProductSale.setPlaceholderText(_translate("visitDialog", "Produkt salg"))
        self.txtPoPostoffice.setPlaceholderText(_translate("visitDialog", "Lev. bynavn"))
        self.txtPoPostcode.setPlaceholderText(_translate("visitDialog", "Lev. postnummer"))
        self.txtPoBuyer.setPlaceholderText(_translate("visitDialog", "Indkøber"))
        self.txtPoCountry.setPlaceholderText(_translate("visitDialog", "Lev. land"))
        self.lblOrderInfo.setText(_translate("visitDialog", "Ordre notat:"))
        self.lblVisitInfo.setText(_translate("visitDialog", "Sælger notat:"))
        self.cboProduct.setItemText(0, _translate("visitDialog", "dbo"))
        self.cboProduct.setItemText(1, _translate("visitDialog", "sslsh"))
        self.cboProduct.setItemText(2, _translate("visitDialog", "speeda"))
        self.cboProduct.setItemText(3, _translate("visitDialog", "mfcps"))
        self.cboProduct.setItemText(4, _translate("visitDialog", "htwpro6"))
        self.cboProduct.setItemText(5, _translate("visitDialog", "rpcfsg"))
        self.cboProduct.setItemText(6, _translate("visitDialog", "as1500"))
        self.lblPrice.setText(_translate("visitDialog", "Pris"))
        self.lblPcs.setText(_translate("visitDialog", "Antal"))
        self.cboDns.setItemText(0, _translate("visitDialog", "D"))
        self.cboDns.setItemText(1, _translate("visitDialog", "N"))
        self.cboDns.setItemText(2, _translate("visitDialog", "S"))
        self.lblDemoNotSold.setText(_translate("visitDialog", "D/N/S"))
        self.lblLineSum.setText(_translate("visitDialog", "Beløb"))
        self.cboSku.setItemText(0, _translate("visitDialog", "02,3450,0005"))
        self.cboSku.setItemText(1, _translate("visitDialog", "02,0135"))
        self.cboSku.setItemText(2, _translate("visitDialog", "02,3100,5000"))
        self.lblSku.setText(_translate("visitDialog", "Varenr"))
        self.lblProduct.setText(_translate("visitDialog", "Produkt"))
        self.lblText.setText(_translate("visitDialog", "Tekst"))
        self.lblCheckSas.setText(_translate("visitDialog", "Sas"))
        self.lblDiscount.setText(_translate("visitDialog", "%"))

