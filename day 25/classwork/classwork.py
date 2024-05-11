# movie = ['12', '13', '14']
# movie.append('19')   #append cahamteba
# movie.insert(3,'marker')   #insert chasma
# movie.pop(2)    #pop  amoshla
# print(len(movie))   #lenght  datvla
# print(movie)

# list_1 = ['1', '2', '3']
# list_2 = ['4','5', '6']
# list_1.append(list_2)
# print(list_1)


# def bmi(weight,height):
#     index = weight /(height * height)
#     bmi = (12,123)
#     return(index)

def shipping_cost(weight):
    return weight * 5

weight = int(input("Enter weight in kg: "))
cost = shipping_cost(weight)
print(cost)