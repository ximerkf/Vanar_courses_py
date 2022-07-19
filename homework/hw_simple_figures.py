figure = input("what figure to draw? ")

if figure == "line":
  print("-----")
elif figure == "square":
    print("-----\n|   |\n|   |\n-----")

    #print("-----")
    #print("|   |")
    #print("|   |")
    #print("-----")
elif figure == "parallel horizontal lines":
    print("-----\n-----")
    
    #print("-----\n")
    #print("-----")
elif figure == "parallel vertical lines":
    print("|   |\n|   |")
    
    #print("|   |")
    #print("|   |")
else:
  print("CAN'T DRAW SUCH FIGURE!")