import sys
from PyQt6 import QtWidgets
from pagha.SalesManagement import *
from pagha.LoginPage import *
from pagha.MainMenu import *
from pagha.QTmainpage import *
from pagha.ALIINVENTORY import *
from pagha.ALIPURCHASE import *
from pagha.ALISELES import *
from pagha.SalesManagementAdd import *
from Class.Login import *
from storePersonalInfo import *

    

def switchWindows(mainWin, mainWin2):
    mainWin.hide()
    mainWin2.show()

def switchWindows1(mainWin, mainWin2):
    mainWin.hide()
    mainWin2.show()

def switchSMPWindows(MainMenu,Salesmanagemnt,SalesManagementAdd):
    switchWindows(MainMenu,Salesmanagemnt)
    SalesManagementAdd.renderSales()



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
store_personal_info = QtWidgets.QMainWindow()


MmWin = Ui_LoginPage()
PmWin = Ui_MainWindow()
SmWin = Ui_SalesManagement()
Smpage = Ui_MainWindow2()
invent = Ui_INVENTORY()
sell = Ui_SELES()
purch = Ui_PURCHASE()
PerM = Ui_MainWindow3()

invent.setupUi(INVENTORYp)
sell.setupUi(selles)
purch.setupUi(Purchasepage)
Smpage.setupUi(salesmainpage)
PmWin.setupUi(MainMenu)
MmWin.setupUi(loginPage)
SmWin.setupUi(Salesmanagemnt)
PerM.setupUi(store_personal_info)


loginObj=Login(MmWin)
AddObj=SalesManagementAdd(SmWin)

loginPage.show()

MmWin.LoginButton.clicked.connect(lambda:loginObj.doLogin(loginPage,MainMenu,PmWin))

PmWin.PermPB.clicked.connect(lambda:switchWindows(MainMenu,store_personal_info))
PmWin.PmPB.clicked.connect(lambda:switchWindows(MainMenu,salesmainpage))

Smpage.back.clicked.connect(lambda:switchWindows(salesmainpage,MainMenu))
PerM.backPB.clicked.connect(lambda:switchWindows(store_personal_info,MainMenu))


Smpage.purchase.clicked.connect(lambda:switchWindows(salesmainpage,Purchasepage))

purch.PurBackB.clicked.connect(lambda:switchWindows(Purchasepage,salesmainpage))

Smpage.produckt.clicked.connect(lambda:switchWindows(salesmainpage,INVENTORYp))

invent.InvBackB.clicked.connect(lambda:switchWindows(INVENTORYp,salesmainpage))

Smpage.sales.clicked.connect(lambda:switchWindows(salesmainpage,selles))

sell.SalBackB.clicked.connect(lambda:switchWindows(selles,salesmainpage))

Smpage.purchase.clicked.connect(lambda:switchWindows(salesmainpage,Purchasepage))

purch.PurBackB.clicked.connect(lambda:switchWindows(Purchasepage,salesmainpage))

PmWin.SmPB.clicked.connect(lambda:switchSMPWindows(MainMenu,Salesmanagemnt,AddObj))
SmWin.BackButton.clicked.connect(lambda:switchWindows(Salesmanagemnt,MainMenu))
SmWin.AddButton.clicked.connect(lambda:AddObj.addProduct())
SmWin.UpdatePB.clicked.connect(lambda:AddObj.updateProduct())
PmWin.BackButton.clicked.connect(lambda:switchWindows(MainMenu,loginPage))


sys.exit(app.exec())
