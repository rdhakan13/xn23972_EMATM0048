# SDPA Coursework (xn23972_EMATM0048)

The work in the following repository is for the SDPA Summative Assessment.


## Part 1 - Coffee Shop Simulation
The purpose of this code is to simulate the operations of a coffee shop for a select number of months as inputted by the user. The coffee shop has fixed demand for each of the coffee type it sells, which require set ingredients and labour hours from set number of baristas. The goal of the coffee shop is to make a profit and avoid going bankrupt.

### Code Design
The code contains 5 classes and 1 main file through which the code will run. The 5 classes are as such:
1. `Supplier` - this class stores the following attributes of a supplier: name, price per quantity for each of the three ingredients (milk, beans and spices). The methods in this class retrieve the attribute values. 
2. `Barista` - this class stores the following attributes of a barista: name, coffee type in which they have speciality, hours they work, hours paid for and the rate per hour. The methods in this class can: retrieve all the attribute values, set values for name and speciality and increase/reset the number of hours worked.
3. `Ingredient` - this class stores the following attributes of an ingredient: name, maximum capacity that can be held by the coffee shop, rate of depreciation of the ingredient over time, pantry cost, quantity utilised over a month and the leftover quantity. The methods in this class can: retrieve all the attribute values, increase/reset quantity used over a month and calculate the cost to restock the ingredient to its full capacity at the end of each month. 
4. `CoffeeType` - this class stores the following attributes of a coffee type: name, quantity of each ingredient required to make the coffee, time to prepare the coffee, monthly demand for the coffee, selling price, quantity sold each month and the name of baristas who specialise in making the coffee. The methods in the class can: retrieve all the attributes, add/remove baristas who specialise, increase/reset quantity sold each month and check if there are sufficient supplies to make this coffee.
5. `CoffeeShop` - this class stores following attribute of a coffee shop: name, number of months to simulate the coffee shop for, monthly rent, a dictionary of all coffee types sold, a dictionary of all ingredients required, a dictionary of suppliers, cash held, a dictionary of baristas. The main methods in this class can: add/remove baristas and set their specialities, assign hours of work to baristas, collect income by selling each coffee types, pay expenses and restock the ingredients to full capacity. 

The design of the code was to ensure minimal coding takes place within the main.py file so that the high level logic can be simply presented and understood.

### About the program
The program runs as such:
- Prompts user to enter coffee shop name
- Prompts user to enter the number of months to simulate, if no response is given then a default value of 6 is taken
- Prompts user to enter the number of baristas to add or remove
- If barista is added the program prompts user to enter the name of the barista, and if they contain any specialities then to enter the name of the coffee type
- Prompts user to enter the number of coffees to serve for each coffee type and alerts the user if there is sufficient supplies (both labour hours and ingredient quantities available) to meet the requested demand. Else an error message informs the user the maximum capacity and the limiting factor causing it.
- The coffee shop uses the entered information and calculates the cash at the end of the month after paying all the expenses. 
- Prompts user to select supplier to restock ingredients. If at any point in paying expenses, there is insufficient cash, then the program terminates the simulating informing the user which expense was unfulfilled and by how much.
- If all expenses are paid then the program continues to the next month or prompts the user to run another simulation. 

The program has been extended in 2 ways to aid the decision making of the user simulating the coffee shop:
1. Barista's who have speciality in coffee making can prepare the speciality in half the required preparation time of that coffee, therefore, saving labour hours
2. Coffee types are arranged via the maximise_income method in the CoffeeShop class which sorts the coffee types based most income generating per unit of preparation time to the least and therefore addresses the time limitation posed by the number of baristas hired. This makes the user prioritize the demands of coffee and also hires baristas with specialities accordingly.

### How to run the program
To run the simulation, first open the terminal and navigate to the directory of the Part-1 folder. Then type the below line:
```
python main.py
```
To terminate or stop the program in the middle of the simulation: `ctrl+C`

## Part 2 - Exploratory Data Analysis

[yfinance](https://github.com/ranaroussi/yfinance) is an open source Python library built by Ran Aroussi. It is a code to fetch market data from Yahoo Finance's API. This library is used to fetch income statement values and Recommendation Scores from analysts for each stock.  

To install `yfinance`, ensure you have a minimum of Python 3.4. Install `yfinance` using `pip`:
```
pip install yfinance
```
