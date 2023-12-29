from CoffeeShop import CoffeeShop

run_simulation = True # boolean value to continue simulating or not
valid_response = False # boolean value to check if simulation months inputted is valid
name_given = False # boolean value to check if shop name is provided or not

# simulation keeps running until user inputs instructs to stop at the end of each loop
while run_simulation is True:

    # keeps asking for a shop name until user provides one; shop name can be any combination alphabets, numbers,
    # and no special characters
    characters = '"!@#$%^&*()~|\;:}{]{£.-+?_=,<>/'
    exception = "'"
    while name_given is False:
        shop_name = input("Please enter your coffee shop name: ").strip().title()
        if shop_name=="" or any(char in characters for char in shop_name) or any(char in exception for char in shop_name):
            print("Please enter a name with no special characters!")
        else:
            name_given = True

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
    # Coffeeshop.maximiseIncome()

    # simulating months with CoffeeShop methods
    for month in range(no_of_simulation_months):

        month += 1

        # setting month number
        Coffeeshop.setMonth(month)

        # printing header
        Coffeeshop.printHeader()

        # selecting barista and their specialities
        response = False # boolean used to check if number of baristas entered is valid
        # if there are no baristas, as is at the beginning, user is only prompted to add baristas
        if not Coffeeshop.getChosenBaristas():
            while response is False:
                try:
                    no_of_baristas = int(input("Please enter the number of baristas to add: "))
                    if no_of_baristas > 4:
                        # if more than 4 baristas are asked to enter then error message is printed
                        print("The shop can only take a maximum of 4 baristas at a time!")
                    elif no_of_baristas <= 0:
                        # if no value is entered then user is prompted again
                        print("Please enter a positive integer!")
                    else:
                        print("")
                        for i in range(no_of_baristas):
                            name, barista = Coffeeshop.addBarista()
                            # user is prompted if barista has any coffee making speciality
                            Coffeeshop.selectSpeciality(name, barista)
                        print("")
                        response = True
                except ValueError:
                    print("Please enter a positive integer!")
        else:
            # if there are already barista, as with the case with month 2 onwards, then the option of removing
            # baristas becomes valid and also to make no change
            while response is False:
                try:
                    print("To add barista(s) enter a positive integer (e.g. 2), to remove barista(s)")
                    add_or_remove = int(input("enter a negative integer (e.g. -2), no change enter '0': "))
                    # if decides to add barista
                    if add_or_remove > 0:
                        # checks if no more than 4 baristas
                        if (add_or_remove + len(Coffeeshop.getChosenBaristas())) > 4:
                            print(f"The shop can only take a maximum of 4 baristas at a time, currently there are {len(Coffeeshop.getChosenBaristas())}!")
                        else:
                            print("")
                            for i in range(abs(add_or_remove)):
                                # adds barista
                                name, barista = Coffeeshop.addBarista()
                                # prompts user if new barista has any speciality in any of the coffee types
                                Coffeeshop.selectSpeciality(name, barista)
                            print("")
                            response = True
                    # if user decides to remove baristas
                    elif add_or_remove < 0:
                        # checks if there will be at least one barista
                        if (add_or_remove + len(Coffeeshop.getChosenBaristas())) <= 0:
                            print(f"The shop must have at least 1 barista, currently there are {len(Coffeeshop.getChosenBaristas())}!")
                        else:
                            print("")
                            for i in range(abs(add_or_remove)):
                                # removes barista
                                Coffeeshop.removeBarista()
                            print("")
                            response = True
                    else:
                        response = True
                except ValueError:
                    print("Please enter an integer")

        # loops through each coffee to set demand
        for coffee in list(Coffeeshop.getCoffeeTypes().values()):
            # boolean used to check if demand values are valid
            response = False 
            # boolean used to check if demand entered can be met with available baristas & ingredient quantities
            sufficient_supply = False 
            # loop ends when response is valid and demand can be met by available supply of baristas and ingredients
            while response is False or sufficient_supply is False:
                try:
                    demand = int(input(f"Coffee {coffee.getName()}, demand {coffee.getMonDem()}, how much to sell: "))
                    if demand > coffee.getMonDem():
                        # if input value is greater than requested demand, error message is printed
                        print(f"Please do not exceed the demand of {coffee.getMonDem()}!")
                    elif demand >=0:
                        # checks supplies by calling on checkSupply method from CoffeeType class
                        sufficient_supply = coffee.checkSupply(demand, Coffeeshop.getChosenBaristas(), Coffeeshop.getIngredients())
                        response = True
                        rem = 0  # remainder variable used when the total time to prepare the demanded coffee is
                        # split between two or more baristas
                        # if supplies are sufficient, only then baristas hrs are increased
                        if sufficient_supply is True:
                            if len(coffee.getSpecialityStaffList())>0:
                                # if there are speciality staff dedicated to the type of coffee in the LOOP
                                # then it loops through the list
                                rem = Coffeeshop.assignDemand(rem, coffee, demand, coffee.getSpecialityStaffList(), True)
                                # if there isn't a speciality staff in line, it assigns time to any other barista
                                Coffeeshop.assignLeftoverDemand(rem, list(Coffeeshop.getChosenBaristas().keys()))
                            # if there are no speciality staff at all
                            else:
                                # loops through the normal staff list first
                                rem = Coffeeshop.assignDemand(rem, coffee, demand, Coffeeshop.getAllNormalStaffName(), False)
                                # if there isn't a barista that is normal, then it loops through all speciality staff
                                # which is not for coffee type in the LOOP (i.e. if a barista specialising in latte is
                                # can be assigned time to fulfill demand for filter coffee)
                                Coffeeshop.assignLeftoverDemand(rem, Coffeeshop.getAllSpecialityStaffName())
                                # if remainder (rem) is zero then it suggests that there no normal baristas, or baristas
                                # with coffee making speciality to the coffeetype currently in LOOP, therefore it loops direct
                                if len(Coffeeshop.getAllNormalStaffName())==0:
                                    rem = Coffeeshop.assignDemand(rem, coffee, demand, Coffeeshop.getAllSpecialityStaffName(), False)
                            # updates the quantity used by each ingredient
                            for ingredient in list(Coffeeshop.getIngredients().values()):
                                ingredient.increaseQuantityUsed(demand,coffee)
                            # updates the quantity sold within the coffeetype class
                            coffee.increaseSoldQuantity(demand)
                    else:
                        print("Please enter an integer greater than or equal to 0!")
                except ValueError:
                    print("Please enter an integer greater than or equal to 0!")
        
        # below system breaks loop at any place where there is insufficient cash to pay up expense and prints out
        # error message informing owner exactly which expense is unpayable and how much is lacking
        # collecting income from selling coffee
        Coffeeshop.collectCoffeeIncome()
        # paying monthly rent
        print("")
        print("Expenses:")
        bankrupt = Coffeeshop.payMonthlyRent()
        if bankrupt is True:
            print(f"Went bankrupt in month {month}")
            print("")
            break
        else:
            # payying baristas
            bankrupt = Coffeeshop.payBaristas()
            if bankrupt is True:
                print(f"Went bankrupt in month {month}")
                print("")
                break
            else:
                # paying pantry costs
                bankrupt = Coffeeshop.payPantryCosts()
                if bankrupt is True:
                    print(f"Went bankrupt in month {month}")
                    print("")
                    break
                else:
                    # printing ingredient quantity and cash status
                    print("")
                    Coffeeshop.printStatus()
                    # restocking ingredient and paying up supplier
                    print("")
                    bankrupt = Coffeeshop.restockIngredients()
                    if bankrupt is True:
                        print("")
                        print(f"Went bankrupt in month {month}")
                        print('--------------------------------------------------------------------------')
                        print("")
                        break
                    else:
                        print("")
                        print("All expenses have been paid!")
                        print("All ingredients have been fully restocked.")
                        print('--------------------------------------------------------------------------')
                        print(f"MONTH {month} FINAL BALANCE: {Coffeeshop.getCurrentCash():.2f}")
                        print('--------------------------------------------------------------------------')
                        print("")

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
            print("")
        elif run_simulation in negative_response:
            run_simulation = False
            run_simulation_response = True
        else:
            print("Please enter a valid response!")
