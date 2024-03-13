num_1 = 10
num_2 = 9

print(num_1 >= num_2) #true
print(num_1 <= num_2) #false
print(num_1 != num_2) #true
print(num_1 == num_2) #false

if num_1 != num_2:
    print("yes")
else:
    print("no")
    
if num_1 == num_2:
    print("yes")
else:
    print("no")

#Iteration, Sequencing, Selection = Flowchart
    
    for i in range(3):
     print("hello")

for i in range(1, 3):
     print(i)

     for num in range(1, 10, 2):
      print(num)

      start = 1
      range_ = 10
      step = 2
      for i in(start, range_, step):
         print(i)