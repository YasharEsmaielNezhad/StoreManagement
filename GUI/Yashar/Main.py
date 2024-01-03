# Form implementation generated from reading ui file 'c:\Users\CFP\Desktop\Coding\Project\StoreManagement\MainMenu.ui'
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
        self.listView.setGeometry(QtCore.QRect(10, -40, 621, 601))
        self.listView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"background-color: rgb(0, 74, 109);")
        self.listView.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.listView.setObjectName("listView")
        self.SmPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SmPB.setGeometry(QtCore.QRect(50, 150, 221, 171))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(True)
        self.SmPB.setFont(font)
        self.SmPB.setAutoFillBackground(False)
        self.SmPB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SmPB.setText("")
        icon = QtGui.QIcon.fromTheme("applications-games")
        self.SmPB.setIcon(icon)
        self.SmPB.setObjectName("SmPB")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 170, 127);")
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
        self.label_2.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_2.setObjectName("label_2")
        self.BackButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.BackButton.setFont(font)
        self.BackButton.setStyleSheet("background-color: rgb(184, 0, 0);\n"
"background-color: rgb(170, 170, 127);")
        self.BackButton.setObjectName("BackButton")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 210, 141, 121))
        self.label_5.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./Images-Icons/product.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.PmPB = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.PmPB.setGeometry(QtCore.QRect(310, 180, 211, 151))
        self.PmPB.setStyleSheet("alternate-background-color: rgb(170, 170, 127);")
        self.PmPB.setObjectName("PmPB")
        self.SmIconLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SmIconLabel.setGeometry(QtCore.QRect(90, 220, 101, 111))
        self.SmIconLabel.setScaledContents(True)
        self.SmIconLabel.setObjectName("SmIconLabel")
        self.SmPB_2 = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.SmPB_2.setGeometry(QtCore.QRect(70, 180, 211, 181))
        self.SmPB_2.setObjectName("SmPB_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 360, 101, 131))
        self.label_3.setObjectName("label_3")
        self.PermPB = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.PermPB.setGeometry(QtCore.QRect(190, 340, 201, 161))
        self.PermPB.setObjectName("PermPB")
        self.SmPB.raise_()
        self.listView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.BackButton.raise_()
        self.label_5.raise_()
        self.PmPB.raise_()
        self.SmIconLabel.raise_()
        self.SmPB_2.raise_()
        self.label_3.raise_()
        self.PermPB.raise_()
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
        MainMenu.setWindowTitle(_translate("MainMenu", "MainMenu"))
        self.label.setText(_translate("MainMenu", "MainMenu"))
        self.label_2.setText(_translate("MainMenu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:700; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00557f;\">Please select from the Options Below to continue!!</span></p></body></html>"))
        self.BackButton.setText(_translate("MainMenu", "Back"))
        self.PmPB.setText(_translate("MainMenu", "ProductManagement"))
        self.SmIconLabel.setText(_translate("MainMenu", "<html><head/><body><p><img src=\":/newPrefix/Project/Images-Icons/icons8-management-80.png\"/></p></body></html>"))
        self.SmPB_2.setText(_translate("MainMenu", "SalesManagement"))
        self.label_3.setText(_translate("MainMenu", "<html><head/><body><p><img src=\":/newPrefix/icons8-team-100.png\"/></p></body></html>"))
        self.PermPB.setText(_translate("MainMenu", "PersonnelManagement"))
