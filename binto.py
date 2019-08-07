items=[]
num=[x for x in input().split(',')]
for i in num:
    x=int(i,2)
    if not x%5:
        items.append(i)
print(','.join(items))        
