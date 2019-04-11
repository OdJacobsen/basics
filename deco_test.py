# Testing decorators
from decorators import *
import math
''

@timer
def say_whee():
    print('Whee!')


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        print(sum([i**2 for i in range(10000)]))


# waste_some_time(999)

@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Whoa {name}! {age} already, you are growing up!'


# make_greeting('Thomas', age=112)

math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


# approximate_e(5)


@slowdown
def countdown(from_number):
    if from_number < 1:
        print('Liftoff!')
    else:
        print(from_number)
        countdown(from_number - 1)


# countdown(10)

# Plugins
import random
PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f'Hello {name}'


@register
def be_awesome(name):
    return f'Hey, {name}, you are awesome!'


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f'Using {greeter!r}')
    return greeter_func(name)


print(PLUGINS)
randomly_greet('Alice')
