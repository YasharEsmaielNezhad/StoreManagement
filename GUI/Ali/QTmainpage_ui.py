# Form implementation generated from reading ui file 'c:\Users\venous\Desktop\management\QTmainpage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, -10, 800, 570))
        self.listView.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(29, 63, 78, 255));")
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(40, 200, 200, 180))
        self.listView_2.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(290, 200, 200, 180))
        self.listView_3.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.listView_3.setObjectName("listView_3")
        self.listView_4 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_4.setGeometry(QtCore.QRect(540, 200, 200, 180))
        self.listView_4.setStyleSheet("background-color: rgb(143, 143, 143);\n"
"")
        self.listView_4.setObjectName("listView_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 240, 120, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\venous\\Desktop\\management\\../for qt/icons8-product-100.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 190, 150, 180))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\venous\\Desktop\\management\\../for qt/icons8-purchase-100.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 220, 180, 120))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\venous\\Desktop\\management\\../for qt/icons8-sales-100.png"))
        self.label_3.setObjectName("label_3")
        self.produckt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.produckt.setGeometry(QtCore.QRect(40, 180, 201, 20))
        self.produckt.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(93, 144, 187);")
        self.produckt.setObjectName("produckt")
        self.purchase = QtWidgets.QPushButton(parent=self.centralwidget)
        self.purchase.setGeometry(QtCore.QRect(290, 180, 200, 20))
        self.purchase.setStyleSheet("background-color: rgb(93, 144, 187);")
        self.purchase.setObjectName("purchase")
        self.sales = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sales.setGeometry(QtCore.QRect(540, 180, 200, 20))
        self.sales.setStyleSheet("background-color: rgb(93, 144, 187);")
        self.sales.setObjectName("sales")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 50, 520, 50))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(143, 143, 143);\n"
"font: 700 10pt \"Simplified Arabic\";")
        self.label_4.setObjectName("label_4")
        self.back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 0, 75, 24))
        self.back.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.produckt.setText(_translate("MainWindow", "produckt page"))
        self.purchase.setText(_translate("MainWindow", "purchase page"))
        self.sales.setText(_translate("MainWindow", "sales page"))
        self.label_4.setText(_translate("MainWindow", "                                         Which page do you want to us?"))
        self.back.setText(_translate("MainWindow", "Back"))
