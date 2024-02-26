resources={ #resources dictionary for making coffee
    "water":500,
    "milk":200,
    "coffee":100
}

menu={  #menu and ingredients for making coffe(in form of nested dictionary)
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":150
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":200
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "milk":18,
            "coffee":16
        },
        "cost":100
    },
}

def check_resources(order_ingredients): #function to check availability of available for making coffee
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():    #function for processing coins given by customer
    print("Please insert coins!")
    total=0
    coins_five=int(input("How many 5rs coin? "))
    coins_ten=int(input("How many 10rs coin? "))
    coins_twenty=int(input("How many 20rs coin? "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(money_received, coffee_cost): #function to check if enough money is given by customer of not
    if money_received>=coffee_cost:
        global sell
        sell += coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs {change} in change")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(coffee_name, coffee_ingredients):   #function to prepare coffee and decrease ingredients from resources
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} coffee. ☕ Enjoy!!")

sell=0  #initially no sell, so no any profit or loss

is_on=True  #flag for running while loop according to user order

while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino/report/off): ").lower() #for changing into lower case
    if choice=="off":   #for ending our loop
        print("Bye!")
        is_on=False
    elif choice=="report":  #will print report of available resources and money
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}")
        print(f"Money={sell}")
    else:   #will make coffee
        coffee_type=menu[choice]    #selecting coffee type using choice(entered by user) from menu dictionary
        print(f"Price of {choice} coffee is Rs {coffee_type['cost']}")
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
