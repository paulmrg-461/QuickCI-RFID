# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickCIMainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(993, 593)
        self.productsTable = QtWidgets.QTableWidget(Dialog)
        self.productsTable.setGeometry(QtCore.QRect(10, 60, 971, 421))
        self.productsTable.setObjectName("productsTable")
        self.productsTable.setColumnCount(4)
        self.productsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsTable.setHorizontalHeaderItem(3, item)
        self.lcdTotalOutput = QtWidgets.QLCDNumber(Dialog)
        self.lcdTotalOutput.setGeometry(QtCore.QRect(750, 500, 231, 41))
        self.lcdTotalOutput.setObjectName("lcdTotalOutput")
        self.btnPay = QtWidgets.QPushButton(Dialog)
        self.btnPay.setGeometry(QtCore.QRect(750, 550, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnPay.setFont(font)
        self.btnPay.setFlat(False)
        self.btnPay.setObjectName("btnPay")
        self.lblTotal = QtWidgets.QLabel(Dialog)
        self.lblTotal.setGeometry(QtCore.QRect(600, 500, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotal.setFont(font)
        self.lblTotal.setObjectName("lblTotal")
        self.lblLogo = QtWidgets.QLabel(Dialog)
        self.lblLogo.setGeometry(QtCore.QRect(860, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblLogo.setFont(font)
        self.lblLogo.setObjectName("lblLogo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.productsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Cant."))
        item = self.productsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.productsTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Barcode"))
        item = self.productsTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Precio U"))
        self.btnPay.setText(_translate("Dialog", "FACTURAR"))
        self.lblTotal.setText(_translate("Dialog", "Total a pagar"))
        self.lblLogo.setText(_translate("Dialog", "QuickCI"))

