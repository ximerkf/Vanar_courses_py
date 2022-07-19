PIN_DOOR_1 = "0123"
PIN_DOOR_2 = "1234"

pin_door_1 = input("Enter PINCODE 1: ")
lock_1_open = pin_door_1 == PIN_DOOR_1

if lock_1_open:
    print("Entered the building!")

    pin_door_2 = input("Enter PINCODE 2: ")
    lock_2_open = pin_door_2 == PIN_DOOR_2

    if lock_2_open:
        print("Entered the flat!")
    else:
        print("Something is wrong with your PINCODE from the flat!")

else:
    print("Something is wrong with your PINCODE from the building!")
