# Form implementation generated from reading ui file 'store_personal_info.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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
        self.backPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backPB.setGeometry(QtCore.QRect(790, 0, 75, 24))
        self.backPB.setObjectName("backPB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Management App"))
        item = self.stdTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        item = self.stdTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "last name"))
        item = self.stdTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID"))
        item = self.stdTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Record"))
        item = self.stdTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "properties"))
        self.label.setText(_translate("MainWindow", "name"))
        self.label_2.setText(_translate("MainWindow", "last name"))
        self.addPB.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "record"))
        self.backPB.setText(_translate("MainWindow", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
