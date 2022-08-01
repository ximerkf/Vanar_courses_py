guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]

guests = guests_1 + guests_2 + guests_3

final_guests = []

for g in guests:
    if final_guests.count(g) == 0:
        final_guests.append(g)

final_guests.sort()

for i in range(len(final_guests)):
    print(i+1,". ", final_guests[i], sep="")
