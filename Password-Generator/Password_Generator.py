import string
import random

Upper_Case = string.ascii_uppercase
Lower_Case = string.ascii_lowercase
Digit = string.digits
Punctuation = string.punctuation

while True:
    """This will check whether we input in the Pass_Length is integer or not if it is not it will print that please enter the string 
    value and else it will convert the Pass_Length to a Int"""
    
    Pass_Length = input("Enter the password length that you want: ")
    if (Pass_Length.isnumeric()):
        Pass_Length = int(Pass_Length)
        break
    else:
        print("Please enter a numerica length!")
        continue

s = []
s.extend(list(Upper_Case))
s.extend(list(Lower_Case))
s.extend(list(Digit))
s.extend(list(Punctuation))

random.shuffle(s)
print("Your Password is: ")
print("".join(s[0:Pass_Length]))
