import math
#calculate the totale surface volume and area of cylinder
hight_cylinder=4
radius_cylinder=6

volume_cylinder=math.pi*radius_cylinder**2*hight_cylinder
area_cylinder=(2*math.pi*radius_cylinder*hight_cylinder)+(2*math.pi*radius_cylinder**2)

print("volume is: %.2f " %volume_cylinder)
print("surface area is: %.2f" %area_cylinder)

#calculate of total cost of purchase 
r=1 #cost of one ton
n=10 #number of tons
vat=0.05
price=n*r
addition=price*vat
new_price=price+addition
print(new_price)
