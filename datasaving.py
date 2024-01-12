from PyQt6 import QtWidgets
import hashlib
from connecting import *


# ali = Ui_signInPage ()
class datasaving:
    def __init__(self, sign):
        self.sign = sign
        self.connecting = connecting()

    def exportNN(self, user, passw):
        hashpassw = hashlib.md5(passw.encode("utf-8")).hexdigest()

        self.connecting.store(
            "insert into signup(username, password) values ('"
            + str(user)
            + "' , '"
            + str(hashpassw)
            + "')"
        )

    def signup(self):
        username = self.sign.usernameLE.text()
        password = self.sign.passwordLE.text()
        reppassword = self.sign.repeatPasswordLE.text()
        print(username)
        if password == reppassword:
            self.exportNN(username, password)
        #    print(hashlib.md5(password.encode('utf-8')).hexdigest())
        else:
            print("11")
