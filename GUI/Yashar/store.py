# Form implementation generated from reading ui file 'store_personal_info.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(880, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow3.sizePolicy().hasHeightForWidth())
        MainWindow3.setSizePolicy(sizePolicy)
        MainWindow3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.stdTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.stdTable.setGeometry(QtCore.QRect(0, 0, 861, 441))
        self.stdTable.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.stdTable.setObjectName("stdTable")
        self.stdTable.setColumnCount(5)
        self.stdTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 460, 83, 24))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 460, 83, 24))
        self.label_2.setObjectName("label_2")
        self.nameLE = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameLE.setGeometry(QtCore.QRect(60, 460, 121, 32))
        self.nameLE.setObjectName("nameLE")
        self.lastNameLE = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lastNameLE.setGeometry(QtCore.QRect(250, 460, 191, 32))
        self.lastNameLE.setObjectName("lastNameLE")
        self.addPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addPB.setGeometry(QtCore.QRect(790, 460, 81, 33))
        self.addPB.setObjectName("addPB")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 460, 83, 24))
        self.label_3.setObjectName("label_3")
        self.lastNameLE_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lastNameLE_2.setGeometry(QtCore.QRect(470, 460, 101, 32))
        self.lastNameLE_2.setObjectName("lastNameLE_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 460, 83, 24))
        self.label_4.setObjectName("label_4")
        self.lastNameLE_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lastNameLE_3.setGeometry(QtCore.QRect(630, 460, 101, 32))
        self.lastNameLE_3.setObjectName("lastNameLE_3")
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "Student Management App"))
        item = self.stdTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow3", "name"))
        item = self.stdTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow3", "last name"))
        item = self.stdTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow3", "ID"))
        item = self.stdTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow3", "Record"))
        item = self.stdTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow3", "properties"))
        self.label.setText(_translate("MainWindow3", "name"))
        self.label_2.setText(_translate("MainWindow3", "last name"))
        self.addPB.setText(_translate("MainWindow3", "Add"))
        self.label_3.setText(_translate("MainWindow3", "ID"))
        self.label_4.setText(_translate("MainWindow3", "record"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow3.show()
    sys.exit(app.exec())
