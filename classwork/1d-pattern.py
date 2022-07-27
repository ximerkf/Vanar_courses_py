# DRAW this PATTERN iterative
# * * # * * # * * # ...

print("\n")
for x in range(1,21):
    if x % 3 == 0:
        print("# ", end="")
    else:
        print("* ", end="")
print("\n")

# DRAW this PATTERN iterative
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *
#       * * * * * * * * * *

print("\n")
for x in range(1,101):
    print("* ", end="")
    if x % 10 == 0:
        print()
print("\n")

# HW1:
# DRAW this PATTERN iterative
# * * * # # * * * # # * * * # # ...

print("\n")
for x in range(1,21):
    if x % 10 == 4 or x % 10 == 5 or x % 10 == 9 or x % 10 == 0:
        print("# ", end="")
    else:
        print("* ", end="")
print("\n")

# HW2:
# DRAW this PATTERN iterative
# *
# * *
# * * *
# * * * *
# * * * * *

print("\n")
y = 1
z = 0
for x in range(1,16):
    if x - z == y:
        print("* ")
        y += 1
        z = x
    else:
        print("* ", end="")
print("\n")