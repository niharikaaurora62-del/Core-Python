class AccountException(Exception):
     def __init__(self, msg):
         super().__init__(msg)

class Account():
  def __init__(self):
      self.name = ""
      self.account_type = ""
  def get_name(self):
      return self.name
  def get_account_type(self):
      return self.account_type
  def set_name(self, name):
      self.name = name
  def set_account_type(self, account_type):
      self.account_type = account_type

try:
    A1 = Account()
    Name = A1.set_name("Niharika Aurora")
    AccountType = A1.set_account_type("Self Account")
    name = A1.get_name()
    account_type = A1.get_account_type()
    if(name == "Niharika Aurora" and account_type == "Self Account"):
        raise AccountException("Account Type and name not matched")
    else:
        print("Account Type and name matched")
except AccountException as e:
    print("Error occured", e)