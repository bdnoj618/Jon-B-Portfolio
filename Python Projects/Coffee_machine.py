# Three hot Flavors
# Espresso
# 50ml Water
# 18g Coffee
# $1.50

espresso = {
    'water': 50,
    'milk': 0,
    'coffee': 18,
    'money': 1.50,
}

# Latte
# 200ml Water
# 24g Coffee
# 150ml Milk
# $2.50
latte = {
    'water': 200,
    'milk': 150,
    'coffee': 24,
    'money': 2.50,
}
# Cappuccino
# 250ml Water
# 24g Coffee
# 100ml Milk
# 3.00
cappuccino = {
    'water': 250,
    'milk': 100,
    'coffee': 24,
    'money': 3.00
}

# Coffee Machine (make a dicitonary)
# 300ml of Water Capacity
# 200ml of Milk Capacity
# 100g of Coffee Capacity

coffee_machine = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

empty = False

# Coins
# Penny - 1
# Nickel - 5
# Dime - 10
# Quarter - 25
def coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * .01)

#function checks if there is enough in the coffee machine
def check(machine, type_coffee):
    if machine['water'] < type_coffee['water'] or machine['milk'] < type_coffee['milk'] or machine['coffee'] < type_coffee['coffee']:
        return True

is_on = True
print("Welcome to the Bruder Coffee Machine")

while is_on:
    coffee = input("What would you like? (Espresso/Latte/Cappuccino): ")
    coffee = coffee.lower()
    if coffee == "off":
        is_on = False
    elif coffee == "report":
        print(f"Water: {coffee_machine['water']}mL")
        print(f"Milk: {coffee_machine['milk']}mL")
        print(f"Coffee: {coffee_machine['coffee']}g")
        print(f"Money: ${coffee_machine['money']}")
    elif coffee == "espresso":
        #check if the machine is empty
        empty = check(coffee_machine, espresso)
        if empty == True:
            empty = True
            exit()
        print(f"An espresso is ${espresso['money']}")
        # The amount of money the customer put it
        customer_money = coins()
        coffee_machine['money'] += espresso['money']
        #checks to see if the customer put enough money it
        if customer_money < espresso['money']:
            print("You need more money to pay for your drink.")
            #ask if the user wants a refund
            refund = input("would you like a refund? 'Y' or 'N' ")
            refund = refund.lower()
            if refund == "y":
                #if coffee machine money is greater than zero
                coffee_machine['money'] -= customer_money
        print(f"${customer_money - espresso['money']} is your change.")
        print(f"Here is your {coffee}. Enjoy!")
        coffee_machine['water'] -= espresso['water']
        coffee_machine['milk'] -= espresso['milk']
        coffee_machine['coffee'] -= espresso['coffee']
    #Checks for the lattee
    elif coffee == "latte":
        empty = check(coffee_machine, latte)
        if empty == True:
            empty = True
            exit()
        print(f"An espresso is ${latte['money']}")
        # The amount of money the customer put it
        customer_money = coins()
        coffee_machine['money'] += latte['money']
        #checks to see if the customer put enough money it
        if customer_money < latte['money']:
            print("You need more money to pay for your drink.")
            #ask if the user wants a refund
            refund = input("would you like a refund? 'Y' or 'N' ")
            refund = refund.lower()
            if refund == "y":
                #if coffee machine money is greater than zero
                coffee_machine['money'] -= customer_money
        coffee_machine['water'] -= latte['water']
        coffee_machine['milk'] -= latte['milk']
        coffee_machine['coffee'] -= latte['coffee']
        print(f"${customer_money - latte['money']} is your change.")
        print(f"Here is your {coffee}. Enjoy!")
    elif coffee == "cappuccino":
        empty = check(coffee_machine, cappuccino)
        if empty == True:
            empty = True
            print("Sorry there is not enough")
            exit()
        print(f"An espresso is ${cappuccino['money']}")
        # The amount of money the customer put it
        customer_money = coins()
        coffee_machine['money'] += cappuccino['money']
        #checks to see if the customer put enough money it
        if customer_money < cappuccino['money']:
            print("You need more money to pay for your drink.")
            #ask if the user wants a refund
            refund = input("would you like a refund? 'Y' or 'N' ")
            refund = refund.lower()
            if refund == "y":
                #if coffee machine money is greater than zero
                coffee_machine['money'] -= customer_money
        coffee_machine['water'] -= cappuccino['water']
        coffee_machine['milk'] -= cappuccino['milk']
        coffee_machine['coffee'] -= cappuccino['coffee']
        print(f"${customer_money - cappuccino['money']} is your change.")
        print(f"Here is your {coffee}. Enjoy!")
    else:
        print("You entered the wrong input!")