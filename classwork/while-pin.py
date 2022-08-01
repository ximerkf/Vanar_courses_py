# allow user > enter PIN > true
# HW: stop loop after 3 wrong attempts

correct_PIN = 1234
wrong = True
wrong_answers = 0

while wrong:
    user_PIN = int(input("Enter PIN: "))
    if user_PIN == correct_PIN:
        print("Yes!")
        wrong = False
    else:
        print("Wrong!")
        wrong_answers += 1
        if wrong_answers == 3:
            print("Sorry you  have already exhausted your attempts limit to dial the PIN!")
            wrong = False