from CoffeeShop import CoffeeShop

run_simulation = True # boolean value to continue simulating or not
valid_response = False # boolean value to check if simulation months inputted is valid
name_given = False # boolean value to check if shop name is provided or not

# simulation keeps running until user inputs instructs to stop at the end of each loop
while run_simulation is True:

    # keeps asking for a shop name until user provides one; shop name can be any combination alphabets, numbers,
    # and or special characters
    while name_given is False:
        shop_name = input("Please enter your coffee shop name: ").strip().title()
        if shop_name!="":
            name_given = True
        else:
            print("No name was given!")

    # keeps asking for the number of months to simulate until a valid response is given; if no response or trailing
    # spaces is provided then default value of 6 is taken
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

    bankrupt = False # boolean value to stop simulation loop if insufficient cash to pay expenses

    # initiating object
    Coffeeshop = CoffeeShop(shop_name)
    # option to maximise income
    Coffeeshop.maximise_income()

    # simulating months with CoffeeShop methods
    for month in range(no_of_simulation_months):
        month += 1
        # setting month number
        Coffeeshop.set_month(month)
        # printing header
        Coffeeshop.print_header()
        # selecting barista and their specialities
        Coffeeshop.select_barista()
        # attending the coffee demand for each coffee types
        Coffeeshop.attend_coffee_demand()
        # paying utilities/rent, ingredient costs and barista costs
        bankrupt = Coffeeshop.pay_expenses()
        # message for the user to know the month when gone bankrupt
        if bankrupt is True:
            print(f"Went bankrupt in month {month}")
            print("")
            break

    run_simulation_response = False # boolean value to check if valid response is given to continue with another simulation
    positive_response = ["Y","Yes"]
    negative_response = ["N","No"]

    # keeps asking whether to continue with another simulation until a valid response is provided
    while run_simulation_response is False:
        run_simulation = input("Would you like to run another simulation? Y/N: ").strip().title()
        if run_simulation in positive_response:
            run_simulation = True
            valid_response = False
            run_simulation_response = True
        elif run_simulation in negative_response:
            run_simulation = False
            run_simulation_response = True
        else:
            print("Please enter a valid response!")
