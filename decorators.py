# Add decorators here


def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print('Something after')
    return wrapper


def check_vowels(func):
    def wrapper():
        if 'aiuoe'.find(word[0]) != -1:
            article = 'an'
        else:
            article = 'a'
        func()
        return wrapper

