import random
inputNum=int(input("enter number between 1 to 100:"))
  
ranNum=round(random.random()*100,0)

if (inputNum>100 or inputNum<0 ):
    print("out of the range")
else:
    for i in range(101):
        if (inputNum==ranNum):
           print("great")
           break
        elif (inputNum<ranNum):
           print("go higher")
        
        elif (inputNum>ranNum):
           print("go lower")
        
        inputNum=int(input("enter number between 1 to 100:"))

       