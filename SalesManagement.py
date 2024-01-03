# Form implementation generated from reading ui file 'SalesManagement.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SalesManagement(object):
    def setupUi(self, SalesManagement):
        SalesManagement.setObjectName("SalesManagement")
        SalesManagement.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=SalesManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-20, -20, 621, 661))
        self.listView.setMaximumSize(QtCore.QSize(1920, 1080))
        self.listView.setStyleSheet("background-color: rgb(62, 62, 62);")
        self.listView.setAlternatingRowColors(True)
        self.listView.setObjectName("listView")
        self.TableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.TableWidget.setGeometry(QtCore.QRect(10, 50, 561, 330))
        self.TableWidget.setMinimumSize(QtCore.QSize(561, 0))
        self.TableWidget.setStyleSheet("background-color: rgb(0, 74, 109);\n"
"background-color: rgb(0, 120, 175);")
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(4)
        self.TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(10)
        item.setFont(font)
        icon = QtGui.QIcon.fromTheme("applications-games")
        item.setIcon(icon)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(10)
        item.setFont(font)
        self.TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(10)
        item.setFont(font)
        self.TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(10)
        item.setFont(font)
        self.TableWidget.setHorizontalHeaderItem(3, item)
        self.SaleLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SaleLineEdit.setGeometry(QtCore.QRect(100, 420, 170, 30))
        self.SaleLineEdit.setStyleSheet("background-color: rgb(252, 252, 188);\n"
"background-color: rgb(203, 203, 151);")
        self.SaleLineEdit.setObjectName("SaleLineEdit")
        self.SaleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SaleLabel.setGeometry(QtCore.QRect(100, 390, 71, 31))
        self.SaleLabel.setObjectName("SaleLabel")
        self.BuyLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.BuyLabel.setGeometry(QtCore.QRect(280, 390, 91, 31))
        self.BuyLabel.setObjectName("BuyLabel")
        self.SmLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SmLabel.setGeometry(QtCore.QRect(160, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(22)
        self.SmLabel.setFont(font)
        self.SmLabel.setStyleSheet("background-color: rgb(62, 62, 62);")
        self.SmLabel.setScaledContents(True)
        self.SmLabel.setObjectName("SmLabel")
        self.BuyLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.BuyLineEdit.setGeometry(QtCore.QRect(280, 420, 170, 30))
        self.BuyLineEdit.setStyleSheet("background-color: rgb(195, 195, 145);")
        self.BuyLineEdit.setObjectName("BuyLineEdit")
        self.AddButton = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.AddButton.setEnabled(True)
        self.AddButton.setGeometry(QtCore.QRect(445, 405, 51, 51))
        self.AddButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images-Icons/icons8-add-60.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setIconSize(QtCore.QSize(40, 40))
        self.AddButton.setObjectName("AddButton")
        self.BackButton = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.BackButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../StoreManagement/Images-Icons/icons8-back-arrow-100.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setIconSize(QtCore.QSize(35, 35))
        self.BackButton.setObjectName("BackButton")
        SalesManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SalesManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SalesManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SalesManagement)
        self.statusbar.setObjectName("statusbar")
        SalesManagement.setStatusBar(self.statusbar)

        self.retranslateUi(SalesManagement)
        QtCore.QMetaObject.connectSlotsByName(SalesManagement)

    def retranslateUi(self, SalesManagement):
        _translate = QtCore.QCoreApplication.translate
        SalesManagement.setWindowTitle(_translate("SalesManagement", "MainWindow"))
        item = self.TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SalesManagement", "SoldBill"))
        item = self.TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SalesManagement", "BoughtBill"))
        item = self.TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SalesManagement", "Update"))
        item = self.TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SalesManagement", "Delete"))
        self.SaleLabel.setText(_translate("SalesManagement", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">SoldBill</span></p></body></html>"))
        self.BuyLabel.setText(_translate("SalesManagement", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">BoughtBill</span></p></body></html>"))
        self.SmLabel.setText(_translate("SalesManagement", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#e2e2a8;\">Sales Management</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SalesManagement = QtWidgets.QMainWindow()
    ui = Ui_SalesManagement()
    ui.setupUi(SalesManagement)
    SalesManagement.show()
    sys.exit(app.exec())
