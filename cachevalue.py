# this code will return the value of arguments if the function already has the value from a previous execution.

import time

def cache(func):
    cache_value = {}
    # print(cache_value) 
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result 
        return result
    return wrapper

@cache
def sum_func(a, b):
    time.sleep(5) 
    return a + b

print(sum_func(2,3))
print(sum_func(2,3))
print(sum_func(4,9)) 
