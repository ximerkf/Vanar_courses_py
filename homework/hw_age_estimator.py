from random import randint

n=1
while n <= 15:

    #age = int(input("Enter your year of birth "))

    age = randint(1850,2022)

    if 1900 <= age <=2022:
        print("Your age is", 2022-age)
        if 2022-age == 0:
            print("You are an embryo\n")
        elif 1<= 2022-age <=3:
            print("You are a baby\n")
        elif 4<= 2022-age <=9:
            print("You are a kid\n")
        elif 10<= 2022-age <=15:
            print("You are a teen\n")
        elif 16<= 2022-age <=18:
            print("You are an young\n")
        elif 19<= 2022-age <=50:
            print("You are an adult\n")
        elif 51<= 2022-age:
            print("You are an old\n")
    else:
        print("Your age should be",2022 - age,"\nSorry, it's imposible. You would be probably dead :(\n")

    n +=1
