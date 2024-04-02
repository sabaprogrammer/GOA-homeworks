def check_student_score(score):
    if score == 10:
        print("კარგია, ასე გააგრძელე.")
    elif score == 8 or score == 9:
        print("თქვენი შვილი ნიჭიერია, მაგრამ ზარმაცობს.")
    elif score == 5:
        print("თქვენი შვილი საშინლად სწავლობს.")
    elif score < 5:
        print("თქვენი შვილი გაგდებულია სკოლიდან, რადგან არ სწავლობს.")
    


score = int(input("Enter your score: "))
check_student_score(score)