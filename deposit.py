import account


class DEPOSIT:
    def __init__(self, acc_no, amt):
        self.acc_no = acc_no
        self.amt = amt

    def deposit(self):
        acc = account.ACCOUNT(self.acc_no)
        balance = self.amt + acc.fetchBalance()
        acc.updateBalance(balance)
        print("The money has ben deposited")
