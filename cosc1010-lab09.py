# Nelia Koontz
# UWYO COSC 1010
# 11/17/2024
# Lab 09
# Lab Section: 15
# Sources, people worked with, help given to:
# Emmanuel and Python Crash Course book
# asked chat gpt to explain this code that I had written because I kept getting only cheese back: 
# def setToppings(self, *toppings):
# """set toppings method"""
# index = 0
# while len(toppings) < index:
#     for topping in toppings:
#         self.toppings.append(topping)
#         index +=1
# print(self.toppings)
# to which it replied the while loop was unneccessary, and I took it out, which fixed the problem
# except it appended as another list ["cheese" ["carrots", "fudge", "crayons"]]. I tried different things
# ways, and eventually, I moved the for loop to before calling the function, which worked OK.
# I also googled does every var in a class need to be called self, and I think I understand that 
# a little more. used the book, especially the chapter on classes. It took me a while to get the pizza to increment.
# this program does not check for a whole number because I didn't see in the rules that it needed to, so it will calculate
# whichever number, it just changes any input to 10 if it is below 10, and it does not check if it is a number so it will
# throw an error if it isn't a number.

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size#
# - Sauce#
# - Toppings, which should be a list#
# You need to create one method that corresponds with each of the above attributes#
# which returns the corresponding attribute, just the value.#
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)#
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.#
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.#
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).#
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.#
# - Assign the parameter for sauce to the attribute. #
# - Create the toppings attribute, starting off as a list only holding cheese.#

class Pizza:
    """a class to define a pizza"""
    def __init__(self, size, sauce = "red"):
        """initialize parameters"""
        if int(size) <= 10:
            self.size = 10
        else:
            self.size = int(size)
        self.sauce = sauce
        self.toppings = ["cheese"]

    def setSize(self, size):
        """set size method"""
        if int(size) <= 10:
            self.size = 10
        else:
            self.size = int(size)

    def setToppings(self, topping):
        """set toppings method"""
        self.toppings.append(topping)
    
    def getAmountOfToppings(self):
        """return amount of toppings list"""
        return len(self.toppings)

    def getSize(self):
        """return size"""
        return self.size

    def getSauce(self):
        """return sauce"""
        return self.sauce

    def getToppings(self):
        """return toppings"""
        topping_s = ''
        for topping in self.toppings:
            topping_s += '\t'
            topping_s += topping
            topping_s += '\n'
        return topping_s
              
# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizzeria:
    """a class that takes in orders for pizza"""
    def __init__(self):
        """initialize parameters"""
        self.orders = 0
        self.price_per_topping = 0.30
        self.price_per_inch = 0.60

    def placeOrder(self):
        """method that takes input for order"""
        self.topping_list = []
        self.size = input("Please enter the size of pizza, as a whole number. The smallest size is 10:")
        self.sauce = input("What kind of sauce would you like? \n leave blank for red sauce")
        if self.sauce == "":
            self.sauce = "red"
        print("Please enter the toppings you would like, leave blank when done")
        while True:
            self.topping = input()
            if self.topping == "":
                break
            else:
                self.topping_list.append(self.topping)
        self.new_pizza = Pizza(self.size, self.sauce)
        for item in self.topping_list:
            self.new_pizza.setToppings(item)

    def incrementOrders(self, order):
        """increments when new order is placed"""
        self.orders = order
  
    def getPrice(self):
        """determines price of pizza"""
        self.size_price = self.price_per_inch * self.new_pizza.getSize()
        self.topping_price = self.price_per_topping * self.new_pizza.getAmountOfToppings() 
        self.pizza_total = (self.new_pizza.getSize() * self.price_per_inch) + (self.new_pizza.getAmountOfToppings() * self.price_per_topping)

    def getReceipt(self):
        """prints receipt for pizza"""
        self.total_price = self.size_price + self.topping_price
        return print(f"You ordered a {self.new_pizza.getSize()} inch pizza with {self.new_pizza.getSauce()} sauce and the following toppings: \n {self.new_pizza.getToppings()}\n You ordered a {self.new_pizza.getSize()} inch pizza for ${self.size_price}\n You had {self.new_pizza.getAmountOfToppings()} toppings for ${self.topping_price}\n Your total price is ${self.pizza_total}\n")
    
    def getNumberOfOrders(self):
        """prints number of orders when finished"""
        return print(f"The total number of orders is {self.orders}")

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

index = 0
active = True
while active:
    my_pizza = Pizzeria()
    my_pizza.incrementOrders(index)
    order_in = input("Would you like to place an order? exit to exit")
    if order_in.lower() == 'exit':
        active = False
    else:
        my_pizza.placeOrder()
        my_pizza.getPrice()
        my_pizza.getReceipt()
        index += 1
my_pizza.getNumberOfOrders()


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""