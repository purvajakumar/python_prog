n=int(input("enter the number"))
c=0
for i in range (2,n+1):
    if(n%i==0):
        c+=1
    
if(c==1):
    print("it is a prime number")
else:
    print("it is a composite number")
    
        
