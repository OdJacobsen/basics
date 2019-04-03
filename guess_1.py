from capitals import capitals_dict
from random import choice


def capital_guess(state, capital):
    while True:
        guess = input(f'Type the capital of the {state}?').lower()
        if guess == 'exit':
            print(f'The capital of the {state} is {capital}, Farewell')
            break
        elif guess == (capital).lower():
            print('good job!')
            break

# Convert the dict to a list in order to use random
state = choice(list(capitals_dict.keys()))
capital = capitals_dict[state]
capital_guess(state, capital)

