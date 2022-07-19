standard_toppings = ["mushrookms", "meat", "red peppers"]
requested_toppings = []
enter_topping=input("Enter name the topping: ")
requested_toppings.append(enter_topping.lower())

for requested_topping in requested_toppings:
    if requested_topping in standard_toppings:
        print("Added "+ requested_topping)
    else:
        print("Sorry, we don't have " + enter_topping)
