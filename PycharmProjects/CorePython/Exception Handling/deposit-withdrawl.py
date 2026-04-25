from itertools import count
class insufficient_balance(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.name = None
        self.number = None
        self.account_type = None
        self.balance = 0.0
        self.address = None
        self.count = 0

    def setname(self, name):
        self.name = name

    def setnumber(self, number):
        self.number = number

    def setaccount_type(self, account_type):
        self.account_type = account_type

    def setbalance(self, balance):
        self.balance = balance

    def setaddress(self, address):
        self.address = address

    def getname(self):
        return self.name

    def getnumber(self):
        return self.number

    def getaccount_type(self):
        return self.account_type

    def getbalance(self):
        return self.balance

    def getaddress(self):
        return self.address

    def deposit(self):
        amt = int(input("Enter amount to deposit: "))
        print("Amount Deposited is", amt)
        if amt < 20000:
            self.balance = self.balance + amt
            print("Total balance after deposit:", self.balance)
        else:
            raise insufficient_balance("You can not submit more than 20000 per time in your account")

    def withdrawal(self):
        amt = int(input("Enter amount to withdraw: "))
        if amt < 10000:
            if amt < self.balance:
                for i in range(6):
                    self.balance = self.balance - amt
                    self.count += 1
                    print(self.count)
                    print("Total balance after withdrawal:", self.balance)
                    if self.count >= 5:
                        raise insufficient_balance("Your Limit for the day is over")
                        break
            else:
                raise insufficient_balance("Insufficient fund transfer")
        else:
            raise insufficient_balance("You can not withdrawl more than 10000 per time from your account")

try:
    account = Account()
    account.setname("Niharika Aurora")
    account.setnumber(123234553)
    account.setaccount_type("Self Account")
    account.setbalance(50000)
    account.setaddress("Indore M.P")
    Name = account.getname()
    AccountNumber = account.getnumber()
    AccountType = account.getaccount_type()
    AccountBalance = account.getbalance()
    AccountAddress = account.getaddress()
    print("Name of Account Holder is", Name)
    print("Account Number is", AccountNumber)
    print("Account Type is", AccountType)
    print("Account Balance is", AccountBalance)
    print("Account Address is", AccountAddress)
    account.deposit()
    account.withdrawal()
except insufficient_balance as e:
    print("Error is",e)

