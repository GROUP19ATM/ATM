class DEPOSIT:
    def __init__(self,acc_no,amt):
        self.acc_no=acc_no
        self.amt=amt

    def deposit(self):
        print("deposited in "+self.acc_no)
    
    