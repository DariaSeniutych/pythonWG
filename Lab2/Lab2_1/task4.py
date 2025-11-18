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

common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print("числа из обоих наборов:", common)

only1 = []
for x in list1:
    if x not in list2 and x not in only1:
        only1.append(x)

only2 = []
for x in list2:
    if x not in list1 and x not in only2:
        only2.append(x)

print("числа только из первого набора:", only1)
print("числа только из второого набора:", only2)

all = []
for x in list1:
    if x not in common and x not in all:
        all.append(x)

for x in list2:
    if x not in common and x not in all:
        all.append(x)

print("все числа:", all)