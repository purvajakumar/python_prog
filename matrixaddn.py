a=[[1,2],
   [3,4],
   [5,6]]
b=[[2,3],
   [4,5],
   [6,7]]
res=[[0,0],
     [0,0],
     [0,0]]
for i in  range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]+b[i][j]
for r in res:
    print(r)
