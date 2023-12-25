from CoffeeShop import CoffeeShop

run_simulation = True
valid_response = False
name_given = False

while run_simulation is True:

    while name_given is False:
        shop_name = input("Please enter your coffee shop name: ")
        if shop_name.strip()!="":
            name_given = True

    while valid_response is False:
        no_of_simulation_months = input("Please enter number of months to simulate the coffee shop (default is 6): ")
        if no_of_simulation_months.strip()=="":
            no_of_simulation_months = 6
            valid_response = True
        else:
            try:
                no_of_simulation_months = int(no_of_simulation_months)
                if no_of_simulation_months > 0:
                    valid_response = True
                else:
                    print("Please enter a positive integer")
            except ValueError:
                print("Please enter a positive integer")

    bankrupt = False

    for month in range(no_of_simulation_months):
        month += 1
        Coffeeshop = CoffeeShop(shop_name, month)
        Coffeeshop.print_header()
        Coffeeshop.select_barista()
        Coffeeshop.attend_coffee_demand()
        bankrupt = Coffeeshop.pay_expenses()
        if bankrupt is True:
            print(f"Went bankrupt in month {month}")
            print("")
            break

    run_simulation_response = False
    positive_response = ["y","yes"]
    negative_response = ["n","no"]
    while run_simulation_response is False:
        run_simulation = input("Would you like to run another simulation? Y/N: ")
        if run_simulation.lower() in positive_response:
            run_simulation = True
            valid_response = False
            run_simulation_response = True
        elif run_simulation.lower() in negative_response:
            run_simulation = False
            run_simulation_response = True
        else:
            print("Please enter a valid response")
