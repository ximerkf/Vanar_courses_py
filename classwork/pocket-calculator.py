#interactive calculator

# CLI - text terminal 

# * input values
# * operations: +,-,/,*
# * show result
# * interactive menu

# + print formating

from os import system

system("cls")

while True:

    answer = input("Again? (y/n)\n")
    system("cls")
    if answer != "y":
        break
    

    operand_1 = int(input("> "))
    operation = input("> ")
    operand_2 = int(input("> "))

    system("cls")

    result = 0

    if operation == "+":
        result = operand_1 + operand_2
    if operation == "-":
        result = operand_1 - operand_2
    if operation == "*":
        result = operand_1 * operand_2
    if operation == "/":
        result = operand_1 / operand_2

    print(f"{operand_1:20}\n{operation:>20}\n{operand_2:20}\n--------------------\n{result:20}")