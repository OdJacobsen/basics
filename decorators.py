# Add decorators here
# functools preserve the function identity
import functools
import time


def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Something before")
        func()
        print('Something after')
    return wrapper


# make this work somehow
def check_vowels(func):
    def wrapper():
        if 'aiuoe'.find(word[0]) != -1:
            article = 'an'
        else:
            article = 'a'
        func()
        return wrapper


# Decorator Template
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# Time functions
def timer(func):
    """time runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Do something before
        start_time = time.perf_counter() # 1
        value = func(*args, **kwargs)
        # Do something after
        end_time = time.perf_counter() # 2
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value
    return wrapper_timer


def debug(func):
    """
    Print the function signature and return value
    Showing arguments coming in and out of the function
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do something before
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f'{k} = {v!r}' for k, v in kwargs.items()]  # 2
        signature = ', '.join(args_repr + kwargs_repr)  # 3
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        # Do something after
        print(f'{func.__name__!r} returned {value!r}')  # 4
        return value
    return wrapper_debug


def slowdown(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        # Do something before
        time.sleep(1)
        return func(*args, **kwargs)
        # Do something after
    return wrapper_slow_down
