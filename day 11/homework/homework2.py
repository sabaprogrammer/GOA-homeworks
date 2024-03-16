#3 დავალება For loop დახმარებით ეცადეთ, რომ სიტყვა დაპრინტოთ საპირისპირო მიმართულებით (სცადეთ და თუ არ გამოგივათ არაუშავს. )

word = "hello"
reversed_word = ""


for i in word:
    reversed_word = i + reversed_word
    
print(reversed_word)