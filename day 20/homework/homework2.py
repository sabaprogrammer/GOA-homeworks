#2)  შექმენით ცარიელი სია. მომხმარებელს შეეკითხეთ სახელი და გვარი, რომელსაც დაამატებთ თქვენ მიერ შექმნილ სიაში. საბოლო შედეგი გამოიტანეთ ტერმინალში

name_list = []


first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")


name_list.append((first_name, last_name))

print("Names added to the list:", name_list)