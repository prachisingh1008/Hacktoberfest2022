number = int(input("Enter a number: "))
flag = True
if number > 1:
    for i in range(2,number//2 + 1):
        if number % i == 0:
            flag = False
            break
    if flag:
        print("prime")
    else:
        print("Not Prime")
else:
    print("Not Prime")
