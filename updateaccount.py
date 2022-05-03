import account
class UPDATEACCDETAILS:

    def __init__(self,acc_no):
        self.acc_no=acc_no

    def updateAccountDetails(self,name):        
        self.name=name
        acc=account.ACCOUNT(self.acc_no)
        acc.updateName(self.name)
        print("Account details(name) updated")

    
    
