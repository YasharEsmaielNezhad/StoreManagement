import sys
from PyQt6 import QtWidgets
from SalesManagement import *
from LoginPage import *
from MainMenu import *
from QTmainpage import *
from ALIINVENTORY import *
from ALIPURCHASE import *
from ALISELES import *



    

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
salesmainpage = QtWidgets.QMainWindow()
INVENTORYp = QtWidgets.QMainWindow()
selles = QtWidgets.QMainWindow()
Purchasepage = QtWidgets.QMainWindow()
salesmainpage = QtWidgets.QMainWindow()



MmWin = Ui_LoginPage()
PmWin = Ui_MainWindow()
SmWin = Ui_SalesManagement()
Smpage = Ui_MainWindow2()
invent = Ui_INVENTORY()
sell = Ui_SELES()
purch = Ui_PURCHASE()

invent.setupUi(INVENTORYp)
sell.setupUi(selles)
purch.setupUi(Purchasepage)
Smpage.setupUi(salesmainpage)
PmWin.setupUi(MainMenu)
MmWin.setupUi(loginPage)
SmWin.setupUi(Salesmanagemnt)

loginPage.show()

MmWin.commandLinkButton.clicked.connect(lambda:switchWindows(loginPage,MainMenu))
PmWin.PmPB.clicked.connect(lambda:switchWindows(MainMenu,salesmainpage))

Smpage.back.clicked.connect(lambda:switchWindows(salesmainpage,MainMenu))


Smpage.purchase.clicked.connect(lambda:switchWindows(salesmainpage,Purchasepage))

purch.PurBackB.clicked.connect(lambda:switchWindows(Purchasepage,salesmainpage))

Smpage.produckt.clicked.connect(lambda:switchWindows(salesmainpage,INVENTORYp))

invent.InvBackB.clicked.connect(lambda:switchWindows(INVENTORYp,salesmainpage))

Smpage.sales.clicked.connect(lambda:switchWindows(salesmainpage,selles))

sell.SalBackB.clicked.connect(lambda:switchWindows(selles,salesmainpage))

Smpage.purchase.clicked.connect(lambda:switchWindows(salesmainpage,Purchasepage))

purch.PurBackB.clicked.connect(lambda:switchWindows(Purchasepage,salesmainpage))

PmWin.SmPB.clicked.connect(lambda:switchWindows(MainMenu,Salesmanagemnt))
SmWin.BackButton.clicked.connect(lambda:switchWindows(Salesmanagemnt,MainMenu))
PmWin.BackButton.clicked.connect(lambda:switchWindows(MainMenu,loginPage))


sys.exit(app.exec())
