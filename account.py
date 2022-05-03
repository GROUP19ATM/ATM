from multiprocessing import connection
from prettytable import PrettyTable
import mysql.connector
from mysql.connector import Error


class ACCOUNT:
    def __init__(self,accountNumber):
        self.accountNumber = accountNumber
 
    def fetchPIN(self):
        print(self.accountNumber)
        try:
            db = mysql.connector.connect(
            host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user = 'uhhcevmfsdoh3b14',
            password = 'iI4zqX9mPaJHPKmFyjhp',
            database = 'byhmrkozld7aa4b3kupq'
        )
            cursor = db.cursor()
            cursor.execute(f"SELECT pin FROM PIN WHERE accountNumber = '{self.accountNumber}'")
            records = cursor.fetchall()
            print(records)
            return records[0][0]        

        except mysql.connector.Error as error:
            print("Failed to fetch PIN : {}".format(error))

# print(fetchPIN(987987987))

    def updatePIN(self, pin):      
        try:
            db = mysql.connector.connect(
            host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user = 'uhhcevmfsdoh3b14',
            password = 'iI4zqX9mPaJHPKmFyjhp',
            database = 'byhmrkozld7aa4b3kupq'
        )
            cursor = db.cursor()
            cursor.execute(f"UPDATE PIN SET pin = {pin} WHERE accountNumber = '{self.accountNumber}'")
            db.commit()
            return True

        except mysql.connector.Error as error:
            return False

    def fetchBalance(self):
        try:
            db = mysql.connector.connect(
            host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user = 'uhhcevmfsdoh3b14',
            password = 'iI4zqX9mPaJHPKmFyjhp',
            database = 'byhmrkozld7aa4b3kupq'
        )
            cursor = db.cursor()
            cursor.execute(f"SELECT balance FROM ACCOUNT WHERE accountNumber = '{self.accountNumber}'")
            records = cursor.fetchall()
            
            return records[0][0]

        except mysql.connector.Error as error:
            print("Failed to fetch Balance : {}".format(error))

    def updateBalance(self, balance):
        self.balance=balance
        print(self.balance, "check", type(self.balance))
        try:
            db = mysql.connector.connect(
            host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user = 'uhhcevmfsdoh3b14',
            password = 'iI4zqX9mPaJHPKmFyjhp',
            database = 'byhmrkozld7aa4b3kupq'
        )
            cursor = db.cursor()
            cursor.execute(f"UPDATE ACCOUNT SET balance = {self.balance} WHERE accountNumber = '{self.accountNumber}'")
            db.commit()
            return True

        except mysql.connector.Error as error:
            print("hihi")
            return False 

    def fetchAccountDetails(self):
        try:
            db = mysql.connector.connect(
            host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user = 'uhhcevmfsdoh3b14',
            password = 'iI4zqX9mPaJHPKmFyjhp',
            database = 'byhmrkozld7aa4b3kupq'
        )
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM ACCOUNT WHERE accountNumber = '{self.accountNumber}'")

            records = cursor.fetchall()

            # t = PrettyTable(['Account Number', 'Account Holder\'s Name', 'Balance', 'Account Type'])
            # t.add_row(records[0])
            # print(t)
            return records[0]

        except mysql.connector.Error as error:
            print(f"Failed to fetch account details : {error}")
    
    def updateName(self, name):
        try:
            db = mysql.connector.connect(
            host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user = 'uhhcevmfsdoh3b14',
            password = 'iI4zqX9mPaJHPKmFyjhp',
            database = 'byhmrkozld7aa4b3kupq'
        )
            cursor = db.cursor()
            cursor.execute(f"UPDATE ACCOUNT SET name = '{name}' WHERE accountNumber = '{self.accountNumber}'")
            db.commit()
            return True

        except mysql.connector.Error as error:
                return False 




    # fetchAccountDetails(987987987)
    # print(updateBalance(987987987, 2))
