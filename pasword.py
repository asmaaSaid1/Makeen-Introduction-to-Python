# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:50:47 2023

@author: Asma
"""

# password
# checking whether the password is valid or not 

"""
Primary conditions for password validation:
Minimum 8 characters.
The alphabet must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ]."""

pasword=input("enter pasword:")
up=0
low=0
dig=0
ch=0
for i in pasword:
    if (i.isupper()==True):
        up=up+1
    if (i.islower()==True):
        low=low+1
    if (i.isdigit()==True):
        dig=dig+1
    if (i=="#"or"$"or"@"or"&"):
        ch=ch+1

if (up>=1)and(low>=1)and(dig>=1)and(ch>=1)and (len(pasword)>=8):
    print("valid pasword")
else:
    print("pasword not valid,try again")