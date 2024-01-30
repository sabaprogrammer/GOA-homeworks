name = "saba"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "saba" არის ცვლადისთვის მნიშვნელობა
surname = "chikvaidze"

print(name)
#სპრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი
name = "saba"  #ეს არის  str (string) ტიპის ცვლადი
age = 15 #ეს არის int (integer) მთელი რიცხვი
height = 180 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი
 
knows_programming = True #true ან false
is_ugly = False   #snakecase (უბრალოდ წერის სტილი სტანდარტულად)
isugly = False   #ჯავასკრიპტული camelcase

print(name + " " + surname)

#სტრინგი არის ბრჭყალებში ჩასმული სიმბოლოები
print(name + age)
print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))

print(name + " " + str(age))
