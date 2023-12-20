import sys
from PyQt6 import QtWidgets
from produckt import *
from QTmainpage import *
from purchase import *
from sales import *
from SalesManagement_ui import *
from ProductManager_ui import *
from Main import *



def switchWindows(mainWin, mainWin2):
    mainWin.hide()
    mainWin2.show()
    



def switchWindows2(mainWin, mainWin3):
    mainWin.hide()
    mainWin3.show()


def switchWindows3(mainWin, mainWin4):
    mainWin.hide()
    mainWin4.show()
    


    
app = QtWidgets.QApplication(sys.argv)
mainWin = QtWidgets.QMainWindow()
mainWin2 = QtWidgets.QMainWindow()
mainWin3 = QtWidgets.QMainWindow()
mainWin4 = QtWidgets.QMainWindow()
mainWin5=QtWidgets.QMainWindow()
mainWin6=QtWidgets.QMainWindow()
mainWin7=QtWidgets.QMainWindow()







win1UI = Ui_MainWindow()
win2UI = Ui_MainWindow2()
win3UI = Ui_MainWindow3()
win4UI = Ui_MainWindow4()
win5UI=Ui_MainMenu()
win6UI=Ui_productManager()
win7UI=Ui_SalesManagement()




win1UI.setupUi(mainWin)
win2UI.setupUi(mainWin2)
win3UI.setupUi(mainWin3)
win4UI.setupUi(mainWin4)
win5UI.setupUi(mainWin5)
win6UI.setupUi(mainWin6)
win7UI.setupUi(mainWin7)


mainWin6.show()
win6UI.loginButton.clicked.connect(lambda:switchWindows(mainWin6,mainWin5))
win5UI.BackButton.clicked.connect(lambda:switchWindows(mainWin5,mainWin6))
win5UI.SmPB_2.clicked.connect(lambda:switchWindows(mainWin5,mainWin7))
win7UI.pushButton_2.clicked.connect(lambda:switchWindows(mainWin7,mainWin5))
win5UI.PmPB.clicked.connect(lambda:switchWindows(mainWin5,mainWin))
win1UI.produckt.clicked.connect(lambda:switchWindows(mainWin,mainWin2))
win1UI.sales.clicked.connect(lambda:switchWindows2(mainWin,mainWin4))
win1UI.back.clicked.connect(lambda:switchWindows2(mainWin,mainWin5))

win1UI.purchase.clicked.connect(lambda:switchWindows2(mainWin,mainWin2))
win3UI.pushButton_2.clicked.connect(lambda:switchWindows2(mainWin3,mainWin))
win4UI.pushButton_2.clicked.connect(lambda:switchWindows2(mainWin4,mainWin))
win2UI.pushButton_2.clicked.connect(lambda:switchWindows(mainWin2,mainWin))

win4UI.pushButton.clicked.connect(lambda: ui.addStd())


sys.exit(app.exec())
