def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            if len(args) != len(types):
                raise TypeError("количество аргументов не совпадает")
            for i in range(len(args)):
                if type(args[i]) is not types[i]:
                    raise TypeError(f"аргумент {i+1} имеет неверный тип")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b
print(add(10, 20))
print(add(10, "20"))