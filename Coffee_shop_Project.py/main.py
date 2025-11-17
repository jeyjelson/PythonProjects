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
    "money" : 0
}

#prompt user what you would like,The prompt should show every time action has completed
def display_prompt():
    choice = input("What would you like? (espresso/cappucino/latte) :").lower()
    if choice == "off":
        active = False
        return
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money €{resources['money']}")
    else:
        return choice


def resources_required(choice):
    if choice == "latte":
        for i in MENU['latte']['ingredients']:
            if resources[i] <= (MENU['latte']['ingredients'][i]):
                print(f"sorry there is not enough {i}")
                return
        process_coins(choice)
    elif choice == "cappuccino":
        for i in MENU['cappuccino']['ingredients']:
            if resources[i] <= (MENU['cappuccino']['ingredients'][i]):
                print(f"sorry there is not enough {i}")
                return
        process_coins(choice)
    elif choice == "espresso":
        for i in MENU['espresso']['ingredients']:
            if resources[i] <= (MENU['espresso']['ingredients'][i]):
                print(f"sorry there is not enough {i}")
                return
        process_coins(choice)


def process_coins(drink):
    two_euro = int(input("Please Enter Coins:\n€2 coins: "))
    one_euro = int(input("€1 coins : "))
    fifty_cent = int(input("50c coins : "))
    twenty_cent = int(input("20c coins : "))
    ten_cent = int(input("10c coins : "))

    sum =  two_euro * 2  + one_euro * 1 + fifty_cent * 0.5 + twenty_cent * 0.2 + ten_cent * 0.1
    if sum >= MENU[drink]['cost']:
        print(f"Thank you\nHere is your change : €{round(sum -MENU[drink]['cost'], 2)}")
        resources["money"] +=  MENU[drink]["cost"]
        return resources["money"]

    else:
        print("Sorry not enough change, Money Refunded")

active = True
while active:
    resources_required(display_prompt())


#Make Coffee. 