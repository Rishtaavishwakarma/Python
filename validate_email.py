email=input("Enter your email")
k,j=0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
           if (email[-4]==".") ^ (email[-3]=="."):
               for i in email:
                   if i==i.isspace():
                       k=1
                   elif i.isalpha():
                       if i==i.upper():
                           j=1
                  
               if k==1 or j==1:
                   print("No Space or caps allowed")       
           else:
               print("check your dot")
        else:
            print("Wrong email @ issue")
    else:
        print("Wrong email not alpha")
else: 
    print("Length is too small")