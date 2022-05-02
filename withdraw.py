class WITHDRAW:
    def __init__(self,acc_no,amt):
        self.acc_no=acc_no
        self.amt=amt

    def withdraw(self):
        print("withdrawed from "+self.acc_no)
    
    