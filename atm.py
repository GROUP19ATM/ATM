import account
import deposit
import withdraw
import checkbalance
import chequedeposit
import fundtransfer
import incometax
import insurancepremium
import updateaccount
import changepin
import loanapp
import authenticator as AR
import os
from multiprocessing import connection
from prettytable import PrettyTable
import mysql.connector
from insurancepremium import Insurance
from transaction_filler import fillTransactions
import time
from incometax import IncomeTax
from mysql.connector import Error

import pwinput
import time;
from termcolor import colored;
from pyfiglet import Figlet;


# import authenticator
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def loading():
    bar = [
        " [=                 ]",
        " [ =                ]",
        " [  =               ]",
        " [   =              ]",
        " [    =             ]",
        " [     =            ]",
        " [      =           ]",
        " [       =          ]",
        " [        =         ]",
        " [         =        ]",
        " [          =       ]",
        " [           =      ]",
        " [            =     ]",
        " [             =    ]",
        " [              =   ]",
        " [               =  ]",
        " [                = ]",

    ]

    x = 0
    while True:
        print(bar[x % len(bar)], end="\r")
        time.sleep(.2)
        x += 1
        if x == 20:
            break


class ATM:
    atmId = "PDF19JB"
    branchCode = "GRP19-BCG1267"

    def __init__(self, cash):
        self.cash = cash

    def fetchAccountNumber(self, cardNumber):
        try:
            db = mysql.connector.connect(
                host='byhmrkozld7aa4b3kupq-mysql.services.clever-cloud.com',
                user='uhhcevmfsdoh3b14',
                password='iI4zqX9mPaJHPKmFyjhp',
                database='byhmrkozld7aa4b3kupq'
            )
            cursor = db.cursor()
            cursor.execute(f"SELECT accountNumber FROM PIN AS P WHERE P.cardNumber='{cardNumber}'")
            records = cursor.fetchall()
            return records[0][0]
        except mysql.connector.Error as error:
            print(f"Failed to fetch account details : {error}")

    def welcome(self):
        f = Figlet(font='banner3-D')
        print(colored(f.renderText('Welcome'), 'red'))

    def getId(self):
        return ATM.atmId

    def insertCard(self):
        print("       ###############################################")
        print("       #                                             #");
        print("       #      Enter Card Number: ", end="")
        c_no = input()
        # print("#")
        print("       #                                             #");
        print("       #      Enter PIN: ", end="")
        pin = int(input())
        print("       #                                             #");
        print("       ###############################################")
        # print("#")
        return c_no, pin

    def readCard(self, acc_no, pin):
        val = AR.AUTHENTICATOR(acc_no, pin)
        return val.validate()

    def rejectCard(self):
        print("Error in card, CARD REJECTED!!")

    def isCashAvailable(self):
        if self.cash >= 5000:
            return True
        else:
            return False

    def displayCash(self):
        print("The Cash present in ATM is : " + self.cash)

    def getACno(card_no):
        acno = 60
        return acno

    def readPin(self, pin):
        self.pin = pin

    def getAccountNumber(self, acc_no):
        self.acc_no = acc_no

    def ejectCard(self):
        x = 0
        print()
        print()
        time.sleep(.6)
        while (x < 4):
            print("                                                ", end="\r")
            time.sleep(.4)
            print(colored("              PLEASE REMOVE YOUR CARD", 'red', attrs=['bold']), end="\r")
            time.sleep(.4)
            x += 1
        print()
        input()
        print("THANKYOU")


obj = ATM(10000)
obj.welcome();
condition = True
while (condition):
    c_no, pin = obj.insertCard()

    acc_no = obj.fetchAccountNumber(c_no)
    print("\nAuthenticating ")
    loading()
    # aut=AR.AUTHENTICATOR(acc_no,pin)
    # if(aut.validate()==False):break

    if obj.readCard(acc_no, pin):
        while 1:
            initial_time = time.time()
            screen_clear()
            print("###########################################")
            print("#   ", end="")
            print(colored("Choose from the given services :", 'red'), end="")
            print("      #")
            print("#-----------------------------------------#")
            print("#   1.Withdraw                            #")
            print("#   2.Deposit                             #")
            print("#   3.Check Balance                       #")
            print("#   4.Cheque Deposit                      #")
            print("#   5.Fund Transfer                       #")
            print("#   6.Income Tax Payment                  #")
            print("#   7.Insurance Premium Payment           #")
            print("#   8.Update Account Details              #")
            print("#   9.Change PIN                          #")
            print("#   10.Loan Application Initiation        #")
            print("#   11.Log Out                            #")
            print("###########################################")

            print(colored("\n\nEnter your choice (NUMBER):)", 'green'))
            choice = int(input())
            if choice == 1:
                screen_clear()
                f = Figlet(font='slant')
                print(colored(f.renderText("               WITHDRAW"), 'blue'))
                print("--------------------------------------------")
                print("|       Enter the amount to withdraw       |")
                print("--------------------------------------------")
                amt = int(input("                   "))
                print()
                o1 = withdraw.WITHDRAW(acc_no, amt)
                o1.withdraw()
                obj.ejectCard()
                condition = False

            elif choice == 2:
                screen_clear()
                f = Figlet(font='slant')
                print(colored(f.renderText("               DEPOSIT"), 'blue'))
                print("--------------------------------------------")
                print("|       Enter the amount to deposit       |")
                print("--------------------------------------------")
                amt = int(input("                   "))
                o2 = deposit.DEPOSIT(acc_no, amt)
                o2.deposit()
                obj.ejectCard();


            elif choice == 3:
                screen_clear()
                f = Figlet(font='slant')
                print(colored(f.renderText("CHECK BALANCE"), 'blue'))

                o3 = checkbalance.CHECKBALANCE(acc_no)
                o3.checkBalance()
                obj.ejectCard()



            elif choice == 4:
                screen_clear()
                f = Figlet(font='slant')
                print(colored(f.renderText("CHEQUE DEPOSIT"), 'blue'))
                print("--------------------------------------------")
                print("|           ENTER THE CHEQUE NUMBER         |")
                print("--------------------------------------------")
                cheque_no = int(input("|"))
                print("--------------------------------------------")
                screen_clear()
                print("--------------------------------------------")
                print("|          ENTER THE AMOUNT TO DEPOSIT     |")
                print("--------------------------------------------")
                amt = int(input("|                RS:"))
                print("--------------------------------------------")
                o4 = chequedeposit.CHEQUEDEPOSIT(acc_no, cheque_no, amt)
                o4.chequeDeposit()

                obj.ejectCard();

            elif choice == 5:
                screen_clear()
                f = Figlet(font='slant')
                print(colored(f.renderText("FUND TRANSFER"), 'blue'))
                print("--------------------------------------------")
                print("|          RECIEVER ACCOUNT NUMBER          |")
                print("--------------------------------------------")
                to = input("|")
                print("--------------------------------------------")
                screen_clear()
                print("--------------------------------------------")
                print("|          ENTER THE AMOUNT TO TRANSFER     |")
                print("--------------------------------------------")
                amt = int(input("|                RS:"))
                print("--------------------------------------------")

                o5 = fundtransfer.FUNDTRANSFER(acc_no, to, amt)
                # print("yes its working toll here");
                o5.fundTransfer()
                print(colored("\n              SUCCESS\n", 'green', attrs=['bold']), end="\r")
                obj.ejectCard()

            elif choice == 6:
                screen_clear()
                o6 = incometax.IncomeTax(account_number=acc_no)
                print(f'Your Income TAX ID is: {o6.fetchIncomeTaxID()}')
                returns = o6.fetchIncomeTaxReturns()
                print(f"Your income tax returns is: {returns}")
                confirmation = input("Type y to confirm")
                if confirmation != 'Y' and confirmation != 'y':
                    print("Service closed")
                    continue
                currentAccount = account.ACCOUNT(accountNumber=acc_no)
                currentAccount.updateBalance(currentAccount.fetchBalance() - returns)
                print(f"You have paid your tax returns of {returns}")
                obj.ejectCard();

            elif choice == 7:
                screen_clear()
                o7 = Insurance(account_number=acc_no)
                print(f'Your Insurance ID is: {o7.findInsuranceID()}')
                insurancePremium = o7.fetchInsurancePremium()
                print(f"Your insurance premium to pay: {insurancePremium}")
                confirmation = input("Type y to confirm")
                if confirmation != 'Y' and confirmation != 'y':
                    print("Service closed")
                    continue
                currentAccount = account.ACCOUNT(accountNumber=acc_no)
                currentAccount.updateBalance(currentAccount.fetchBalance() - insurancePremium)
                print(f"You have paid your insurance premium of {insurancePremium}")
                obj.ejectCard();

            elif choice == 8:
                screen_clear()
                f = Figlet(font='slant')
                print(colored(f.renderText("Update account details"), 'blue'))
                print("--------------------------------------------")
                print("|          ENTER OLD NAME          |")
                print("--------------------------------------------")
                o_name = input("|              ")
                print("--------------------------------------------")
                screen_clear()
                print("--------------------------------------------")
                print("|          ENTER NEW NAME          |")
                print("--------------------------------------------")
                n_name = input("|              ")
                print("--------------------------------------------")

                o8 = updateaccount.UPDATEACCDETAILS(acc_no)
                o8.updateAccountDetails(n_name)
                print(colored("\n              SUCCESS\n", 'green', attrs=['bold']), end="\r")
                obj.ejectCard();
            elif choice == 9:

                screen_clear()
                f = Figlet(font='slant')
                o_pin = pin

                print(colored(f.renderText("CHANGE PIN"), 'blue'))
                print("--------------------------------------------")
                print("|          PLEASE ENTER YOUR NEW PIN         |")
                print("--------------------------------------------")
                n_pin = int(pwinput.pwinput(prompt="|               "))
                screen_clear()
                print(colored(f.renderText("CHANGE PIN"), 'blue'))
                print("--------------------------------------------")
                print("|          PLEASE RE-ENTER YOUR NEW PIN    |")
                print("--------------------------------------------")

                rn_pin = int(pwinput.pwinput(prompt="|              "))
                if n_pin != rn_pin:
                    while n_pin != rn_pin:
                        screen_clear()
                        print(colored(f.renderText("CHANGE PIN"), 'blue'))
                        print("PINS are different!")
                        print("--------------------------------------------")
                        print("|          PLEASE RE-ENTER YOUR NEW PIN    |")
                        print("--------------------------------------------")
                        rn_pin = int(input("|          "))
                o9 = changepin.CHANGEPIN(acc_no, o_pin, n_pin)
                o9.changePin()
                print(colored("\n              SUCCESS\n", 'green', attrs=['bold']), end="\r")
                obj.ejectCard();
            elif choice == 10:
                screen_clear()
                o10 = loanapp.LOANAPLICATION()
                o10.loanApplictionInitiation()
                obj.ejectCard();

            elif choice == 11:
                screen_clear()
                print("LOGGED OUT! ")
                obj.ejectCard()
                break
            else:
                print("Wrong Input, Try again!!")
            final_time = time.time()
            fillTransactions(initial_time=initial_time, final_time=final_time, account_number=acc_no, choice=choice)
    else:
        obj.rejectCard()
