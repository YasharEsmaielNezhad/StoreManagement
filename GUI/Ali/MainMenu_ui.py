# Form implementation generated from reading ui file 'c:\Users\venous\Desktop\management\StoreManagement\GUI\Yashar\MainMenu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-30, -30, 621, 601))
        self.listView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.listView.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listView.setObjectName("listView")
        self.SmPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SmPB.setGeometry(QtCore.QRect(50, 160, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.SmPB.setFont(font)
        self.SmPB.setObjectName("SmPB")
        self.PmPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PmPB.setGeometry(QtCore.QRect(410, 160, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.PmPB.setFont(font)
        self.PmPB.setObjectName("PmPB")
        self.PermPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PermPB.setGeometry(QtCore.QRect(230, 160, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.PermPB.setFont(font)
        self.PermPB.setObjectName("PermPB")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label.setLineWidth(3)
        self.label.setMidLineWidth(3)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.BackButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "MainWindow"))
        self.SmPB.setText(_translate("MainMenu", "SalesManagemnt"))
        self.PmPB.setText(_translate("MainMenu", "ProductsManagement"))
        self.PermPB.setText(_translate("MainMenu", "PersonnelManagement"))
        self.label.setText(_translate("MainMenu", "MainMenu"))
        self.label_2.setText(_translate("MainMenu", "Please select from the Options Below to continue"))
        self.BackButton.setText(_translate("MainMenu", "Back"))
