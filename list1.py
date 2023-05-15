
"""Write for loops that iterate over the elements of a list without the use of the
range function for the following tasks.
a. Printing all elements of a list in a single row, separated by spaces.
b. Computing the product of all elements in a list.
c. Counting how many elements in a list are negative."""

x=[22,3,-2,-1,10,1]
count=0
p=1
for element in x:
    print(element,"",end="")
    
    p=p*element
    if element<0:
        count+=1  
   
print("\n")
print("the product of all elements in a list is =",p)
print("elements in a list are negative =",count)       

