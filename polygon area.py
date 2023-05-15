

#program to Find the area of polygon

import math

def area(n,side):
    a=float((n*side**2)/(4*math.tan(math.pi/n)))
    return a


def main():
    n=int(input("Enter the number of sides :"))
    side=float(input("Enter the side :"))
    x=area(n,side)
    print("The area of polygon is ",x)
    
    
main()