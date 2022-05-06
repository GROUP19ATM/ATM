import account


class WITHDRAW:
    def __init__(self, acc_no, amt):
        self.acc_no = acc_no
        self.amt = amt

    def withdraw(self):
        acc = account.ACCOUNT(self.acc_no)
        if acc.fetchBalance() > 2000:
            if self.amt < acc.fetchBalance() and self.amt < 200000:
                balance = acc.fetchBalance() - self.amt
                acc.updateBalance(balance)
                print("The money has been withdrawn")
        else:
            print("Not enough money")
