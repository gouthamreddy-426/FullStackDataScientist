class ATM:
    def __init__(self,pin,balance):
        self.balance = balance
        self.pin = pin 
        self.log_in = False
    def login(self,pin1):
        if pin1 == self.pin:
            self.log_in = True
            return "Access Granted"
        else:
            return "Incorrect Pin! Please Relogin"
    def check_balance(self):
        if self.log_in == True:
            return "Available Balance "+str(self.balance)
        else:
            return "Relogoin Needed"
    def deposit(self,amount):
        if self.log_in == True:
            self.balance += amount
            return "Deposited "+str(amount)
        else:
            return "Relogoin Needed"
    def withdraw(self,amount):
        if self.log_in == True:
            if self.balance >= amount:
                self.balance -= amount
                return "Withdrew "+str(amount)
            else:
                return "Insufficient Balance! Withdraw Failed"
        else:
            return "Relogoin Needed"
atm = ATM(1234, 500)
print(atm.login(1234))
print(atm.deposit(200))
print(atm.withdraw(701))
print(atm.check_balance())

    