a = int(input("введи a: "))
b = int(input("введи b: "))

print(f"сумма: {a + b}")
print(f"разность: {a - b}")
print(f"произведение: {a * b}")
print(f"частное: {a / b if b != 0 else 'ошибка: деление на ноль'}")
print(f"остаток: {a % b if b != 0 else 'Ошибка: деление на ноль'}")
print(f"степень: {a ** b}")