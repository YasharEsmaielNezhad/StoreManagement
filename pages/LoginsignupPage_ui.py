# Form implementation generated from reading ui file 'c:\Users\venous\Desktop\for qt\StoreManagement\pages\LoginsignupPage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(371, 465)
        LoginPage.setMaximumSize(QtCore.QSize(480, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/product.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LoginPage.setWindowIcon(icon)
        LoginPage.setStyleSheet("background-color: rgb(0, 77, 113);")
        LoginPage.setIconSize(QtCore.QSize(55, 55))
        self.centralwidget = QtWidgets.QWidget(parent=LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.UnBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.UnBox.setGeometry(QtCore.QRect(60, 210, 260, 30))
        self.UnBox.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 127);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);")
        self.UnBox.setObjectName("UnBox")
        self.passBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.passBox.setGeometry(QtCore.QRect(60, 280, 260, 30))
        self.passBox.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.passBox.setObjectName("passBox")
        self.labelUn = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelUn.setGeometry(QtCore.QRect(140, 189, 94, 20))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        font.setBold(False)
        self.labelUn.setFont(font)
        self.labelUn.setStyleSheet("font-size:14pt;")
        self.labelUn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelUn.setObjectName("labelUn")
        self.labelPass = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelPass.setGeometry(QtCore.QRect(140, 257, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        font.setBold(False)
        self.labelPass.setFont(font)
        self.labelPass.setStyleSheet("font-size:14pt;")
        self.labelPass.setObjectName("labelPass")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 151, 131))
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\venous\\Desktop\\for qt\\StoreManagement\\pages\\../StoreManagement/Images-Icons/icons8-user-100.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(150, 310, 71, 71))
        self.commandLinkButton.setStyleSheet("")
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\venous\\Desktop\\for qt\\StoreManagement\\pages\\../StoreManagement/Images-Icons/icons8-login-100.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(55, 55))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 320, 75, 24))
        self.pushButton.setObjectName("pushButton")
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 22))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "StoreManagement"))
        self.UnBox.setHtml(_translate("LoginPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.passBox.setHtml(_translate("LoginPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labelUn.setText(_translate("LoginPage", "<html><head/><body><p align=\"center\">Username</p></body></html>"))
        self.labelPass.setText(_translate("LoginPage", "<html><head/><body><p align=\"center\">Password</p></body></html>"))
        self.pushButton.setText(_translate("LoginPage", "sign up"))
