# მომხმარებელს შემოაქვს რიცხვი. შეამოწმეთ არის თუ არა ეს რიცხვი მარტივი. თუ მარტიცია დაუპრინტეთ "თქვენი რიცხვი მარტივია", სხვა შემთხვევაში დაუპრინტეთ "თქვენი რიცხვი არ არის მარტივი"(მარტივი რიცხვი არის ისეთი ნატურალური რიცხვი რომელსაც გააჩნია მხოლოდ ორი გამოყოფი(1 და თავისი თავი))

number = int(input("Enter a number: "))


if number <= 1:
    is_prime = False
elif number <= 3:
    is_prime = True
elif number % 2 == 0 or number % 3 == 0:
    is_prime = False
else:
    is_prime = True
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            is_prime = False
            break
        i += 6


if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
