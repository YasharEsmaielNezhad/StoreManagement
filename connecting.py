import mysql.connector


class connecting:
    def __init__(self):
        self.emp = mysql.connector.connect(
            host="localhost", user="root", password="", database="emp"
        )
        self.myCursor = self.emp.cursor()

    def restore(self, query):
        self.myCursor.execute(query)
        return self.myCursor.fetchall()

    def store(self, query):
        self.myCursor.execute(query)
        self.emp.commit()
