# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)
import qt_rc
import qtt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 600)
        MainWindow.setBaseSize(QSize(1920, 1080))
        icon = QIcon()
        icon.addFile(u"../StoreManagement/Images-Icons/icons8-create-order-90.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ChoosingLabel = QLabel(self.centralwidget)
        self.ChoosingLabel.setObjectName(u"ChoosingLabel")
        self.ChoosingLabel.setGeometry(QRect(40, 50, 471, 31))
        font = QFont()
        font.setFamilies([u"Georgia"])
        font.setPointSize(18)
        self.ChoosingLabel.setFont(font)
        self.ChoosingLabel.setScaledContents(True)
        self.SmPB = QCommandLinkButton(self.centralwidget)
        self.SmPB.setObjectName(u"SmPB")
        self.SmPB.setGeometry(QRect(230, 80, 111, 121))
        icon1 = QIcon()
        icon1.addFile(u"../Images-Icons/icons8-management-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SmPB.setIcon(icon1)
        self.SmPB.setIconSize(QSize(200, 200))
        self.SalesManagementLabel = QLabel(self.centralwidget)
        self.SalesManagementLabel.setObjectName(u"SalesManagementLabel")
        self.SalesManagementLabel.setGeometry(QRect(200, 190, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Mongolian Baiti"])
        self.SalesManagementLabel.setFont(font1)
        self.PmPB = QCommandLinkButton(self.centralwidget)
        self.PmPB.setObjectName(u"PmPB")
        self.PmPB.setGeometry(QRect(230, 240, 111, 121))
        icon2 = QIcon()
        icon2.addFile(u"../StoreManagement/Images-Icons/icons8-paid-bill-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PmPB.setIcon(icon2)
        self.PmPB.setIconSize(QSize(100, 100))
        self.ProductManagementLabel = QLabel(self.centralwidget)
        self.ProductManagementLabel.setObjectName(u"ProductManagementLabel")
        self.ProductManagementLabel.setGeometry(QRect(190, 350, 211, 31))
        self.ProductManagementLabel.setFont(font1)
        self.PersonnelManagementLabel = QLabel(self.centralwidget)
        self.PersonnelManagementLabel.setObjectName(u"PersonnelManagementLabel")
        self.PersonnelManagementLabel.setGeometry(QRect(180, 510, 221, 31))
        self.PersonnelManagementLabel.setFont(font1)
        self.PermPB = QCommandLinkButton(self.centralwidget)
        self.PermPB.setObjectName(u"PermPB")
        self.PermPB.setGeometry(QRect(230, 400, 111, 121))
        icon3 = QIcon()
        icon3.addFile(u"../StoreManagement/Images-Icons/icons8-management-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PermPB.setIcon(icon3)
        self.PermPB.setIconSize(QSize(100, 100))
        self.BackButton = QCommandLinkButton(self.centralwidget)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(0, 0, 61, 61))
        icon4 = QIcon()
        icon4.addFile(u"../StoreManagement/Images-Icons/icons8-back-arrow-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BackButton.setIcon(icon4)
        self.BackButton.setIconSize(QSize(43, 43))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 566, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ChoosingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#bfbf8e;\">Choose From Categories Below to Continue.</span></p></body></html>", None))
        self.SmPB.setText("")
        self.SalesManagementLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#bebe8e;\">Sales Management</span></p></body></html>", None))
        self.PmPB.setText("")
        self.ProductManagementLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#bebe8e;\">Product Management</span></p></body></html>", None))
        self.PersonnelManagementLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#bebe8e;\">Personnel Management</span></p></body></html>", None))
        self.PermPB.setText("")
        self.BackButton.setText("")
    # retranslateUi

