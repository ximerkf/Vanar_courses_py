# LIFT SIMULATION / realms simulation

#   * conditionals / looping / branching
#   * logic wrapping / inside-out
#   * logic sequences / connections

#   ---|-----|----
#    R |     |    
#   ---|     |----
#    9 |     |    
#   ---|     |----
#    8 |     |    
#   ---|     |----
#    7 |     |    
#   ---|     |----
#    6 |     |    
#   ---|     |----
#    5 |     |    
#   ---|     |----
#    4 |  ^  |    
#   ---||---||----
#    3 || H ||    
#   ---||---||----
#    2 |     |    
#   ---|     |----
#    1 |     |    
#   ---|     |----
#    P |     |    
#   ---|-----|----

from os import system

# LIFT STATE
DIR_UP = -1
DIR_STOPPED = 0
DIR_DOWN = 1

building_roof = True
building_floors = 9
building_parking = True

lift_floor = 3
lift_open = True
lift_dir = DIR_UP

human_floor = 3
human_in_lift = True
# LIFT STATE

# RENDER FRAME
#system("cls")

if building_roof:
    print("---|-----|----")
    print(" R |     |    ")

for floor in range(9,0,-1):
    print("---|     |----")
    print(f"{floor:^3}|     |    ")

if building_parking:
    print("---|     |----")
    print(" P |     |    ")
    print("---|-----|----")
# RENDER FRAME 
