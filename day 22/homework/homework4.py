def calculate_perimeter(side1, side2, side3, side4):
    perimeter =(side1 + side2 + side3 + side4)
    return perimeter


side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))
side4 = int(input("Enter the length of side 4: "))


print(calculate_perimeter(side1, side2, side3, side4))