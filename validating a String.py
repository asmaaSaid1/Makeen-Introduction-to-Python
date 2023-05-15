string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
      if position == 0:
         valid = string[position] == "("
      elif position == 4 :
         valid = string[position] == ")"
      elif position == 8 :
         valid = string[position] == "-"
      else:
         valid = string[position].isdigit()
      position = position + 1
if valid :
     print("The string contains a valid phone number.")
else:
     print("The string does not contain a valid phone number.")
     
     
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
    valid=((position==0 and position[string]=="(")or (position==4 and position[string]==")") or (positon==8 and position=="-") or (position!=0 and position!=4 and position!=8 and string[position].isdigit()))
    position=position+1
if valid :
     print("The string contains a valid phone number.")
else:
     print("The string does not contain a valid phone number.")
       