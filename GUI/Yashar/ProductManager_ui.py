# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductManager.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_productManager(object):
    def setupUi(self, productManager):
        if not productManager.objectName():
            productManager.setObjectName(u"productManager")
        productManager.resize(800, 600)
        self.centralwidget = QWidget(productManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginLabel = QLabel(self.centralwidget)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(120, 30, 381, 101))
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(16)
        self.loginLabel.setFont(font)
        self.loginLabel.setFrameShape(QFrame.WinPanel)
        self.loginLabel.setFrameShadow(QFrame.Plain)
        self.loginLabel.setLineWidth(3)
        self.loginLabel.setMidLineWidth(2)
        self.loginLabel.setTextFormat(Qt.MarkdownText)
        self.loginLabel.setScaledContents(False)
        self.loginLabel.setWordWrap(False)
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(180, 330, 75, 24))
        self.unBox = QTextEdit(self.centralwidget)
        self.unBox.setObjectName(u"unBox")
        self.unBox.setGeometry(QRect(10, 200, 251, 51))
        self.passBox = QTextEdit(self.centralwidget)
        self.passBox.setObjectName(u"passBox")
        self.passBox.setGeometry(QRect(10, 270, 251, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 180, 80, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 250, 49, 16))
        productManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(productManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        productManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(productManager)
        self.statusbar.setObjectName(u"statusbar")
        productManager.setStatusBar(self.statusbar)

        self.retranslateUi(productManager)

        QMetaObject.connectSlotsByName(productManager)
    # setupUi

    def retranslateUi(self, productManager):
        productManager.setWindowTitle(QCoreApplication.translate("productManager", u"MainWindow", None))
        self.loginLabel.setText(QCoreApplication.translate("productManager", u"Please Log in to your Account", None))
        self.loginButton.setText(QCoreApplication.translate("productManager", u"Log in", None))
        self.unBox.setHtml(QCoreApplication.translate("productManager", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.passBox.setHtml(QCoreApplication.translate("productManager", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("productManager", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("productManager", u"Password", None))
    # retranslateUi

