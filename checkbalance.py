import account
class CHECKBALANCE:
    def __init__(self,acc_no):
        self.acc_no=acc_no

    def checkBalance(self):
        acc=account.ACCOUNT(self.acc_no)
        print("Balance is : RS %0.2f"%acc.fetchBalance())
        
    
    