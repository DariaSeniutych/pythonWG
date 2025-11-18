import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"функция {func.name} выполнилась за {(end - start) * 1000:.2f} мс")
        return result
    return wrapper

@timing
def slow_func():
    time.sleep(0.1)
    return "готово"
print(slow_func())