# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 600)
        MainWindow.setBaseSize(QtCore.QSize(1920, 1080))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Images-Icons/icons8-create-order-90.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ChoosingLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ChoosingLabel.setGeometry(QtCore.QRect(40, 50, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.ChoosingLabel.setFont(font)
        self.ChoosingLabel.setScaledContents(True)
        self.ChoosingLabel.setObjectName("ChoosingLabel")
        self.SmPB = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.SmPB.setGeometry(QtCore.QRect(230, 80, 111, 121))
        self.SmPB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Images-Icons/icons8-management-80.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.SmPB.setIcon(icon1)
        self.SmPB.setIconSize(QtCore.QSize(200, 200))
        self.SmPB.setObjectName("SmPB")
        self.SalesManagementLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SalesManagementLabel.setGeometry(QtCore.QRect(200, 190, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        self.SalesManagementLabel.setFont(font)
        self.SalesManagementLabel.setObjectName("SalesManagementLabel")
        self.PmPB = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.PmPB.setGeometry(QtCore.QRect(230, 240, 111, 121))
        self.PmPB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Images-Icons/icons8-paid-bill-100.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PmPB.setIcon(icon2)
        self.PmPB.setIconSize(QtCore.QSize(100, 100))
        self.PmPB.setObjectName("PmPB")
        self.ProductManagementLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ProductManagementLabel.setGeometry(QtCore.QRect(190, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        self.ProductManagementLabel.setFont(font)
        self.ProductManagementLabel.setObjectName("ProductManagementLabel")
        self.PersonnelManagementLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.PersonnelManagementLabel.setGeometry(QtCore.QRect(180, 510, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        self.PersonnelManagementLabel.setFont(font)
        self.PersonnelManagementLabel.setObjectName("PersonnelManagementLabel")
        self.PermPB = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.PermPB.setGeometry(QtCore.QRect(230, 400, 111, 121))
        self.PermPB.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Images-Icons/icons8-management-100.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PermPB.setIcon(icon3)
        self.PermPB.setIconSize(QtCore.QSize(100, 100))
        self.PermPB.setObjectName("PermPB")
        self.BackButton = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.BackButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Images-Icons/icons8-back-arrow-100.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BackButton.setIcon(icon4)
        self.BackButton.setIconSize(QtCore.QSize(43, 43))
        self.BackButton.setObjectName("BackButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 22))
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
        self.ChoosingLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bfbf8e;\">Choose From Categories Below to Continue.</span></p></body></html>"))
        self.SalesManagementLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#bebe8e;\">Sales Management</span></p></body></html>"))
        self.ProductManagementLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#bebe8e;\">Product Management</span></p></body></html>"))
        self.PersonnelManagementLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#bebe8e;\">Personnel Management</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
