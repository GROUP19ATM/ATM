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
#import authenticator 

class ATM:
    atmId="abc"
    branchCode="bbb"

    def __init__(self,cash):
        self.cash=cash

    def getId(self):
        return ATM.atmId
     
    def insertCard(self):
        print("Please insert card in the ATM")
        return True
    
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

    def readPin(self,pin):
        self.pin=pin

    def getAccountNumber(self,acc_no):
        self.acc_no=acc_no


    
obj=ATM(10000)

if obj.insertCard():
    acc_no=input("Enter Account Number : ")
    pin=int(input("Enter the pin : "))
    
    if obj.readCard(acc_no,pin):
        while 1:
            print("Choose from the given services : ")
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Check Balance")
            print("4.Cheque Deposit")
            print("5.Fund Transfer")
            print("6.Income Tax Payment")
            print("7.Insurance Premium Payment")
            print("8.Update Account Details")
            print("9.Change PIN")
            print("10.Loan Application Initiation")
            print("11.Log Out")
        
            choice=int(input("Enter your choice : (enter the respective number of the services list above)"))
            if choice==1:
                amt=int(input("Enter the amount to withdraw : "))
                o1=withdraw.WITHDRAW(acc_no,amt)
                o1.withdraw()
            
            elif choice==2:
                amt=int(input("Enter the amount to deposit : "))
                o2=deposit.DEPOSIT(acc_no,amt)
                o2.deposit()
            
            elif choice==3:
                o3=checkbalance.CHECKBALANCE(acc_no)
                o3.checkBalance()

            elif choice==4:
                cheque_no=int(input("Enter the Cheque Number : "))
                o4=chequedeposit.CHEQUEDEPOSIT(acc_no,cheque_no)
                o4.chequeDeposit()

            elif choice==5:
                o5=fundtransfer.FUNDTRANSFER()
                o5.fundTransfer()

            elif choice==6:
                inc_id=input("Enter the Income TAx ID : ")
                o6=incometax.INCOMETAXPAYMENT(inc_id)
                o6.incomeTaxPayment()

            elif choice==7:
                ins_id=input("Enter Insurance Premium ID : ")
                o7=insurancepremium.INSURANCEPREMIUM(ins_id)
                o7.insurancePremiumPaytemt()

            elif choice==8:
                o8=updateaccount.UPDATEACCDETAILS()
                o8.updateAccountDetails()
            elif choice==9:
                o_pin=int(input("Enter old pin : "))
                n_pin=int(input("Enter new pin: "))
                o9=changepin.CHANGEPIN(acc_no,o_pin,n_pin)
                o9.changePin()
            elif choice==10:
                o10=loanapp.LOANAPLICATION()
                o10.loanApplictionInitiation()

            elif choice==11:
                print("LOGGED OUT! ")
                break
            else:
                print("Wrong Input, Try again!!")
    else:
        obj.rejectCard()
    
