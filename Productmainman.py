# from PyQt6 import QtWidgets

# from manangment.hashbtest import *


# class Productmainman:
#     def __init__(self, ui):
#         self.ui = ui
#         # self.model = Model1()
#         self.renderproduckts()
        
#     def renderproduckts(self,ui):
#         self.ui.tableWidget.setRowCount(0)
#         stdList = self.model.restore("select id, name, lastName from produckts")

#         for std in stdList:
#             deletePB = QtWidgets.QPushButton()
#             deletePB.setText("delete")

#             editPB = QtWidgets.QPushButton()
#             editPB.setText("edit")

#             lastRowIndex = self.ui.tableWidget.rowCount()
#             self.ui.tableWidget.insertRow(lastRowIndex)
#             self.ui.tableWidget.setItem(
#                 lastRowIndex, 0, QtWidgets.QTableWidgetItem(std[2])
#             )
#             self.ui.tableWidget.setItem(
#                 lastRowIndex, 1, QtWidgets.QTableWidgetItem(std[3])
#             )
#             self.ui.tableWidget.setCellWidget(lastRowIndex, 2, deletePB)
#             self.ui.tableWidget.setCellWidget(lastRowIndex, 3, editPB)

#             # deletePB.clicked.connect(lambda *args, id=std[0]: self.deleteStd(id))
#             # editPB.clicked.connect(lambda *args, stdObj=std: self.editStd(stdObj))
#     def addStd(self):
#         product1 = self.ui.InvProL.text()
#         Count1 = self.ui.InvCountL.text()
#         Price1 = self.ui.InvPricL.text()

#         self.model.store(
#             "insert into students(Product, count,price) values ('"
#             + product1
#             + "' , '"
#             + Count1
#             + "' , '"
#             + Price1
#             + "')"
#         )

#         self.renderStudents()
#         self.ui.nameLE.setText("")
#         self.ui.lastNameLE.setText("")

   