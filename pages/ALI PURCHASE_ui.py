# Form implementation generated from reading ui file 'c:\Users\venous\Desktop\for qt\StoreManagement\pages\ALI PURCHASE.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PURCHASE(object):
    def setupUi(self, PURCHASE):
        PURCHASE.setObjectName("PURCHASE")
        PURCHASE.resize(800, 597)
        self.centralwidget = QtWidgets.QWidget(parent=PURCHASE)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 0, 771, 531))
        self.listView.setStyleSheet("background-color: rgb(38, 49, 56);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 110, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.PurAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PurAdd.setGeometry(QtCore.QRect(660, 490, 75, 24))
        self.PurAdd.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.PurAdd.setObjectName("PurAdd")
        self.PurProL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PurProL.setGeometry(QtCore.QRect(90, 490, 140, 30))
        self.PurProL.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.PurProL.setText("")
        self.PurProL.setObjectName("PurProL")
        self.PurCountL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PurCountL.setGeometry(QtCore.QRect(280, 490, 140, 30))
        self.PurCountL.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.PurCountL.setObjectName("PurCountL")
        self.PurPricL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PurPricL.setGeometry(QtCore.QRect(480, 490, 140, 30))
        self.PurPricL.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.PurPricL.setObjectName("PurPricL")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 470, 49, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 470, 49, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 460, 40, 30))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 60, 510, 260))
        self.tableWidget.setStyleSheet("background-color: rgb(134, 135, 132);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.PurBackB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PurBackB.setGeometry(QtCore.QRect(20, 0, 40, 20))
        self.PurBackB.setObjectName("PurBackB")
        PURCHASE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=PURCHASE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        PURCHASE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=PURCHASE)
        self.statusbar.setObjectName("statusbar")
        PURCHASE.setStatusBar(self.statusbar)

        self.retranslateUi(PURCHASE)
        QtCore.QMetaObject.connectSlotsByName(PURCHASE)

    def retranslateUi(self, PURCHASE):
        _translate = QtCore.QCoreApplication.translate
        PURCHASE.setWindowTitle(_translate("PURCHASE", "MainWindow"))
        self.label.setText(_translate("PURCHASE", "Purchase page"))
        self.PurAdd.setText(_translate("PURCHASE", "ADD"))
        self.label_2.setText(_translate("PURCHASE", "product"))
        self.label_3.setText(_translate("PURCHASE", "count"))
        self.label_4.setText(_translate("PURCHASE", "price"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PURCHASE", "product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PURCHASE", "count"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PURCHASE", "price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PURCHASE", "update"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PURCHASE", "delete"))
        self.PurBackB.setText(_translate("PURCHASE", "back"))
