class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        msg = self.balance
        return str(msg)

    def deposits(self, money):
        self.balance = self.balance + money
        print "You deposits", money, "$."

    def withdrawals(self, money):
        if self.balance > money:
            self.balance = self.balance - money
            print "You withdrawals", money, "$."
        else:
            print "Balance less than money."

myAccount = BankAccount("ander", "000000", 200)
print myAccount
myAccount.deposits(100)
print myAccount
BankAccount.withdrawals(myAccount, 50)
print myAccount