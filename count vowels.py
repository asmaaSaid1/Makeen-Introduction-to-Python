
#program to count the vowels
def main():
    string=input("Enter a string :")
    print("The number of vowels are :",countVowels(string))
    
    
def countVowels(string):
    count=0
    for i in string:
        if (i in"aeiuo") or (i in "aeiuo".upper()):
            count=count+1
        
    return count
    
main()