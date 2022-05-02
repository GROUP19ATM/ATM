import mysql.connector
import numpy as np

class IncomeTax:

    def __init__(self, account_number):
        self.account_number = account_number
        self.incomeTax = self.fetchIncomeTaxID()

    def fetchIncomeTaxID(self):
        try:
            db = mysql.connector.connect(
                host='byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
                user='uhhcevmfsdoh3b14',
                password='iI4zqX9mPaJHPKmFyjhp',
                database='byhmrkozld7aa4b3kupq'
            )
            cursor = db.cursor()
            cursor.execute(f"SELECT incomeTaxID FROM INCOME_TAX WHERE accountNumber = '{self.account_number}'")
            records = cursor.fetchall()
            return records[0][0]

        except mysql.connector.Error as error:
            print(f"Unable to fetch Income Tax ID")

    def fetchBalance(self, accountNumber):
        try:
            db = mysql.connector.connect(
                host='byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
                user='uhhcevmfsdoh3b14',
                password='iI4zqX9mPaJHPKmFyjhp',
                database='byhmrkozld7aa4b3kupq'
            )
            cursor = db.cursor()
            cursor.execute(f"SELECT balance FROM ACCOUNT WHERE accountNumber = '{accountNumber}'")
            records = cursor.fetchall()

            return records[0][0]

        except mysql.connector.Error as error:
            print("Failed to fetch Balance : {}".format(error))

    def fetchIncomeTaxReturns(self):
        balance = self.fetchBalance(self.account_number)
        income_tax_returns = np.random.randint(low=10000, high=int(balance * 3 / 10))
        print(income_tax_returns)

i = IncomeTax('PDFJB00000000001')
i.fetchIncomeTaxReturns()
