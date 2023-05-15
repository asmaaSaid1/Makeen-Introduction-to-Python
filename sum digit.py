

#compute the sum of the digit in an integer
def main():
    n=input("enter number :")
    print(sumdigit(n))



def sumdigit(n):
    s=str(n)
    add=0
    for i in s:
        add=add+int(i)
    return add



  
main()          