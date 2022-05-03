import authenticator
import account
class CHANGEPIN:
    def __init__(self,acc_no,o_pin,n_pin):
        self.acc_no=acc_no
        self.o_pin=o_pin
        self.n_pin=n_pin

    def changePin(self):
        at=authenticator.AUTHENTICATOR(self.acc_no,self.o_pin)
        if at.validate()==True:
            acc=account.ACCOUNT(self.acc_no)
            acc.updatePIN(self.n_pin)
            print("The pin has been updated")
        else:
            print("The enered old pin is incorrect try again!!.")


    
    
