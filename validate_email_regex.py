import re
email_condition = "^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter Your Mail: ")
if re.search(email_condition,user_email):
    print("Right mail")
else:
    print("Wrong mail")