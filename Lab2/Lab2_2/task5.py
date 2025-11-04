def cache(func):
    kesh = {}
    def wrapper(*args):
        if args in kesh:
            return kesh[args]
        result = func(*args)
        kesh[args] = result
        return result
    return wrapper

@cache
def slow_add(a, b):
    return a + b
print(slow_add(2, 3))
print(slow_add(2, 3))