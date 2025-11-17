#1. Уникальные числа.
#2. Повторяющиеся числа.
#3. Четные и нечетные чисел.
#4. Отрицательные чисел.
#5. Числа с плавающей точкой.
#6. Сумму всех чисел, кратных 5.
#7. Самое большое число.
#8. Самое маленькое число.



chisla = input("введи числа через пробел: ")
parts = chisla.split()

numbers = []
for x in parts:
    if '.' in x:
        numbers.append(float(x))
    else:
        numbers.append(int(x))

unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print("уникальные числа:", unique)

repeated = []
for n in numbers:
    if numbers.count(n) > 1 and n not in repeated:
        repeated.append(n)
print("повторяющиеся числа:", repeated)

chet = []
nechet = []
for n in numbers:
    if isinstance(n, int):  # проверяем только целые
        if n % 2 == 0:
            chet.append(n)
        else:
            nechet.append(n)
print("чётные числа:", chet)
print("нечётные числа:", nechet)

otricatelnue = [n for n in numbers if n < 0]
print("отрицательные числа:", otricatelnue)

floats = [n for n in numbers if isinstance(n, float)]
print("числа с плавающей точкой:", floats)

kratn5 = 0
for n in numbers:
    if isinstance(n, int) and n % 5 == 0:
        kratn5 += n
print("сумма чисел, кратных 5:", kratn5)

biggest = max(numbers)
print("самое большое число:", biggest)

smallest = min(numbers)
print("самое маленькое число:", smallest)
