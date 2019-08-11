import re
username=str(input("Enter the user name"))
password=str(input("Enter the passwords")).split(',')
x=True
while x:
    if(len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("valid password")
        x=False
        break
print("invalid password")
    
