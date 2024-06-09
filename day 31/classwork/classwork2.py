def find_needle(haystack):
    if "needle" in haystack:
        return "found the needle at position" + " " + str(haystack.index("needle"))
    

list=[1,3,23,451,"needle"]
print(find_needle(list))