### For future improvements:
    ### Find out who to continue asking for different capitals.
    ### Add a helper if the answer is wrong,
    ### telling the player the first letter of the capital

from capitals import countries_dict
from random import choice


def capital_guess(country, capital):
    while True:
        guess = input(f'Type the capital of the {country}?').lower()
        if guess == 'exit':
            print(f'The capital of the {country} is {capital}, Farewell')
            break
        elif guess == (capital).lower():
            print('good job!')
            break



# Convert the dict to a list in order to use random.choice
country = choice(list(countries_dict.keys()))
capital = countries_dict[country]
capital_guess(country, capital)

