# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTmainpage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_SALESMANAGEMENT(object):
    def setupUi(self, SALESMANAGEMENT):
        if not SALESMANAGEMENT.objectName():
            SALESMANAGEMENT.setObjectName(u"SALESMANAGEMENT")
        SALESMANAGEMENT.resize(800, 599)
        self.centralwidget = QWidget(SALESMANAGEMENT)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, -10, 800, 570))
        self.listView.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(29, 63, 78, 255));")
        self.listView_2 = QListView(self.centralwidget)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(40, 200, 200, 180))
        self.listView_2.setStyleSheet(u"background-color: rgb(143, 143, 143);")
        self.listView_3 = QListView(self.centralwidget)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(290, 200, 200, 180))
        self.listView_3.setStyleSheet(u"background-color: rgb(143, 143, 143);")
        self.listView_4 = QListView(self.centralwidget)
        self.listView_4.setObjectName(u"listView_4")
        self.listView_4.setGeometry(QRect(540, 200, 200, 180))
        self.listView_4.setStyleSheet(u"background-color: rgb(143, 143, 143);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 230, 120, 100))
        self.label.setPixmap(QPixmap(u"../for qt/icons8-product-100.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 190, 150, 180))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"../for qt/icons8-purchase-100.png"))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 220, 180, 120))
        self.label_3.setPixmap(QPixmap(u"../for qt/icons8-sales-100.png"))
        self.inventory = QPushButton(self.centralwidget)
        self.inventory.setObjectName(u"inventory")
        self.inventory.setGeometry(QRect(40, 180, 201, 20))
        self.inventory.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"background-color: rgb(93, 144, 187);")
        self.purchase = QPushButton(self.centralwidget)
        self.purchase.setObjectName(u"purchase")
        self.purchase.setGeometry(QRect(290, 180, 200, 20))
        self.purchase.setStyleSheet(u"background-color: rgb(93, 144, 187);")
        self.sales = QPushButton(self.centralwidget)
        self.sales.setObjectName(u"sales")
        self.sales.setGeometry(QRect(540, 180, 200, 20))
        self.sales.setStyleSheet(u"background-color: rgb(93, 144, 187);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 50, 520, 50))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(143, 143, 143);\n"
"font: 700 10pt \"Simplified Arabic\";")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 75, 24))
        self.back.setStyleSheet(u"background-color: rgb(143, 143, 143);")
        SALESMANAGEMENT.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SALESMANAGEMENT)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        SALESMANAGEMENT.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SALESMANAGEMENT)
        self.statusbar.setObjectName(u"statusbar")
        SALESMANAGEMENT.setStatusBar(self.statusbar)

        self.retranslateUi(SALESMANAGEMENT)

        QMetaObject.connectSlotsByName(SALESMANAGEMENT)
    # setupUi

    def retranslateUi(self, SALESMANAGEMENT):
        SALESMANAGEMENT.setWindowTitle(QCoreApplication.translate("SALESMANAGEMENT", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.inventory.setText(QCoreApplication.translate("SALESMANAGEMENT", u"inventory page", None))
        self.purchase.setText(QCoreApplication.translate("SALESMANAGEMENT", u"purchase page", None))
        self.sales.setText(QCoreApplication.translate("SALESMANAGEMENT", u"sales page", None))
        self.label_4.setText(QCoreApplication.translate("SALESMANAGEMENT", u"                                         Which page do you want to us?", None))
        self.back.setText(QCoreApplication.translate("SALESMANAGEMENT", u"Back", None))
    # retranslateUi

