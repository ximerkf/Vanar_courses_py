east = 4      # meters
south = 3     # meters 
west = 2      # meters
north = 5     # meters

total_path = east + south + west + north 
total_right = north - south 
total_down = east - west

print("Robo hoover made a path of", total_path, "meters")
print("Robo hoover moved down", total_path, "meters")
print("Robo hoover moved", total_path, "meters", "to the right")