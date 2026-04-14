print("\t\t\t\t\tWelcome to the Kirana Store Calculator")
print("\t\t\t\t\tyou can exit or quit it by pressing q key")
sum = 0
while True:
    User_Entry = input("Enter the price: ")
    if User_Entry != 'q':
        sum = sum + int(User_Entry)
        print(f"Till now total Bill is {sum}\n")
    else:
        print(f"\n\tYour total Bill is {sum}. Thank you! for shopping in our shop")
        break
