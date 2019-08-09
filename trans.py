net_amt=0
trans=[]
while True:
    str1=input("enter the transaction")
    trans=str1.split(" ")
    print(trans)
    typ=trans[0]
    #amt=int(trans[1])
    if(typ=='D')or(typ=='d'):
        net_amt+=int(trans[1])
    elif(typ=='W')or(typ=='w'):
        net_amt-=int(trans[1])
    else:
       break
    
print("net amt is %d" %(net_amt))        
