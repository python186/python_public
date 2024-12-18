
import requests
import pyinputplus as pyip
import json

def main():
    users_choice = pyip.inputMenu(['Add pizza', 'view order', 'submit'], numbered = True)

    if users_choice == 'Add pizza':
        add()





def add():

    total_pizzas = 0

    pizzas = []
    each_pizza = {}

    pizza_url = input('Please enter the pizza url here: ')

    requested_url = requests.get(pizza_url)
    json_url = requested_url.json()

    for base in json_url['base_options']:



        base_option = pyip.inputMenu(list(base['options']), numbered=True)              # I had put .values() after [options] to get price but there was an error

    for top in json_url['toppings']:

        topping = pyip.inputYesNo('Do you want', top)







    print(pizzas)


    return pizzas








main()
