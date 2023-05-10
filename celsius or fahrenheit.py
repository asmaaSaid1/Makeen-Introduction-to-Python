
#program to calculate the temprature degree in celsius or fahrenheit

tem_unit=input("enter C for celsius or F for fahrenheit :")
tem=float(input("enter temperature :"))

#transfer from celsius to fahrenheit
if tem_unit=="C":
          f=(tem*1.8)+32
          print("temperature in fahrenheit is ", f)

#transfer from fahrenheit to celsius 
elif tem_unit=="F":
    c=int(tem-32)//1.8
    print("temperature in celsius is " ,c)
