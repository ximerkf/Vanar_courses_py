# python -> random 1..10
# player -> guess < hints
# limited tries
#BINARY SEARCH 

import random

N = random.randint(1,10)

for tries in range(1,6):
    n = int(input(str(tries) + ") GUESS? >> "))

    if n == N:
        print("YES :)\nYou won!")
        break
    elif n < N:
        print("Try greater")
    else:
        print("Try lesser")
if n != N:
    print("GAME OVER, you loose\nThe correct answer was:", N)