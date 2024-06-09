def grow(arr):
    result = 1
    for i in arr:
        result *=i
    return result
    

list=[4,2,3,4,5,6]
print(grow(list))
