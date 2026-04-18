'''
Author: Adityaraj Yadav 
Date: 20 January 2022
Project Name: Trailing Zeros with Factorial
Purpose:For Practising Purpose
'''

Factorial_Num = int(input("Enter the number: "))

# This program find the factorial of the given number and it used recursion
def Factorial(Number):
    if Number == 0 or Number == 1:
        return 1
    else:
        return  Number * Factorial(Number-1)

# This fucntion find out the the trailing zero of the given number
def factorial_Trailing_Zero(Number):
    # This will say memory error you given some bigger number and the above one also
    # Fac = Factorial(Number)
    # count = 0
    # while Fac%10 == 0:
    #     count = count + 1
    #     Fac = Fac/10
    # return count

    # This will not give any error like the above one
    count = 0
    i = 5
    while Number//i != 0:
        count += int(Number/i)
        i = i * 5 
    return count

if __name__ == '__main__':
    fac= Factorial(Factorial_Num)
    print(fac)
    trail = factorial_Trailing_Zero(560)
    print(trail)
