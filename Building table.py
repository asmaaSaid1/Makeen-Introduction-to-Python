
m=[[i]*3 for i in range(1,4)]
     


for k in range(3):
    for j in range(3):
        print(m[k][j],end=" ")
    print()
    
    

r=int(input("enter the number of rows :"))
c=int(input("enter the number of columns :"))
s=[[i]*c for i in range(r)]

for k in range(r):
    for j in range(c):
        s[k][j]=int(input("enter value :"))
        
        
for i in range(r):
    for j in range(c):
         print(s[i][j],end=" ")
    print()