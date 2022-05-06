import withdraw
import deposit


class FUNDTRANSFER:
    def __init__(self, acc_no, to, amt):
        self.acc_no = acc_no
        self.to = to
        self.amt = amt

    def fundTransfer(self):
        w = withdraw.WITHDRAW(self.acc_no, self.amt)
        w.withdraw()
        d = deposit.DEPOSIT(self.to, self.amt)
        d.deposit()
        print("The money has been transferred from " + self.acc_no + " to " + self.to)
