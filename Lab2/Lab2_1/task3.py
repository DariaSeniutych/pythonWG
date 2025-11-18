chisla = input("введи числа через пробел: ")
parts = chisla.split()

numbers = []
for x in parts:
    if '.' in x:
        numbers.append(float(x))
    else:
        numbers.append(int(x))

max1 = numbers[0]
max2 = None

for n in numbers:
    if n > max1:
        max1 = n

for n in numbers:
    if n < max1:
        if max2 is None or n > max2:
            max2 = n

if max2 is None:
    print("второго по величине числа нет")
else:
    print("второе по величине число:", max2)