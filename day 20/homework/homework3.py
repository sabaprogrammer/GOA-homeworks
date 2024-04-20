#მომხმარებელს შემოატანიეთ რიცხვი და for loop-ის დახმარებით დაპრინტეთ რიცხვები 1-დან  მომხმარებლის მიერ შემოტანილი რიცხვის ჩათვლით.ტერმინალში გამოიტანეთ ამ რიცხვების ჯამი და საშუალო არითმეტიკული
num = int(input("Please enter a number: "))


sum = 0
count = 0


for i in range(1, num + 1):
    print(i)
    sum += i
    count += 1


mean = sum / count


print("რიცხვთა ჯამი:", sum)
print("საშუალო არითმეტიკული:", mean)