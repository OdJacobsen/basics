# Testing decorators
from decorators import my_decorator


@my_decorator
def say_whee():
    print('Whee!')

say_whee()
