#Tip Calculator
bill_amount = float(input("Enter the bill amount: $"))

tip_percentage = 0.20
tip_amount = bill_amount * tip_percentage

print("The tip amount is: $", round(tip_amount, 2))