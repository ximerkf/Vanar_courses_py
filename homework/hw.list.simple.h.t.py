clients = ["John","Marry","Kate"]
clientsHighPriority = ["Tob","Pete"]
clientsLowPriority = ["Vicky","Lessly"]

for i in range(len(clientsHighPriority)):
    clients.insert(i,clientsHighPriority[i])

for n in clientsLowPriority:
    clients.append(n)

for i in range(len(clients)):
    print(i+1,". ",clients[i], sep="")