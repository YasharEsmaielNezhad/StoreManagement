from Class.Model import *
from PyQt6 import QtWidgets




class SalesManagementAdd:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model()


    def renderSales(self):
        self.ui.TableWidget.setRowCount(0)
        SalesTable = self.model.restore("select ProductID, SoldBill, PurchasedBill from salesmanagement")

        for std in SalesTable:
            deletePB = QtWidgets.QPushButton()
            deletePB.setText("delete")

            editPB = QtWidgets.QPushButton()
            editPB.setText("edit")
            print(std[1])

            lastRowIndex = self.ui.TableWidget.rowCount()
            self.ui.TableWidget.insertRow(lastRowIndex)
            self.ui.TableWidget.setItem(
                lastRowIndex, 0, QtWidgets.QTableWidgetItem(str(std[1]))
            )
            self.ui.TableWidget.setItem(
                lastRowIndex, 1, QtWidgets.QTableWidgetItem(str(std[2]))
            )
           
            # self.ui.TableWidget.setCellWidget(lastRowIndex, 2, deletePB)
            # self.ui.TableWidget.setCellWidget(lastRowIndex, 3, editPB)

            # deletePB.clicked.connect(lambda *args, id=std[0]: self.deleteStd(id))
            # editPB.clicked.connect(lambda *args, stdObj=std: self.editStd(stdObj))

    def addProduct(self):
        Sold = self.ui.SaleLineEdit.text()
        Purchased = self.ui.BuyLineEdit.text()

        self.model.store(
            "insert into salesmanagement(SoldBill, PurchasedBill) values ('"
            + Sold
            + "' , '"
            + Purchased
            + "')"
        )

        self.renderSales()
        self.ui.SaleLineEdit.setText("")
        self.ui.BuyLineEdit.setText("")

    def deleteProduct(self, id):
        self.model.store("delete from ProductID where id = " + str(id))
        self.renderSales()

    def editProduct(self, std):
        self.ui.hiddenValue.setText(str(std[0]))
        self.ui.SaleLineEdit.setText(std[1])
        self.ui.BuyLineEdit.setText(std[2])

        self.ui.addPB.hide()
        self.ui.updatePB.show()

    def updateProduct(self):
        name = self.ui.SaleLineEdit.text()
        lastName = self.ui.BuyLineEdit.text()
        index = int(self.ui.hiddenValue.text())

        self.model.store(
            "update students set name= '"
            + name
            + "', lastName = '"
            + lastName
            + "' where id = "
            + str(index)
        )

        self.renderSales()
        self.ui.AddButton.show()
        self.ui.UpdatePB.hide()
        self.ui.SaleLineEdit.setText("")
        self.ui.BuyLineEdit.setText("")