# 1d game 
# ~~~~W~~x~~

w = 4
x = 2

while True:

    ####### RENDER MAP #######
    print()
    n = 1
    while n <= 10:
        if n == w:
            print("W ", end="") # "text\n"
        elif n == x:
            print("x ", end="")
        else:
            print("~ ", end="")
        n += 1
    print("\n")
    ####### RENDER MAP #######

    ####### INTERACTION #######
    # HW1: add limits conditions
    # HW2: add condition - mine, "BOOM!" and stop main loop
    direction = input("dir > (a,d): ")
    if direction == "a":
        if w == 1:
            pass
        else:
            w -= 1
    if direction == "d":
        if w == 10:
            pass
        else:
            w += 1
    
    if w == x:
        print("BOOM!")
        print("Game Over!")
        break
    ####### INTERACTION #######