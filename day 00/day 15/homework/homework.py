#1 დავალება
def check_score(score):
    if score > 90 and score < 100:
        print("თქვენ დაგიფინანსდებათ სწავლა სრულიად.")
    elif score > 70 and score < 80:
        print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით.")
    elif score > 40 and score < 70:
        print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით.")
    elif score < 40:
        print("თქვენ არ დაგიფინანსდებათ სწავლა.")
 

score = int(input("Enter your test score: "))
check_score(score)
