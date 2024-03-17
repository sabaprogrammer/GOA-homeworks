#1 დავალება შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს, იქამდე უნდა შეეკითხოს სანამ პაროლი სწორი არ იქნება.

correct_password = "secretword"

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("acceess granted")
        break  
    else:
        print("access denied. Try again.")

#2 დავალება შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ ითვლის ამ რიცხვიდან 1-მდე.
input = input("enter a number that is greater than 0.: ")

number = int(input)

if number <= 0:
    print("")
else:
    for i in range(number, 0, -1):
        print(i)

