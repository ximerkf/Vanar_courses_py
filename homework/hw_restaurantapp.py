# 1. Order

food_1_name      = 'Pizza'
food_1_price     = 100   
food_1_available = 5
food_1_quantity  = int(input('How many ' + food_1_name + ' do you want ? '))

food_2_name      = 'Burger'
food_2_price     = 150   
food_2_available = 10
food_2_quantity  = int(input('How many ' + food_2_name + ' do you want ? '))

drink_1_name      = 'Coca cola'
drink_1_price     = 50   
drink_1_available = 100
drink_1_quantity  = int(input('How many ' + drink_1_name + ' do you want ? '))

if 1<=food_1_quantity<=food_1_available and 1<=food_2_quantity<=food_2_available and 1<=drink_1_quantity<=drink_1_available:
    food_1_cost = food_1_quantity * food_1_price
    food_2_cost = food_2_quantity * food_2_price
    drink_1_cost = drink_1_quantity * drink_1_price
    total_cost = food_1_cost + food_2_cost + drink_1_cost
    print('You have ordered: \n'\
         + str(food_1_quantity) + ' x ' + food_1_name +'\n'\
         + str(food_2_quantity) + ' x ' + food_2_name +'\n'\
         + str(drink_1_quantity) + ' x ' + drink_1_name +'\n'\
         +'Total cost is ' + str(total_cost))

elif not 1<=food_1_quantity<=food_1_available:
    print("Don't have such quantity of Pizza. Choose less.")
    if not 1<=food_2_quantity<=food_2_available:
        print("Don't have such quantity of Burger. Choose less.")
        if not 1<=drink_1_quantity<=drink_1_available:
            print("Don't have such quantity of Coca cola. Choose less.")
    elif not 1<=drink_1_quantity<=drink_1_available:
        print("Don't have such quantity of Coca cola. Choose less.")

elif not 1<=food_2_quantity<=food_2_available:
    print("Don't have such quantity of Burger. Choose less.")
    if not 1<=drink_1_quantity<=drink_1_available:
        print("Don't have such quantity of Coca cola. Choose less.")

elif not 1<=drink_1_quantity<=drink_1_available:
    print("Don't have such quantity of Coca cola. Choose less.")

# 2. Delivery

delivery_free_limit = 1000
delivery_cost = 150

delivery_need = input("Do you want delivery? (yes/no) ")

if delivery_need == 'yes' and delivery_free_limit < total_cost:
    print("You have got free delivery.")
elif delivery_need == 'yes' and delivery_free_limit > total_cost:
    print("You have to pay for delivery", delivery_cost, "unless you add something to the order to make your price over", delivery_free_limit)
else:
    print("If you don't want to use delivery, we are waiting you in our restaurant!")