year=int(input("Enter year:"))
if (year%4==0)or (year%400==0):
    print("سنة كبيسة")
else:
    print("سنة بسيطة")