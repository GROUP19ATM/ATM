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

        insurance_premium = np.random.randint(low=10000, high=int(balance * 3 / 10))
        print(insurance_premium)


i = Insurance('PDFJB00000000001')
i.fetchInsurancePremium()

    
    
