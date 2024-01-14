# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ALI INVENTORY.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_INVENTORY(object):
    def setupUi(self, INVENTORY):
        if not INVENTORY.objectName():
            INVENTORY.setObjectName(u"INVENTORY")
        INVENTORY.resize(800, 597)
        self.centralwidget = QWidget(INVENTORY)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 0, 771, 531))
        self.listView.setStyleSheet(u"background-color: rgb(38, 49, 56);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 0, 110, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.InvAdd = QPushButton(self.centralwidget)
        self.InvAdd.setObjectName(u"InvAdd")
        self.InvAdd.setGeometry(QRect(660, 490, 75, 24))
        self.InvAdd.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.InvProL = QLineEdit(self.centralwidget)
        self.InvProL.setObjectName(u"InvProL")
        self.InvProL.setGeometry(QRect(90, 490, 140, 30))
        self.InvProL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.InvCountL = QLineEdit(self.centralwidget)
        self.InvCountL.setObjectName(u"InvCountL")
        self.InvCountL.setGeometry(QRect(280, 490, 140, 30))
        self.InvCountL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.InvPricL = QLineEdit(self.centralwidget)
        self.InvPricL.setObjectName(u"InvPricL")
        self.InvPricL.setGeometry(QRect(480, 490, 140, 30))
        self.InvPricL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 470, 49, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 470, 49, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 460, 40, 30))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(140, 60, 510, 260))
        self.tableWidget.setStyleSheet(u"background-color: rgb(134, 135, 132);")
        self.InvBackB = QPushButton(self.centralwidget)
        self.InvBackB.setObjectName(u"InvBackB")
        self.InvBackB.setGeometry(QRect(20, 0, 40, 20))
        INVENTORY.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(INVENTORY)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        INVENTORY.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(INVENTORY)
        self.statusbar.setObjectName(u"statusbar")
        INVENTORY.setStatusBar(self.statusbar)

        self.retranslateUi(INVENTORY)

        QMetaObject.connectSlotsByName(INVENTORY)
    # setupUi

    def retranslateUi(self, INVENTORY):
        INVENTORY.setWindowTitle(QCoreApplication.translate("INVENTORY", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("INVENTORY", u"Inventory Page", None))
        self.InvAdd.setText(QCoreApplication.translate("INVENTORY", u"ADD", None))
        self.InvProL.setText("")
        self.label_2.setText(QCoreApplication.translate("INVENTORY", u"product", None))
        self.label_3.setText(QCoreApplication.translate("INVENTORY", u"count", None))
        self.label_4.setText(QCoreApplication.translate("INVENTORY", u"price", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("INVENTORY", u"product", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("INVENTORY", u"count", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("INVENTORY", u"price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("INVENTORY", u"update", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("INVENTORY", u"delete", None));
        self.InvBackB.setText(QCoreApplication.translate("INVENTORY", u"back", None))
    # retranslateUi

