#3 დავალება შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს დადებითი მთელი რიცხვი, შექმნილ ცვლადში რომლის სახელიც არის num, შემდეგ გგამოითვალოს და დაბეჭდოს ყველა რიცხვის ჯამინ 1-დან num-მდე


num = int(input("Enter integer: "))


numbers = 0


if num <= 0:
    print("number must be greater than 0.")
else:
    for i in range(1, num + 1):
        numbers += i


    print(f"sum of all numbers from 1 to {num} is {numbers}.")