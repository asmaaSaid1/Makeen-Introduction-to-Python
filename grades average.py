
#FIND THE AVERAGE OF GRADES
numString=int(input("enter number of grades :"))
s=0

for i in range(numString):
                interString=float(input("enter grade :"))
                s=s+interString
                
if numString>0:
   avg=float(s/numString)
   print(avg)
