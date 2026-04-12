num_lines = int(input("Enter Numbers of rows want to be: "))
boll_will_typecast = int(input("Enter One(1) or Two(2): "))
lines_increse = 0
lines_decresed = num_lines + 1
for i in range(num_lines):
    lines_increse += 1
    lines_decresed -= 1
    if boll_will_typecast == 1:
        boll_will_typecast = bool(True)
    elif boll_will_typecast == 2:
        boll_will_typecast = bool(False)
    if boll_will_typecast == True:
        print("*" *lines_increse)
    elif boll_will_typecast == False:
        print("*" *lines_decresed)
