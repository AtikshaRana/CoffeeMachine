import data

total_input = 0
water = data.resources["water"]
milk = data.resources["milk"]
total_coffee = data.resources["coffee"]
money = 0





def report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {total_coffee}")
    print(f"Money: {money}")


def enter_coin():
    global total_input
    total_input = 0
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    quarters /= 4
    dimes /= 10
    nickles /= 20
    pennies /= 100

    total_input = quarters + dimes + nickles + pennies

def update_report(coffee_cost, coffee):
    global money, water, milk, total_coffee
    money += coffee_cost
    water -= data.menu[coffee]["ingredients"]["water"]
    milk -= data.menu[coffee]["ingredients"].get("milk", 0)
    total_coffee -= data.menu[coffee]["ingredients"]["coffee"]


def make_coffee(coffee):
    global total_input
    coffee_cost = data.menu[coffee]["cost"]
    print(f"total_input : {total_input}")
    if total_input == coffee_cost:
        print(f"Here is your {coffee} ☕ Enjoy!")
        update_report(coffee_cost, coffee)
    elif total_input > coffee_cost:
        change = round(total_input - coffee_cost, 2)
        update_report(coffee_cost, coffee)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee} ☕ Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

def check_resources(coffee):
    water_needed = data.menu[coffee]["ingredients"]["water"]
    milk_needed = data.menu[coffee]["ingredients"].get("milk", 0)
    coffee_needed = data.menu[coffee]["ingredients"]["coffee"]

    if water >= water_needed and milk >= milk_needed and total_coffee >= coffee_needed:
        enter_coin()
        make_coffee(coffee)
    else:
        if water < water_needed:
            print("Water is not sufficient.")
        elif milk < milk_needed:
            print("Milk is not sufficient.")
        else:
            print("Coffee is not sufficient.")


# print(total_input)

def coffee_machine():
    flag = True
    while flag:
        what_you_want = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
        if what_you_want == 'report':
            report()
        else:
            check_resources(what_you_want)


coffee_machine()






