# DRAW this PATTERN ITERATIVE IN 2D:
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * R * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *

print("\n")

roboX = 3
roboY = 3

for y in range(1,11):
    ################## ROW ###################
    for x in range(1,11):
        if x == roboX and y == roboY:
            print("R ", end="")
        else:
            print("* ", end="")
    print()
    ################## ROW ###################

print("\n")

#HW: 