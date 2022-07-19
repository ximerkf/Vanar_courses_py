from random import randint

n = 1

while n <=15:
    distance_km = randint(-20,200)

    print("The distance", distance_km, "km\nis:")

    if distance_km <=1:
        print(" - near \n")
    elif distance_km <= 10:
        print(" - close \n")
    elif distance_km <= 100:
        print(" - far \n")
    else:
        print(" - very far \n")

    n +=1