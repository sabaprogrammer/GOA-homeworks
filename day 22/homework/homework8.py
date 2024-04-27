def check_age(age):
    if age < 13:
        print("you are kid")
    elif 13 <= age <= 19:
        print("you are teenager")
    else:
        print("you are adult")


age = int(input("enter your age: "))
check_age(age)