import mysql.connector
from mysql.connector import Error

services = {
    1: 'Withdraw',
    2: 'Deposit',
    3: 'Check Balance',
    4: 'Cheque Deposit',
    5: 'Fund Transfer',
    6: 'Income Tax Payment',
    7: 'Insurance Premium Payment',
    8: 'Update Account Details',
    9: 'Change PIN',
    10: 'Loan Application Initiation',
}


def fillTransactions(initial_time, final_time, account_number, choice):
    offset = 546
    try:
        db = mysql.connector.connect(
            host='byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
            user='uhhcevmfsdoh3b14',
            password='iI4zqX9mPaJHPKmFyjhp',
            database='byhmrkozld7aa4b3kupq'
        )
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM ATM_TRANSACTIONS WHERE accountNumber = '{account_number}'")
        records = cursor.fetchall()
        offset += len(records)
        offset = str(offset)
        cursor.execute(
            f"INSERT INTO ATM_TRANSACTIONS VALUES('{'TRN' + offset}', '{account_number}', '{services[choice]}', '{'SSN' + offset}', '{initial_time}', '{final_time}') "
        )
        db.commit()
    except mysql.connector.Error as error:
        print("Failed to fetch PIN : {}".format(error))
    pass
