from Class.Model import *
from PyQt6 import QtWidgets
import hashlib


class Login:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model()
        self.messageBox = None

    def fetchUserInfo(self, username):
        return self.model.restore(
            "SELECT * FROM login WHERE  username ='" + username + "'"
        )

    def doLogin(self, loginForm, homeForm, homeUI):
        self.ui.ErrorLabel.setText("")
        userInfo = self.fetchUserInfo(self.ui.UnLineEdit.text())
        if userInfo.__len__() == 1:
            if self.getPassHash(self.ui.PassLineEdit.text()) == userInfo[0][2]:
                loginForm.hide()
                homeForm.show()
            else:
                self.ui.ErrorLabel.setText("* wrong username or password!")
        else:
            self.ui.ErrorLabel.setText("* wrong username or password!")
            self.ui.PassLineEdit.setText("")

    def getPassHash(self, password):
        return hashlib.md5(bytes(password, "ascii")).hexdigest()
