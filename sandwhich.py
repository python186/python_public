
def main():
    meals = []

    ingredient_prices = {'white': 0.50, 'wheat': .55, 'sourdough': .60, 'chicken': 1, 'turkey': 1.25, 'lamb': 1.5,
                         'tofu': 1.75,
                         'cheddar': .20, 'swiss': .25, 'mozzarella': .3, 'mayo': .1, 'mustard': .11, 'lettuce': .12,
                         'tomato': .13}

    sandwich_count = pyip.inputInt("How many sandwiches would you like? ", min=1)
    for i in range(sandwich_count):
        meal_one = build_sandwich()
        # x = build_sandwich()
        meals.append(meal_one)



        outputs(meals, meal_one, ingredient_prices, i + 1)

    restart = pyip.inputYesNo("Do you want to restart this program? ")
    if restart == 'yes':
        main()
    else:
        print("Have a good day.")




    return meals, ingredient_prices



def build_sandwich():

    meal_one = []



    print("pick your bread.")
    bread_type = pyip.inputMenu(['white', 'wheat', 'sourdough'], numbered=True)
    meal_one.append(bread_type)

    print("Pick your protein.")
    protein_type = pyip.inputMenu(['chicken', 'turkey', 'lamb', 'tofu'], numbered=True)
    meal_one.append(protein_type)

    cheese = pyip.inputYesNo('Would you like cheese?')
    if cheese == 'yes':
        print("What type of cheese would you like? ")
        cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True)
        meal_one.append(cheese_type)

    else:
        print("Ok.")

    mayo = pyip.inputYesNo('Would you like mayo?')
    if mayo == 'yes':
        meal_one.append('mayo')

    mustard = pyip.inputYesNo('Would you like mustard?')
    if mustard == 'yes':
        meal_one.append('mustard')

    lettuce = pyip.inputYesNo('Would you like lettuce?')
    if lettuce == 'yes':
       meal_one.append('lettuce')

    tomato = pyip.inputYesNo('Would you like tomato?')
    if tomato == 'yes':
       meal_one.append('tomato')

    #print(meal_one)




    return meal_one


# def processing(meal_one):
#
#     total = 0
#     for items in meal_one:
#         total = sum(meal_one)


def outputs(meals, items ,meal_one_value,ingredient_prices_value):
    # print(meal_one_value)
    # print(ingredient_prices_value)
    total = 0
    print(f'{'Ingredients':<15}{"":>5}{"Prices":>7}')
    for ingredients in meal_one_value:
        print(f'{ingredients:<15} {"$":>5}{ingredient_prices_value[ingredients]:>7}')
        total = sum(ingredient_prices_value.values())
        print('This is your total',total)


        # for ingredients in meal_one_value:




main()
