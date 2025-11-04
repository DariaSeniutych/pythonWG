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
    if type(n) == int:
        if n % 2 == 0:
            chet.append(n)
        else:
            nechet.append(n)
print("чётные числа:", chet)
print("нечётные числа:", nechet)

otricatelnue = []
for n in numbers:
    if n < 0:
        otricatelnue.append(n)
print("отрицатльные числа:", otricatelnue)

floats = []
for n in numbers:
    if type(n) == float:
        floats.append(n)
print("числа с плавающей точкой:", floats)

kratn5 = 0
for n in numbers:
    if type(n) == int and n % 5 == 0:
        total = kratn5 + n
print("сумма чисел, кратных 5:", kratn5)

biggest = numbers[0]
for n in numbers:
    if n > biggest:
        biggest = n
print("самое большое число:", biggest)

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("самое маленькое число:", smallest)