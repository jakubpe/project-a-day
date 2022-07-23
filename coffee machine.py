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

# TODO 1.print a report of machine resources
status = {'water': 100, 'milk': 50, 'coffee': 76, 'money': 0}
Water = status['water']
Milk = status['milk']
Coffee = status['coffee']
Money = status['money']
on = True
while on:
    make_coffee = False
    insert_coins = False
    choice = input("What coffee would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print('Water: {}ml\nMilk: {}ml\nCoffee: {}g\nMoney: {}$'.format(Water, Milk, Coffee, Money))
# TODO 2.end command to stop te machine
    elif choice == 'end':
        on = False
# TODO 3.check if there is enough ingredients in the machine
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if Water < MENU[choice]['ingredients']['water']:
            print('There is not enough water in the machine')
        elif Coffee < MENU[choice]['ingredients']['coffee']:
            print('There is not enough coffee in the machine')
        elif choice != 'espresso':
            if Milk < MENU[choice]['ingredients']['milk']:
                print('There is not enough milk in the machine')
        else:
            print("Please insert coins")
            insert_coins = True
# TODO 4.get the money
    if insert_coins:
        quarters = int(input('How many quarters?: '))
        dimes = int(input('How many dimes?: '))
        nickels = int(input('How many nickels?: '))
        pennies = int(input('How many pennies? :'))
        coins_sum = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
        if coins_sum > MENU[choice]['cost']:
            change = coins_sum - MENU[choice]['cost']
            print('Your change is: {}$'.format(change))
            make_coffee = True
        elif coins_sum < MENU[choice]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            make_coffee = True
# TODO 5.make coffee and actualize resources
    if make_coffee:
        Water = Water - MENU[choice]['ingredients']['water']
        Coffee = Coffee - MENU[choice]['ingredients']['coffee']
        Money = Money + MENU[choice]['cost']
        if choice != 'espresso':
            Milk = Milk - MENU[choice]['ingredients']['milk']
        print("Here is your {}. Enjoy!".format(choice))
