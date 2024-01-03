import sys
from PyQt6 import QtWidgets
from pyqt6_tools import *
from pyqt6_plugins import *
from SalesManagement import *
from LoginPage import *
from MainMenu import *


def switchWindows(mainWin, mainWin2):
    mainWin.hide()
    mainWin2.show()

def switchWindows1(mainWin, mainWin2):
    mainWin.hide()
    mainWin2.show()



app = QtWidgets.QApplication(sys.argv)
UnBox = QtWidgets.QTextEdit()
passBox = QtWidgets.QTextEdit()
Salesmanagemnt = QtWidgets.QMainWindow()
MainMenu = QtWidgets.QMainWindow()
loginPage = QtWidgets.QMainWindow()
MmWin = Ui_LoginPage()
PmWin = Ui_MainWindow()
SmWin = Ui_SalesManagement()



PmWin.setupUi(MainMenu)
MmWin.setupUi(loginPage)
SmWin.setupUi(Salesmanagemnt)

loginPage.show()


            
MmWin.LoginButton.clicked.connect(lambda:switchWindows(loginPage,MainMenu))
PmWin.SmPB.clicked.connect(lambda:switchWindows(MainMenu,Salesmanagemnt))
SmWin.BackButton.clicked.connect(lambda:switchWindows(Salesmanagemnt,MainMenu))
PmWin.BackButton.clicked.connect(lambda:switchWindows(MainMenu,loginPage))


sys.exit(app.exec())
