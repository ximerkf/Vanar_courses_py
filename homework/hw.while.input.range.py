from os import system

system("cls")

while True:
    answer = input("Do you want to start?(y/n)")

    if answer != "y":
        break

    system("cls")

    start_n = int(input("Enter start n position:"))
    end_n = int(input("Enter end n position:"))

    if start_n <= end_n:
        while start_n <= end_n:
            print(start_n)
            start_n += 1
    else:
        while start_n >= end_n:
            print(start_n)
            start_n -= 1