import mysql.connector
import numpy as np


class Insurance:
    def __init__(self, account_number):
        self.account_number = account_number
        self.insuranceID = self.findInsuranceID()

    def findInsuranceID(self):
        try:
            db = mysql.connector.connect(
                host='byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
                user='uhhcevmfsdoh3b14',
                password='iI4zqX9mPaJHPKmFyjhp',
                database='byhmrkozld7aa4b3kupq'
            )
            cursor = db.cursor()
            cursor.execute(f"SELECT insuranceID from INSURANCE WHERE accountNumber='{self.account_number}'")
            records = cursor.fetchall()
            return records[0][0]
        except mysql.connector.Error as error:
            print(f"Failed to fetch insurance details: {error}")

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

    def fetchInsurancePremium(self):
        balance = self.fetchBalance(self.account_number)
        high_bound = int(balance * 3 / 10)
        low_bound = 10000 if int(balance * 3 / 10) > 10000 else int(high_bound/2)
        insurance_premium = np.random.randint(low=low_bound, high=high_bound)
        return insurance_premium
