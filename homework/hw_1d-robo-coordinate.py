# HW1: input length/roboX (done)
#     *check limits (done)
# HW3: 
#   + add "hp", default:100% or hearts, when bomb - % or hearts
#   + game over  -> hp == 0 
#   + show hp
#   + healing
#   + many bombs
#   + limits (a) teleport or b) stop on boards )
#   + charge
#   + coins 
#   + ! jumps
# HW4: 1d robo game print map -> "for in"

# a - move left
# d - move right
# x - exit game

###################### IMPORT  ######################
from os import system
from random import randint
###################### IMPORT  ######################

###################### START DATA  ##################
length = 15#int(input("Choose your length: "))
roboX = 1#int(input("Choose your robot step: "))
bombX1 = randint(1,length/3)
bombX2 = randint(length/3+1,length-length/3)
bombX3 = randint((length-length/3)+1,length)
moneybagX = randint(1,length)
heartsX = 5
heartsAttack = 5
moneyscore = 0
charge = 100
###################### START DATA  ##################

if roboX > length or roboX < 0:
    print("Wrong data")
else:
    while True:
        system("cls")

        ###################### GAME STATUS  ##################
        # if charge < 0 and moneyscore>=100:
        #     charge =100
        #     moneyscore -=100
        # if charge < 0 and heartsAttack>0: #
        #     charge =100
        #     heartsAttack -=1
        if roboX == bombX1 or roboX == bombX2 or roboX == bombX3:
            heartsAttack -=1
        if heartsAttack == 0:
            print("Game Over!")
            break
        if roboX == moneybagX:
            moneyscore +=100
            bombX1 = randint(1,length/3)
            bombX2 = randint(length/3+1,length-length/3)
            bombX3 = randint((length-length/3)+1,length)
            moneybagX = randint(1,length)
            while bombX1 == moneybagX or bombX2 == moneybagX or bombX3 == moneybagX or roboX == bombX1 or roboX == bombX2 or roboX == bombX3 or roboX == moneybagX:
                bombX1 = randint(1,length/3)
                bombX2 = randint(length/3+1,length-length/3)
                bombX3 = randint((length-length/3)+1,length)
                moneybagX = randint(1,length)
        ###################### GAME STATUS  ##################

        ###################### HERO STATUS ######################
        y = 1 
        print("\n")

        while y <= heartsX:
            if y > heartsAttack:
                h = "🖤"
            else:
                h = "💖"
            print(f"{h}", end="")
            y +=1

        m = "💰:"
        print(f"{m:>5}{moneyscore}", end="")
        c = "⚡:"
        print(f"{c:>5}{charge}", end="")
        ###################### HERO STATUS ######################

        ###################### DRAWING MAP ######################
        print("\n")

        for x in range(1,length+1):
            # HW2: optimize from HERE
            if x == roboX:
                r = "  🤖  "
            elif x == moneybagX:
                r = "  💰  "
            elif x == bombX1:
                r = "  💣  "
            elif x == bombX2:
                r = "  💣  "
            elif x == bombX3:
                r = "  💣  "
            else:
                r = "  ▬  "
            print(f"{r}", end="")
            # to HERE
            
        print("\n")
        ###################### DRAWING MAP ######################
    
        ###################### CONTROL     ######################
        d = 0
        while d == 0:
            direction = input("dir (a/d/aa/dd/ch/cc/x)> ")

            if direction == "a":
                if charge >=10:
                    roboX -= 1
                    charge -=10
                else:
                    print("No charge for that move!")
                    continue

            if direction == "aa":
                if charge >= 30:
                    roboX -= 2
                    charge -=30
                else:
                    print("No charge for that move!")
                    continue

            if direction == "d":
                if charge >=10:
                    roboX += 1
                    charge -=10
                else:
                    print("No charge for that move!")
                    continue

            if direction == "dd":
                if charge >= 30:
                    roboX += 2
                    charge -=30
                else:
                    print("No charge for that move!")
                    continue
            
            if direction == "ch":
                charge = 100
                heartsAttack -=1

            if direction == "cc" and moneyscore>=100:
                charge = 100
                moneyscore -=100

            if roboX <= 0:
                roboX += length
            elif roboX > length:
                roboX -= length
            d +=1

        if direction == "x":
            system("cls")
            print("Thank you for playing!!!")
            break
        ###################### CONTROL     ######################

