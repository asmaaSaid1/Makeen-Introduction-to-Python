
#find middle character from string
string=input("enter string:")

#find middle character if string is even
if len(string)%2==0:
    mid=len(string)//2-1
    print(string[mid]+string[mid+1])
    
#find middle character if tring is even
else:
    mid=len(string)//2
    print(string[mid])
