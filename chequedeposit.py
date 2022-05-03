import deposit
class CHEQUEDEPOSIT:
    def __init__(self,acc_no,cheque_id,amt):
        self.acc_no=acc_no
        self.cheque_id=cheque_id
        self.amt=amt

    def chequeDeposit(self):
        ched=deposit.DEPOSIT(self.acc_no,self.amt)
        ched.deposit()
        print("Money deposited from cheque ID ",end="")
        print(self.cheque_id)
    
    
