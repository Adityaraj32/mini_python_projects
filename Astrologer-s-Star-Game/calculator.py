#    First Method For Calculator

while True:
    firstnum = int(input("Enter first number: "))
    operator = input("Enter the operator: ")
    secondnum = int(input("Enter second number: "))
    if operator == "+":
        num = firstnum + secondnum
        print(num)
    elif operator == "-":
        num = firstnum - secondnum
        print(num)
    elif operator == "/":
        num = firstnum / secondnum
        print(num)
    elif operator == "*":
        num = firstnum * secondnum
        print(num)
    elif operator == "remainder":
        num = firstnum % secondnum
        print(num)
    exitornot = input("Do you want to exit Yes(y) or No(n): ")
    if exitornot == "y":
        break
    else:
        continue

#      This Calculator Will Add,Multiply,Divide,Substract And Show Remainder

# firstnum = int(input("Enter first number: "))
# operator = input("Enter the operator: ")
# secondnum = int(input("Enter second number: "))

# if operator == "+" :
#     print(f"{firstnum} {operator} {secondnum} = {firstnum + secondnum}")
# elif operator == "*" :
#     print(f"{firstnum} {operator} {secondnum} = {firstnum * secondnum}")
# elif operator == "-" :
#     print(f"{firstnum} {operator} {secondnum} = {firstnum - secondnum}")
# elif operator == "/" :
#     print(f"{firstnum} {operator} {secondnum} = {firstnum / secondnum}")
# elif operator == "%":
#     print((secondnum-firstnum)/secondnum * 100)
# elif operator == "remainder" or  "or":
#     print(f"{firstnum % secondnum}")