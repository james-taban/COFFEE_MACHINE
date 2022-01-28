# TODO 1 print out a report of the resources found in the machine

from resources import MENU, resources


def print_report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# TODO 2 bring out the different menus depending on the customer's choice

def coffee_water(choice, water1):
    if choice == "espresso":
        water1 = MENU["espresso"]["ingredients"]["water"]
        return water1
    elif choice == "latte":
        water1 = MENU["latte"]["ingredients"]["water"]
        return water1

    elif choice == "cappuccino":
        water1 = MENU["cappuccino"]["ingredients"]["water"]
        return water1


def coffee_coffee(choice, coffee1):
    if choice == "espresso":
        coffee1 = MENU["espresso"]["ingredients"]["coffee"]
        return coffee1
    elif choice == "latte":
        coffee1 = MENU["latte"]["ingredients"]["coffee"]
        return coffee1
    elif choice == "cappuccino":
        coffee1 = MENU["cappuccino"]["ingredients"]["coffee"]
        return coffee1


def coffee_milk(choice, milk1):
    if choice == "espresso":
        return 0
    elif choice == "latte":
        milk1 = MENU["latte"]["ingredients"]["milk"]
        return milk1
    elif choice == "cappuccino":
        milk1 = MENU["cappuccino"]["ingredients"]["milk"]
        return milk1

# TODO 3 Calculating the total amount of money based on the coins


def calculate_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    total_result = (nickels * 0.05) + (quarters * 0.25) + (dimes * 0.10) + (pennies * 0.01)
    return round(total_result, 2)


def coffee_shop():
    # Retrieving values from the resources tab
    water = resources["Water"]
    milk = resources["Milk"]
    coffee = resources["Coffee"]
    money = 0
    continue_order = True
    while continue_order:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            print_report(water, milk, coffee, money)
        elif choice == "off":
            continue_order = False
        else:
            water_customer = coffee_water(choice, water)
            milk_customer = coffee_milk(choice, milk)
            coffee_customer = coffee_coffee(choice, coffee)
            if water < water_customer:
                print("Sorry there is not enough water")
            elif coffee < coffee_customer:
                print("Sorry there is not enough coffee")
            elif milk < milk_customer:
                print("Sorry there is not enough milk")
            else:
                money_received = calculate_money()
                cost = MENU[choice]["cost"]
                balance = money_received - cost
                if balance < 0:
                    print("You have insufficient funds. Here is your refund")
                else:
                    print(f"Here is ${balance} in change.")
                    print(f"Here is your {choice} . Enjoy!")
                    money += cost
                    water -= water_customer
                    coffee -= coffee_customer
                    milk -= milk_customer


coffee_shop()
