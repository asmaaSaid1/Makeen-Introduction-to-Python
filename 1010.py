a=[[0]*4 for i in range(0,4)]


for i in range(4):
    for j in range(4):
        if (i+j)%2==0:
            a[i][j]=1
        
for i in range(4):
    for j in range(4):
         print(a[i][j],end=" ")
    print()