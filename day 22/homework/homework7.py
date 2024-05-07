def check_number(num):
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("its 0")

number = int(input("enter a number: "))
check_number(number)

