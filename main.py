import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Please Enter Your Password : ")
result = re.findall(pattern, password)
if (result):
    print ("Valid password")
else:
    print ("Password not valid")

