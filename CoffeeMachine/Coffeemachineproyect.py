A simulator of a coffee machine that can ask what drink you want, count the money you give them and make your drink. It has a 

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

power=True
money=0
def check_ingredient(cafe):
    '''It makes sure there are enough ingredients, reports if that's not the case, and discounts the ingredients used.'''
    for key in resources:
        if key in MENU[cafe]['ingredients']:
            if resources[key]<=MENU[cafe]['ingredients'][key]:
                print(f"Sorry there is not enought {key}")
            elif resources[key]>=MENU[cafe]['ingredients'][key]:
                resources2={}
                resources2[key]=resources[key]-MENU[cafe]['ingredients'][key] 
                resources.update(resources2)
    return resources
            
def total_coins(cafe):
    '''It counts the coins that are delivered to the machine, accumulates the winnings and returns the change.'''
    coins=[]
    quarters=int(input("How many quarters?: "))
    coins.append(0.25*quarters)
    dimes=int(input("How many dimes?: "))
    coins.append(0.10*dimes)
    nickles=int(input("How many nickles?: "))
    coins.append(0.05*nickles)
    pennies=int(input("How many pennies?: "))
    coins.append(0.01*pennies)
    coins=round(sum(coins), 2)
    if coins>=MENU[cafe]['cost']:
        print(f"Here is ${round(coins-MENU[cafe]['cost'], 2)} in change.")
        return money + MENU[cafe]['cost']
    else:
        print("Sorry, that\'s not enough money. Money refunded.")

while power==True:
# Ask for your drink, consider ingredients and money, make the drink. With the "report" 
# command it prints the remaining ingredients and the money collected, with the "off" 
# command it turns off.
    bebida=input("What would you like? (espresso/latte/cappuccino): ")
    if bebida=='espresso' or bebida=='latte' or bebida=='cappuccino':
        resources=check_ingredient(bebida)
        money=total_coins(bebida)
        print(f"Here is your {bebida}.")
    elif bebida=='report':
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}ml")
        print(f"Money: ${round(money, 2)}")
    elif bebida=='off':
        power==False
    else:
        print("Invalid input.")
    
