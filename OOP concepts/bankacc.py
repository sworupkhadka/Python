class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    #debit
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount,"was debited ")
        print("total balance is =",self.get_balance())

    #credit
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited ")
        print("total balance is =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(100000,123)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)