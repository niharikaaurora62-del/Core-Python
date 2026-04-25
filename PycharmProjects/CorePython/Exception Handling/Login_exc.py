

class LoginException(Exception):
     def __init__(self, msg):
         super().__init__(msg)




LoginI="Admin"
PasswordI="Admin"

try:
    if LoginI == "Adin" and PasswordI == "Admin":
        print("Login Successful")
    else:
        raise LoginException("Login Failed")
except Exception as e:
    print("Exception",e)