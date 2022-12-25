import mysql.connector as db


class DataBaseHelper:

    def _init_(self, database='customerapp'):
        self.connection = db.connect(user='root', password='Mehmeet#2407!@',
                                     host='127.0.0.1',
                                     database=database)
        print("1. DB CONNECTED :)")
        self.cursor = self.connection.cursor()
        print("2. CURSOR CREATED :)")

    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("SQL QUERY EXECUTED :)")

    def read(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall() # list of Tuples :)
        return rows