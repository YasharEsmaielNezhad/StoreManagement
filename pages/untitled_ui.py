# Form implementation generated from reading ui file 'c:\Users\venous\Desktop\for qt\StoreManagement\pages\untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(209, 151)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 20, 181, 81))
        self.listView.setMinimumSize(QtCore.QSize(20, 55))
        self.listView.setMaximumSize(QtCore.QSize(181, 81))
        self.listView.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 121, 16))
        self.label.setMaximumSize(QtCore.QSize(121, 16))
        self.label.setObjectName("label")
        self.OKpb = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OKpb.setGeometry(QtCore.QRect(120, 70, 75, 24))
        self.OKpb.setMaximumSize(QtCore.QSize(75, 24))
        self.OKpb.setObjectName("OKpb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "password is not  True"))
        self.OKpb.setText(_translate("MainWindow", "OK"))
