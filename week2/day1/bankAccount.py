class BankAccount:
    def __init__(self,balance,name):
        self.balance = balance
        self.name = name
    def deposit(self,n):
        self.balance += n
        print("Deposit of",n,"is Completed Successfully")
    def withdraw(self,n):
        self.balance -= n
        print("Withdraw of",n,"is Completed Successfully")
    def getBalance(self):
        return "Current balance ",self.balance
ac = BankAccount(100,"Goutham")
print(ac.name)
print(ac.getBalance())
ac.withdraw(25)
print(ac.getBalance())
ac.deposit(50)
print(ac.getBalance())
