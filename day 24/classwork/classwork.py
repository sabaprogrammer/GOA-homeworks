def solution(string):
    reversed_string=''
    for char in string: 
        reversed_string = char + reversed_string
    return reversed_string
    
print(solution('dato'))
print(solution('luka'))
print(solution('saba'))
print(solution('mate'))
print(solution('nika'))
print(solution('gio'))
