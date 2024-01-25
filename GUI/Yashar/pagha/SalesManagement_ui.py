# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SalesManagement.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCommandLinkButton, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)
import qtt_rc

class Ui_SalesManagement(object):
    def setupUi(self, SalesManagement):
        if not SalesManagement.objectName():
            SalesManagement.setObjectName(u"SalesManagement")
        SalesManagement.resize(583, 600)
        self.centralwidget = QWidget(SalesManagement)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(-20, -20, 621, 661))
        self.listView.setMaximumSize(QSize(1920, 1080))
        self.listView.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.listView.setAlternatingRowColors(True)
        self.TableWidget = QTableWidget(self.centralwidget)
        if (self.TableWidget.columnCount() < 4):
            self.TableWidget.setColumnCount(4)
        icon = QIcon()
        iconThemeName = u"applications-games"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        font = QFont()
        font.setFamilies([u"Imprint MT Shadow"])
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setIcon(icon);
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setGeometry(QRect(10, 60, 561, 321))
        self.TableWidget.setMinimumSize(QSize(561, 0))
        self.TableWidget.setLayoutDirection(Qt.LeftToRight)
        self.TableWidget.setAutoFillBackground(True)
        self.TableWidget.setStyleSheet(u"background-color: rgb(182, 182, 136);\n"
"background-color: rgb(148, 148, 148);")
        self.TableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.TableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.TableWidget.setAutoScroll(True)
        self.TableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.TableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)
        self.TableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.TableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.TableWidget.verticalHeader().setStretchLastSection(True)
        self.SaleLineEdit = QLineEdit(self.centralwidget)
        self.SaleLineEdit.setObjectName(u"SaleLineEdit")
        self.SaleLineEdit.setGeometry(QRect(100, 420, 170, 30))
        self.SaleLineEdit.setStyleSheet(u"background-color: rgb(252, 252, 188);\n"
"background-color: rgb(203, 203, 151);")
        self.SaleLabel = QLabel(self.centralwidget)
        self.SaleLabel.setObjectName(u"SaleLabel")
        self.SaleLabel.setGeometry(QRect(100, 390, 71, 31))
        self.BuyLabel = QLabel(self.centralwidget)
        self.BuyLabel.setObjectName(u"BuyLabel")
        self.BuyLabel.setGeometry(QRect(280, 390, 91, 31))
        self.SmLabel = QLabel(self.centralwidget)
        self.SmLabel.setObjectName(u"SmLabel")
        self.SmLabel.setGeometry(QRect(160, 10, 261, 41))
        font1 = QFont()
        font1.setFamilies([u"Imprint MT Shadow"])
        font1.setPointSize(22)
        self.SmLabel.setFont(font1)
        self.SmLabel.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.SmLabel.setScaledContents(True)
        self.BuyLineEdit = QLineEdit(self.centralwidget)
        self.BuyLineEdit.setObjectName(u"BuyLineEdit")
        self.BuyLineEdit.setGeometry(QRect(280, 420, 170, 30))
        self.BuyLineEdit.setStyleSheet(u"background-color: rgb(195, 195, 145);")
        self.AddButton = QCommandLinkButton(self.centralwidget)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setEnabled(True)
        self.AddButton.setGeometry(QRect(445, 405, 51, 51))
        icon1 = QIcon()
        icon1.addFile(u"../Images-Icons/icons8-add-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setIconSize(QSize(40, 40))
        self.BackButton = QCommandLinkButton(self.centralwidget)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(10, 0, 51, 51))
        icon2 = QIcon()
        icon2.addFile(u"../StoreManagement/Images-Icons/icons8-back-arrow-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BackButton.setIcon(icon2)
        self.BackButton.setIconSize(QSize(35, 35))
        self.UpdatePB = QPushButton(self.centralwidget)
        self.UpdatePB.setObjectName(u"UpdatePB")
        self.UpdatePB.setGeometry(QRect(379, 450, 71, 24))
        self.UpdatePB.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 600 10pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-radius:20px;")
        self.HiddenVal = QLabel(self.centralwidget)
        self.HiddenVal.setObjectName(u"HiddenVal")
        self.HiddenVal.setGeometry(QRect(340, 150, 49, 16))
        SalesManagement.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.SaleLineEdit.raise_()
        self.SaleLabel.raise_()
        self.BuyLabel.raise_()
        self.SmLabel.raise_()
        self.BuyLineEdit.raise_()
        self.AddButton.raise_()
        self.BackButton.raise_()
        self.UpdatePB.raise_()
        self.HiddenVal.raise_()
        self.TableWidget.raise_()
        self.menubar = QMenuBar(SalesManagement)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 583, 22))
        SalesManagement.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SalesManagement)
        self.statusbar.setObjectName(u"statusbar")
        SalesManagement.setStatusBar(self.statusbar)

        self.retranslateUi(SalesManagement)

        QMetaObject.connectSlotsByName(SalesManagement)
    # setupUi

    def retranslateUi(self, SalesManagement):
        SalesManagement.setWindowTitle(QCoreApplication.translate("SalesManagement", u"MainWindow", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SalesManagement", u"SoldBill", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SalesManagement", u"PurchasedBill", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SalesManagement", u"Update", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SalesManagement", u"Delete", None));
        self.SaleLabel.setText(QCoreApplication.translate("SalesManagement", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">SoldBill</span></p></body></html>", None))
        self.BuyLabel.setText(QCoreApplication.translate("SalesManagement", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">BoughtBill</span></p></body></html>", None))
        self.SmLabel.setText(QCoreApplication.translate("SalesManagement", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#e2e2a8;\">Sales Management</span></p></body></html>", None))
        self.AddButton.setText("")
        self.BackButton.setText("")
        self.UpdatePB.setText(QCoreApplication.translate("SalesManagement", u"Update", None))
        self.HiddenVal.setText(QCoreApplication.translate("SalesManagement", u"TextLabel", None))
    # retranslateUi

