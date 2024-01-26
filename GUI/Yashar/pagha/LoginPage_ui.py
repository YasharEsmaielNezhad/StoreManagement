# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
import qt_rc
import qtt_rc

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(371, 465)
        LoginPage.setMaximumSize(QSize(480, 620))
        icon = QIcon()
        icon.addFile(u":/newPrefix/product.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginPage.setWindowIcon(icon)
        LoginPage.setStyleSheet(u"background-color: rgb(0, 77, 113);")
        LoginPage.setIconSize(QSize(55, 55))
        self.centralwidget = QWidget(LoginPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelUn = QLabel(self.centralwidget)
        self.labelUn.setObjectName(u"labelUn")
        self.labelUn.setGeometry(QRect(140, 200, 94, 20))
        font = QFont()
        font.setFamilies([u"Imprint MT Shadow"])
        font.setPointSize(14)
        font.setBold(False)
        self.labelUn.setFont(font)
        self.labelUn.setStyleSheet(u"font-size:14pt;")
        self.labelUn.setAlignment(Qt.AlignCenter)
        self.labelPass = QLabel(self.centralwidget)
        self.labelPass.setObjectName(u"labelPass")
        self.labelPass.setGeometry(QRect(140, 257, 91, 21))
        self.labelPass.setFont(font)
        self.labelPass.setStyleSheet(u"font-size:14pt;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 60, 151, 131))
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setPixmap(QPixmap(u"../StoreManagement/Images-Icons/icons8-user-100.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.LoginButton = QCommandLinkButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(150, 310, 71, 71))
        self.LoginButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../StoreManagement/Images-Icons/icons8-login-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LoginButton.setIcon(icon1)
        self.LoginButton.setIconSize(QSize(55, 55))
        self.UnLineEdit = QLineEdit(self.centralwidget)
        self.UnLineEdit.setObjectName(u"UnLineEdit")
        self.UnLineEdit.setGeometry(QRect(60, 221, 261, 31))
        self.UnLineEdit.setStyleSheet(u"background-color: rgb(190, 190, 142);")
        self.PassLineEdit = QLineEdit(self.centralwidget)
        self.PassLineEdit.setObjectName(u"PassLineEdit")
        self.PassLineEdit.setGeometry(QRect(60, 280, 261, 31))
        self.PassLineEdit.setStyleSheet(u"background-color: rgb(190, 190, 142);")
        self.PassLineEdit.setEchoMode(QLineEdit.Password)
        self.ErrorLabel = QLabel(self.centralwidget)
        self.ErrorLabel.setObjectName(u"ErrorLabel")
        self.ErrorLabel.setGeometry(QRect(118, 40, 141, 20))
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 371, 22))
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginPage)
        self.statusbar.setObjectName(u"statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"StoreManagement", None))
        self.labelUn.setText(QCoreApplication.translate("LoginPage", u"<html><head/><body><p align=\"center\">Username</p></body></html>", None))
        self.labelPass.setText(QCoreApplication.translate("LoginPage", u"<html><head/><body><p align=\"center\">Password</p></body></html>", None))
        self.label.setText("")
        self.LoginButton.setText("")
        self.UnLineEdit.setText("")
        self.PassLineEdit.setText("")
        self.ErrorLabel.setText("")
    # retranslateUi

