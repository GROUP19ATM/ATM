import account

class AUTHENTICATOR:

    def __init__(self,acc_no,pin):
        self.acc_no=acc_no
        self.pin=pin

    def validate(self):
        acc=account.ACCOUNT(self.acc_no)
        if self.pin==acc.fetchPIN():
            print("Entered pin is correct")
            return True
        else:
            print("Error, Entered credentials are incorrect")
            return False


    