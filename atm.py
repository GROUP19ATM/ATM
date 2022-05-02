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
import os;
import time;
from termcolor import colored;
from pyfiglet import Figlet;
#import authenticator 
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
    
    x=0
    while True:
        print(bar[x % len(bar)], end="\r")
        time.sleep(.2)
        x += 1
        if(x==20):break
class ATM:
    atmId="abc"
    branchCode="bbb"

    def __init__(self,cash):
        self.cash=cash

    def welcome(self):
        f=Figlet(font='banner3-D')
        
                                                                                    
        print(colored(f.renderText('Welcome'),'red'))
        
    def getId(self):
        return ATM.atmId
     
    def insertCard(self):
        print("       #########################################")
        print("       #                                       #");
        print("       #      Enter Card Number:",end="")
        c_no=input()
        #print("#")
        print("       #                                       #");
        print("       #      Enter PIN:",end="")
        pin=input()
        print("       #                                       #");
        print("       #########################################")
        #print("#")
        return c_no
    
    def readCard(self,accno,pin):
        return True

    def rejectCard(self):
        print("Error in card, CARD REJECTED!!")

    def isCashAvailable(self):
        if self.cash>=5000:
            return True 
        else:
            return False
            
    def displayCash(self):
        print("The Cash present in ATM is : "+self.cash)
    def getACno(card_no):
        acno=60
        return acno
    def readPin(self,pin):
        self.pin=pin

    def getAccountNumber(self,acc_no):
        self.acc_no=acc_no
    def ejectCart():
        print()
        print("               Please Remove Your Card        ");
        print()
        input()


    
obj=ATM(10000)
obj.welcome();
while(true):
    c_no=obj.insertCard()
    acc_no=obj.getAccountNumber(c_no)
    pin=60
    print("\nAuthenticating ")
    loading()

    if obj.readCard(acc_no,pin):
        while 1:
            screen_clear()
            print("###########################################")
            print("#   ",end="")
            print(colored("Choose from the given services :",'red'),end="")
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
        
            print(colored("\n\nEnter your choice (NUMBER):)",'green'))
            choice=int(input())
            if choice==1:
                screen_clear()
                print("WITHDRAW")
                amt=int(input("Enter the amount to withdraw : "))
                o1=withdraw.WITHDRAW(acc_no,amt)
                o1.withdraw()
                obj.ejectCart();
            
            elif choice==2:
                screen_clear()
                amt=int(input("Enter the amount to deposit : "))
                o2=deposit.DEPOSIT(acc_no,amt)
                o2.deposit()
                obj.ejectCart();
            
            elif choice==3:
                screen_clear()
                o3=checkbalance.CHECKBALANCE(acc_no)
                o3.checkBalance()
                obj.ejectCart();

            elif choice==4:
                screen_clear()
                cheque_no=int(input("Enter the Cheque Number : "))
                o4=chequedeposit.CHEQUEDEPOSIT(acc_no,cheque_no)
                o4.chequeDeposit()
                obj.ejectCart();

            elif choice==5:
                screen_clear()
                o5=fundtransfer.FUNDTRANSFER()
                o5.fundTransfer()
                obj.ejectCart();

            elif choice==6:
                screen_clear()
                inc_id=input("Enter the Income TAx ID : ")
                o6=incometax.INCOMETAXPAYMENT(inc_id)
                o6.incomeTaxPayment()
                obj.ejectCart();

            elif choice==7:
                screen_clear()
                ins_id=input("Enter Insurance Premium ID : ")
                o7=insurancepremium.INSURANCEPREMIUM(ins_id)
                o7.insurancePremiumPaytemt()
                obj.ejectCart();

            elif choice==8:
                screen_clear()
                o8=updateaccount.UPDATEACCDETAILS()
                o8.updateAccountDetails()
                obj.ejectCart();
            elif choice==9:
                screen_clear()
                o_pin=int(input("Enter old pin : "))
                n_pin=int(input("Enter new pin: "))
                o9=changepin.CHANGEPIN(acc_no,o_pin,n_pin)
                o9.changePin()
                obj.ejectCart();
            elif choice==10:
                screen_clear()
                o10=loanapp.LOANAPLICATION()
                o10.loanApplictionInitiation()
                obj.ejectCart();

            elif choice==11:
                print("LOGGED OUT! ")
                break
            else:
                print("Wrong Input, Try again!!")
    else:
        obj.rejectCard()
    
