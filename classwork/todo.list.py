# APP / TODO - plan your tasks

# dynamic + batteries included

from os import system

# DATA

tasks = [
    "Learn Python",
    "Become a DEV"
]

menu = [
    "Add task",
    "Show tasks",
    "Remove task",
    "Clear TODO",
    "Exit TODO"
]

# DATA

# PRINT THE TASKS

#HW1: while True -> modify condition -> stop input ""
#HW2: 
#   make it fully interactive:
#   MENU: 1. add task, 2. show tasks, 3. remove task, 4. clear TODO, 5. exit the program

system("cls")

while True:
    # MENU
    print()
    print("TODO MENU:")
    for i in range(len(menu)):
        print("\t",i+1,") ",menu[i], sep="")
    print()
    # MENU/

    # INTERACTION
    command = input("Press your command: ")
    system("cls")
    if command == "1":
        new_task = input("Add task: ")
        system("cls")
        if new_task == "":
            continue
        elif new_task not in tasks:
            tasks.append(new_task)
        else:
            print("This task already exists!")
    
    if command == "2":
        print("TODO list (", len(tasks),"):")
        for i in range(len(tasks)):
            print("\t",i,">",tasks[i])

    if command == "3":
        print("TODO list (", len(tasks),"):")
        for i in range(len(tasks)):
            print("\t",i,">",tasks[i])
        rem_elem = input("Choose index of the element should be removed: ")
        system("cls")
        for i in range(len(tasks)):
            if rem_elem.isdigit():
                if int(rem_elem) == i:
                    print("The element","\"",i,tasks[i],"\"","has been removed.")
                    tasks.pop(int(rem_elem))
            elif i == len(tasks)-1:
                print("No such element")

    if command == "4":
        answer_remove_all = input("Are you sure you want to remove all the elements? (y/n) ")
        system("cls")
        if answer_remove_all == "y":
            tasks.clear()
            print("TODO has been removed")
        else:
            print("Back to MENU")

    if command == "5":
        print("See you soon!")
        break
    # INTERACTION
