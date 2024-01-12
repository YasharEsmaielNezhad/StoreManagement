import sys
from datasaving import *
from PyQt6 import QtWidgets
from pages.SalesManagement import *
from pages.LoginsignupPage import *
from pages.MainMenu import *
from pages.QTmainpage import *
from pages.ALIINVENTORY import *
from pages.ALIPURCHASE import *
from pages.ALISELES import *
from pages.signInPage import *


# from Productmainman import *
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
signuping = QtWidgets.QMainWindow()



MmWin = Ui_LoginPage()
sign = Ui_signInPage()
PmWin = Ui_MainWindow()
SmWin = Ui_SalesManagement()
Smpage = Ui_MainWindow2()
invent = Ui_INVENTORY()
sell = Ui_SELES()
purch = Ui_PURCHASE()

# INVENTORYcls = Productmainman(invent)
# sellescls = Productmainman(sell)
# purchcls = Productmainman(purch)

sign.setupUi(signuping)
invent.setupUi(INVENTORYp)
sell.setupUi(selles)
purch.setupUi(Purchasepage)
Smpage.setupUi(salesmainpage)
PmWin.setupUi(MainMenu)
MmWin.setupUi(loginPage)
SmWin.setupUi(Salesmanagemnt)

student = datasaving(sign)


loginPage.show()

MmWin.commandLinkButton.clicked.connect(lambda:switchWindows(loginPage,MainMenu))

MmWin.pushButton.clicked.connect(lambda:switchWindows(loginPage,signuping))

sign.signuppb.clicked.connect(lambda:student.signup())
sign.Backpb.clicked.connect(lambda:switchWindows(signuping,loginPage))

PmWin.PmPB.clicked.connect(lambda:switchWindows(MainMenu,salesmainpage))

Smpage.back.clicked.connect(lambda:switchWindows(salesmainpage,MainMenu))


Smpage.purchase.clicked.connect(lambda:switchWindows(salesmainpage,Purchasepage))

purch.PurBackB.clicked.connect(lambda:switchWindows(Purchasepage,salesmainpage))

Smpage.produckt.clicked.connect(lambda:switchWindows(salesmainpage,INVENTORYp))

# invent.InvAdd.clicked.connect(lambda:INVENTORYcls.)
invent.InvBackB.clicked.connect(lambda:switchWindows(INVENTORYp,salesmainpage))

Smpage.sales.clicked.connect(lambda:switchWindows(salesmainpage,selles))

sell.SalBackB.clicked.connect(lambda:switchWindows(selles,salesmainpage))

Smpage.purchase.clicked.connect(lambda:switchWindows(salesmainpage,Purchasepage))

purch.PurBackB.clicked.connect(lambda:switchWindows(Purchasepage,salesmainpage))

PmWin.SmPB.clicked.connect(lambda:switchWindows(MainMenu,Salesmanagemnt))
SmWin.BackButton.clicked.connect(lambda:switchWindows(Salesmanagemnt,MainMenu))
PmWin.BackButton.clicked.connect(lambda:switchWindows(MainMenu,loginPage))


sys.exit(app.exec())
