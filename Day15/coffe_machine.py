MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money" : 0
}


def display_report():
    """Displays the Report of Remaining Resources"""
    print("Water : ", resources["water"])
    print("Milk : ", resources["milk"])
    print("Coffee : ", resources["coffee"])
    print("Money : $", resources["money"])


def check_resource(user_choice):
    """Check For Resources Individually"""

    # Should have used for loop here, had a feeling I was missing something!
    if(resources["water"] <= MENU[user_choice]["ingredients"]["water"]):
        return "Sorry there is not enough water"

    elif(resources["milk"] <= MENU[user_choice]["ingredients"]["milk"]):
        return "Sorry there is not enough milk"

    elif(resources["coffee"] <= MENU[user_choice]["ingredients"]["coffee"]):
        return "Sorry there is not enough coffee"
        
    else:
        return "enough"


def check_money(user_choice, money):
    if(money >= MENU[user_choice]["cost"]):
        return True
    else:
        return False


def update_resources(user_choice):
    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    resources["money"] += MENU[user_choice]["cost"]


def make_coffee(user_choice):
    
    # Check for resources
    if(check_resource(user_choice) == "enough"):
        quarters = int(input("Enter Quarters : "))
        dimes = int(input("Enter Dimes : "))
        nickles = int(input("Enter Nickles : "))
        pennies = int(input("Enter Pennies : "))

        money = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

        if(check_money(user_choice, money)):

            print(f"Here is your {user_choice}. Enjoy!")
            update_resources(user_choice)
            money_change = round(money - MENU[user_choice]["cost"], 2)
            if(money_change > 0):
                print(f"And here is your ${money_change} dollars in change")
                
        else:
            print("Sorry that's not enough money. Money Refunded")
    else:
        print(check_resource(user_choice))


user_choice = input("What would you like? (espresso/latte/cappuccino): ")

while(user_choice != "off"):

    if(user_choice == "report"):
        display_report()
    else:
        make_coffee(user_choice)

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")