def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            # проверяет количество количества аргументов
            if len(args) != len(types):
                raise TypeError(
                    f"Ожидалось {len(types)} аргументов, получено {len(args)}"
                )
            # проверяет тип каждого аргумента
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(
                        f"Аргумент {i+1} имеет неверный тип: "
                        f"получено {type(args[i]).__name__}, "
                        f"ожидалось {types[i].__name__}, "
                        f"значение = {args[i]!r}"
                    )
            return func(*args)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(10, 20))    # корректный вызов
print(add(10, "20"))  # вызовет ошибку
