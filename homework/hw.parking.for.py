PARKING_PLACES = 7
FREE_PLACE = 5

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if FREE_PLACE == place_index:
        print("|   |", end="")    
    else:
        print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")


# ii.
# Так как нам нужно чтоб print в цикле for был без \n, мы заменили его
# на отсутсвие символов с помощью параметра end="".
# Поэтому, чтобы перенести следующий print вне цикла нам понадобился \n.
# Но так как между элементами в print по дефолту стоит пробел, при помощи 
# sep="" мы заменили разделяющий элементы символ с пробела на ничего :)