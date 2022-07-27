#TASK:
# i. ship place from keyboard
# ii. small_ship to big_ship 
# iii. change the code if/else for if big_ship=5 result is ~~~wWw~~~~

from os import system

system("cls")
while True:
    big_ship = int(input("Where is the ship? "))
    
    print()

    for x in range(1,11):
        if x == big_ship:
            print( "W", end="" )
        elif x - 1 == big_ship or x + 1 == big_ship:
            print( "w", end="" )
        else:
            print( "~", end="" )

    print("\n")

    while True:
        answer = input("Do you want to continue? (y/n) ")
        print()

        if answer == "y" or answer == "n":
            break
        else:
            print("Try again\n")
    if answer == "n":
        break
