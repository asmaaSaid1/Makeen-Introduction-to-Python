
#program to print the frist 10 even numbers using while loop
num=0
while num<20:
    if (num%2==0):
        print(num)
    num=num+1
    
#program to print the frist 10 numbers and their squares    
num=0
while (num<10):
    print(num)
    print(num**2)
    num=num+1
    
#while loop to print(105,98,91,....7)

num=105
while (num<=105) and (num>=7):
    print(num)
    num=num-7


#display acsii
string="Hello"
i=0
while i<len(string):
    print(ord(string[i]))
    i=i+1

#factor of 10
num=1
while num<=10:
    if 10%num==0:
        print(num)
    num=num+1

    
    