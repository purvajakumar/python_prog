amt=int(input("Enter the amount"))
while(amt>0):
    a=amt//500
    r=amt%500
    b=r//200
    r=r%200
    c=r//100
    r=r%100
    d=r//50
    r=r%50
    e=r//20
    r=r%20
    f=r//10
    r=r%10
    break
print("500=", a,"200=",b,"100=",c,"50=",d,"20=",e,"10=",f)
        
