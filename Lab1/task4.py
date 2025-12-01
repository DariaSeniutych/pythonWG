summa = int(input("введи сумму в рублях, целым числом: "))

hundred = summa // 100
summa %= 100
fifty = summa // 50
summa %= 50
ten = summa // 10
summa %= 10
five = summa // 5
summa %= 5
two = summa // 2
summa %= 2
one = summa

print("купюр по 100: ", hundred)
print("купюр по 50: ", fifty)
print("купюр по 10: ", ten)
print("купюр по 5: ", five)
print("монет по 2: ", two)
print("монет по 1: ", one)