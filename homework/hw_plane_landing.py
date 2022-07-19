# data
plane_altitude = 500    # meters
plane_speed    = 300    # km/hours
plane_free_tracks= True
wind_speed = 50         # km/hours
same_direction = False
plane_fuel = 1
plane_has_problems = False
# logic 
can_land = 100 < plane_altitude < 700 and 200 < plane_speed < 500 and plane_free_tracks and wind_speed < 100 and not same_direction\
    or 0 < plane_fuel < 1 or plane_has_problems

# view
print( "Can the plane land? ", can_land )

print("Plane altitude =", plane_altitude, "meters")
print("Plane speed =", plane_speed, "km/hours")
print("Does the airport has free tracks?", plane_free_tracks)
print("Wind speed =", wind_speed, "km/hours")
print("Do the plane and wind have the same direction?", same_direction)
print("Plane fuel =", plane_fuel, "%")
print("Does the plane has problems?", plane_has_problems)