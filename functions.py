from multiprocessing import connection
from prettytable import PrettyTable
import mysql.connector
from mysql.connector import Error


# try:
#     #old account :-
#     # mydb = mysql.connector.connect(
#     #     host='bfs0jullxosf8xrxbosu-mysql.services.clever-cloud.com', 
#     #     user = 'u26hhuzcr1tpa1cd', 
#     #     password = 'pha9fjVfZxug54QBYGeP',
#     #     database = 'bfs0jullxosf8xrxbosu')

#     db = mysql.connector.connect(
#         host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
#         user = 'uhhcevmfsdoh3b14',
#         password = 'iI4zqX9mPaJHPKmFyjhp',
#         database = 'byhmrkozld7aa4b3kupq'
#     )

#     cursor = db.cursor()
#     # mycursor.execute("""CREATE TABLE ACCOUNTS(
        # accountNumber varchar(16) NOT NULL, 
        # cardPIN int NOT NULL, 
        # accountHoldersName varchar(50), 
        # balance double, 
        # insuranceID varchar(10), 
        # incomeTaxID varchar(10)
        # PRIMARY KEY(accountNumber)
#     # )""")

#     # mycursor.execute("CREATE DATABASE Bank_Database")

#     cursor.execute("INSERT INTO PIN VALUES ('987987987', 1234)")
#     db.commit()

# except mysql.connector.Error as error:
#     print("Failed to insert value in PIN Table : {}".format(error))


def fetchPIN(accountNumber):
    try:
        db = mysql.connector.connect(
        host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
        user = 'uhhcevmfsdoh3b14',
        password = 'iI4zqX9mPaJHPKmFyjhp',
        database = 'byhmrkozld7aa4b3kupq'
    )
        cursor = db.cursor()
        cursor.execute(f"SELECT pin FROM PIN WHERE accountNumber = {accountNumber}")
        records = cursor.fetchall()

        return records[0][0]        

    except mysql.connector.Error as error:
        print("Failed to fetch PIN : {}".format(error))

# print(fetchPIN(987987987))

def updatePIN(accountNumber, pin):
    try:
        db = mysql.connector.connect(
        host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
        user = 'uhhcevmfsdoh3b14',
        password = 'iI4zqX9mPaJHPKmFyjhp',
        database = 'byhmrkozld7aa4b3kupq'
    )
        cursor = db.cursor()
        cursor.execute(f"UPDATE PIN SET pin = {pin} WHERE accountNumber = {accountNumber}")
        db.commit()
        return True

    except mysql.connector.Error as error:
        return False

def fetchBalance(accountNumber):
    try:
        db = mysql.connector.connect(
        host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
        user = 'uhhcevmfsdoh3b14',
        password = 'iI4zqX9mPaJHPKmFyjhp',
        database = 'byhmrkozld7aa4b3kupq'
    )
        cursor = db.cursor()
        cursor.execute(f"SELECT balance FROM ACCOUNT WHERE accountNumber = {accountNumber}")
        records = cursor.fetchall()
        
        return records[0][0]

    except mysql.connector.Error as error:
        print("Failed to fetch Balance : {}".format(error))

def updateBalance(accountNumber, balance):
    try:
        db = mysql.connector.connect(
        host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
        user = 'uhhcevmfsdoh3b14',
        password = 'iI4zqX9mPaJHPKmFyjhp',
        database = 'byhmrkozld7aa4b3kupq'
    )
        cursor = db.cursor()
        cursor.execute(f"UPDATE ACCOUNT SET balance = {balance} WHERE accountNumber = {accountNumber}")
        db.commit()
        return True

    except mysql.connector.Error as error:
        return False 

def fetchAccountDetails(accountNumber):
    try:
        db = mysql.connector.connect(
        host = 'byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
        user = 'uhhcevmfsdoh3b14',
        password = 'iI4zqX9mPaJHPKmFyjhp',
        database = 'byhmrkozld7aa4b3kupq'
    )
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM ACCOUNT WHERE accountNumber = {accountNumber}")

        records = cursor.fetchall()

        # t = PrettyTable(['Account Number', 'Account Holder\'s Name', 'Balance', 'Account Type'])
        # t.add_row(records[0])
        # print(t)
        return records[0]

    except mysql.connector.Error as error:
        print(f"Failed to fetch account details : {error}")



fetchAccountDetails(987987987)
# print(updateBalance(987987987, 2))
