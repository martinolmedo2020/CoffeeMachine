MENU = {
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

coins = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):" ✅
# TODO: 2. Turn off the Coffee Machine by entering off to the prompt. ✅
# TODO: 3. Print report. ✅
# TODO: 4. Check resources sufficient? ✅
# TODO: 5. Process coins. ✅
# TODO: 6. Check transaction successful? ✅
# TODO: 7. Make Coffee. ✅


def coffee_machine():
    on_machine = True
    money_in_machine = 0

    def check_resources(initial_resources, needed_resources):
        """Compare the value of two dictionaries and return True if the resources it's more than
        the needed resources"""
        for ingredient in needed_resources:
            if needed_resources[ingredient] > initial_resources[ingredient]:
                print(f"Sorry not enough {ingredient}")
                return False
        return True

    def update_resources(initial_resources, new_resources):
        """Subtract the new resources values from the initial resources"""
        for ingredient in new_resources:
            initial_resources[ingredient] -= new_resources[ingredient]

    def process_coins(list_coins):
        """Asks the user how many coins from a list of coins they want to put in and returns the total amount"""
        user_payment = 0
        print("Please insert coins.")
        for coin in list_coins:
            insert_coin = int(input(f"How many {coin}?: "))
            user_payment += list_coins[coin] * insert_coin
        return user_payment

    def check_transaction(cost, payment):
        if cost > payment:
            print("Sorry not enough money. Money refunded")
            return False
        elif payment > cost:
            change = payment - cost
            print(f"Here's your change: ${change:.2f}")
            print(f"Here's your {user_election} ☕ Enjoy!")
            return True
        else:
            print(f"Here's your {user_election} ☕ Enjoy!")
            return True

    def report():
        for resource in resources:
            print(f"{resource.title()}: {resources[resource]}")
        print(f"Money: ${money_in_machine:.2f}")

    while on_machine:
        user_election = input("What would you like? (espresso/latte/cappuccino): ")
        if user_election == "off":
            on_machine = False
        elif user_election == "report":
            report()
        else:
            coffee_choice = MENU[user_election]
            coffee_ingredients = coffee_choice['ingredients']
            coffee_cost = coffee_choice['cost']
            if check_resources(resources, coffee_ingredients):
                if check_transaction(coffee_cost, process_coins(coins)):
                    update_resources(resources, coffee_ingredients)
                    money_in_machine += coffee_cost


coffee_machine()
