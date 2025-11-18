numbers1 = input("введи первый набор чисел через пробел: ")
numbers2 = input("введи второй набор чисел через пробел: ")

def innumbers(s):
    vremlist = s.split()
    numbers = []
    for x in vremlist:
        if '.' in x:
            numbers.append(float(x))
        else:
            numbers.append(int(x))
    return numbers

list1 = innumbers(numbers1)
list2 = innumbers(numbers2)

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
print("числа из обоих наборов:", common)

only1 = set1 - set2
print("числа только из первого набора:", only1)

only2 = set2 - set1
print("числа только из второго набора:", only2)

all_numbers = set1 | set2
print("все числа:", all_numbers)
