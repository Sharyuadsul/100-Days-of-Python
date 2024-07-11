menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
stop_machine = False


def resources_enough(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry..there is not enough {item} to make your order.")
            return False
    return True


def coins():
    print("Please Insert the Coins: ")
    quarts = int(input("How many Qarters: "))
    dimes = int(input("How many Dimes: "))
    nickels = int(input("How many Nickels: "))
    penny = int(input("How many Pennys: "))
    return (quarts*0.25) + (dimes*0.10) + (nickels*0.05) + (penny*0.01)


def tran_successful(choice):
    total = coins()
    cost = menu[choice]["cost"]
    global profit
    if total == cost:
        profit += cost
        return True
    elif total < cost:
        print("Sorry..not enough money inserted. Money Refunded")
        return False
    else:
        change = round(total-cost,2)
        print(f"here is the change ${change}")
        profit += cost
        return True


def make_coffee(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"Here is Your ☕{drink}. Enjoy!")


while not stop_machine:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        stop_machine = True
    elif choice == "report":
        print("The remaining resources: ")
        print(f"water : {resources["water"]}ml")
        print(f"milk : {resources["milk"]}ml")
        print(f"coffee : {resources["coffee"]}g")
        print(f"money : ${profit}")
    elif choice == "espresso" or "latte" or "cappuccino":
        order = menu[choice]
        if resources_enough(menu[choice]["ingredients"]):
            if tran_successful(choice):
                make_coffee(choice,menu[choice]["ingredients"])
    else:
        print("Enter Valid Input!")








