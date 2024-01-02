"""Raj Dhakan (xn23972) | Part-1 | main.py is the file through which the shop simulation must run"""

from CoffeeShop import CoffeeShop

RUN_SIMULATION = True # boolean value to continue simulating or not
VALID_RESPONSE = False # boolean value to check if simulation months inputted is valid
NAME_GIVEN = False # boolean value to check if shop name is provided or not

# simulation keeps running until user inputs instructs to stop at the end of each loop
while RUN_SIMULATION is True:

    # keeps asking for a shop name until user provides one; shop name can be any combination
    # alphabets, numbers, and no special characters
    CHARACTERS = '"!@#$%^&*()~|\;:}{]{£.-+?_=,<>/'
    EXCEPTION = "'"
    while NAME_GIVEN is False:
        shop_name = input("Please enter your coffee shop name: ").strip().title()
        if (shop_name=="" or any(char in CHARACTERS for char in shop_name) or any(char in EXCEPTION for char in shop_name)):
            print("Please enter a name with no special characters!")
        else:
            NAME_GIVEN = True

    # keeps asking for the number of months to simulate until a valid RESPONSE is given; if no
    # RESPONSE or trailing spaces is provided then default value of 6 is taken
    while VALID_RESPONSE is False:
        no_of_simulation_months = input(
            "Please enter number of months to simulate the coffee shop (default is 6): ")
        if no_of_simulation_months.strip()=="":
            no_of_simulation_months = 6
            VALID_RESPONSE = True
        else:
            try:
                no_of_simulation_months = int(no_of_simulation_months)
                if no_of_simulation_months > 0:
                    VALID_RESPONSE = True
                else:
                    print("Please enter a positive integer")
            except ValueError:
                print("Please enter a positive integer")

    BANKRUPT = False # boolean value to stop simulation loop if insufficient cash to pay expenses

    # initiating object
    Coffeeshop = CoffeeShop(shop_name)

    # option to maximise income, ask users to enter coffee demand in order of most income generating
    Coffeeshop.maximise_income()

    # simulating months with CoffeeShop methods
    for month in range(no_of_simulation_months):

        month += 1

        # setting month number
        Coffeeshop.set_month(month)

        # printing header
        Coffeeshop.print_header()

        # selecting barista and their specialities
        RESPONSE = False # boolean used to check if number of baristas entered is valid
        # if there are no baristas, as is at the beginning, user is only prompted to add baristas
        if not Coffeeshop.get_chosen_baristas():
            while RESPONSE is False:
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
                            name, barista = Coffeeshop.add_barista()
                            # user is prompted if barista has any coffee making speciality
                            Coffeeshop.select_speciality(name, barista)
                        print("")
                        RESPONSE = True
                except ValueError:
                    print("Please enter a positive integer!")
        else:
            # if there are already barista, as with the case with month 2 onwards, then the option
            # of removing baristas becomes valid and also to make no change
            while RESPONSE is False:
                try:
                    print("To add barista(s) enter a positive integer (e.g. 2), to remove barista(s)")
                    add_or_remove = int(input("enter a negative integer (e.g. -2), no change enter '0': "))
                    # if decides to add barista
                    if add_or_remove > 0:
                        # checks if no more than 4 baristas
                        if (add_or_remove + len(Coffeeshop.get_chosen_baristas())) > 4:
                            print(f"The shop can only take a maximum of 4 baristas at a time, currently there are {len(Coffeeshop.get_chosen_baristas())}!")
                        else:
                            print("")
                            for i in range(abs(add_or_remove)):
                                # adds barista
                                name, barista = Coffeeshop.add_barista()
                                # prompts user if new barista has any speciality in any of the coffee types
                                Coffeeshop.select_speciality(name, barista)
                            print("")
                            RESPONSE = True
                    # if user decides to remove baristas
                    elif add_or_remove < 0:
                        # checks if there will be at least one barista
                        if (add_or_remove + len(Coffeeshop.get_chosen_baristas())) <= 0:
                            print(f"The shop must have at least 1 barista, currently there are {len(Coffeeshop.get_chosen_baristas())}!")
                        else:
                            print("")
                            for i in range(abs(add_or_remove)):
                                # removes barista
                                Coffeeshop.remove_barista()
                            print("")
                            RESPONSE = True
                    else:
                        print("")
                        RESPONSE = True
                except ValueError:
                    print("Please enter an integer")

        # loops through each coffee to set demand
        for coffee in list(Coffeeshop.get_coffee_types().values()):
            # boolean used to check if demand values are valid
            RESPONSE = False 
            # boolean used to check if demand entered can be met with available baristas &
            # ingredient quantities
            SUFFICIENT_SUPPLY = False 
            # loop ends when RESPONSE is valid and demand can be met by available supply of baristas
            # and ingredients
            while RESPONSE is False or SUFFICIENT_SUPPLY is False:
                try:
                    demand = int(input(f"Coffee {coffee.get_name()}, demand {coffee.get_mon_dem()}, how much to sell: "))
                    if demand > coffee.get_mon_dem():
                        # if input value is greater than requested demand, error message is printed
                        print(f"Please do not exceed the demand of {coffee.get_mon_dem()}!")
                    elif demand >=0:
                        # checks supplies by calling on check_supply method from CoffeeType class
                        SUFFICIENT_SUPPLY = coffee.check_supply(demand, Coffeeshop.get_chosen_baristas(), Coffeeshop.get_ingredients())
                        RESPONSE = True
                        rem = 0  # remainder variable used when the total time to prepare the
                        # demanded coffee is split between two or more baristas
                        # if supplies are sufficient, only then baristas hrs are increased
                        if SUFFICIENT_SUPPLY is True:
                            if len(coffee.get_speciality_staff_list())>0:
                                # if there are speciality staff dedicated to the type of coffee in
                                # the LOOP then it loops through the list
                                rem = Coffeeshop.assign_demand(rem, coffee, demand, coffee.get_speciality_staff_list(), True)
                                # if there isn't a speciality staff in line, it assigns time to any
                                # other barista
                                Coffeeshop.assign_leftover_demand(rem, list(Coffeeshop.get_chosen_baristas().keys()))
                            # if there are no speciality staff at all
                            else:
                                # loops through the normal staff list first
                                rem = Coffeeshop.assign_demand(rem, coffee, demand, Coffeeshop.get_all_normal_staff_name(), False)
                                # if there isn't a barista that is normal, then it loops through
                                # all speciality staff which is not for coffee type in the LOOP
                                # (i.e. if a barista specialising in latte is can be assigned time
                                # to fulfill demand for filter coffee)
                                Coffeeshop.assign_leftover_demand(rem, Coffeeshop.get_all_speciality_staff_name())
                                # if remainder (rem) is zero then it suggests that there no normal
                                # baristas, or baristas with coffee making speciality to the
                                # coffeetype currently in LOOP, therefore it loops direct
                                if len(Coffeeshop.get_all_normal_staff_name())==0:
                                    rem = Coffeeshop.assign_demand(rem, coffee, demand, Coffeeshop.get_all_speciality_staff_name(), False)
                            # updates the quantity used by each ingredient
                            for ingredient in list(Coffeeshop.get_ingredients().values()):
                                ingredient.increase_quantity_used(demand,coffee)
                            # updates the quantity sold within the coffeetype class
                            coffee.increase_sold_quantity(demand)
                    else:
                        print("Please enter an integer greater than or equal to 0!")
                except ValueError:
                    print("Please enter an integer greater than or equal to 0!")

        # below system breaks loop at any place where there is insufficient cash to pay up expense
        # and prints out error message informing owner exactly which expense is unpayable and how 
        # much is lacking collecting income from selling coffee
        Coffeeshop.collect_coffee_income()
        # paying monthly rent
        print("")
        print("Expenses:")
        BANKRUPT = Coffeeshop.pay_monthly_rent()
        if BANKRUPT is True:
            print(f"Went BANKRUPT in month {month}")
            print("")
            break
        else:
            # payying baristas
            BANKRUPT = Coffeeshop.pay_baristas()
            if BANKRUPT is True:
                print(f"Went BANKRUPT in month {month}")
                print("")
                break
            else:
                # paying pantry costs
                BANKRUPT = Coffeeshop.pay_pantry_costs()
                if BANKRUPT is True:
                    print(f"Went BANKRUPT in month {month}")
                    print("")
                    break
                else:
                    # printing ingredient quantity and cash status
                    print("")
                    Coffeeshop.print_status()
                    # restocking ingredient and paying up supplier
                    print("")
                    BANKRUPT = Coffeeshop.restock_ingredients()
                    if BANKRUPT is True:
                        print("")
                        print(f"Went BANKRUPT in month {month}")
                        print('--------------------------------------------------------------------------')
                        print("")
                        break
                    else:
                        print("")
                        print("All expenses have been paid!")
                        print("All ingredients have been fully restocked.")
                        print('--------------------------------------------------------------------------')
                        print(f"MONTH {month} FINAL BALANCE: {Coffeeshop.get_current_cash():.2f}")
                        print('--------------------------------------------------------------------------')
                        print("")

    # boolean value to check if valid RESPONSE is given to continue with another simulation
    RUN_SIMULATION_RESPONSE = False 
    positive_RESPONSE = ["Y","Yes"]
    negative_RESPONSE = ["N","No"]

    # keeps asking whether to continue with another simulation until a valid RESPONSE is provided
    while RUN_SIMULATION_RESPONSE is False:
        RUN_SIMULATION = input("Would you like to run another simulation? Y/N: ").strip().title()
        if RUN_SIMULATION in positive_RESPONSE:
            RUN_SIMULATION = True
            VALID_RESPONSE = False
            RUN_SIMULATION_RESPONSE = True
            print("")
        elif RUN_SIMULATION in negative_RESPONSE:
            RUN_SIMULATION = False
            RUN_SIMULATION_RESPONSE = True
        else:
            print("Please enter a valid RESPONSE!")
