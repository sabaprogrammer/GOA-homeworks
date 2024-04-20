# input() ფუნქციის დახმარებით მომხმარებელს შემოაქვს ორი რიცხვი a და b.  შექმენით ცარიელი სია. for ციკლის და range() ფუნქციის გამოყენებით ახალ სიაში  დაამატეთ ყველა რიცხვი რომელიც a და b რიცხვებს შორისაა ( range(a, b) ).append() ფუნქციის დახმარებითშედეგი გამოიტანეთ ტერმინალში


a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))


numbers_list = []


for num in range(a, b):
    numbers_list.append(num)


print("Numbers between", a, "and", b, ":", numbers_list)