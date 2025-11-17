def merge_sorted_lists(list1, list2):
    resultat = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            resultat.append(list1[i])
            i += 1
        else:
            resultat.append(list2[j])
            j += 1

    while i < len(list1):
        resultat.append(list1[i])
        i += 1

    while j < len(list2):
        resultat.append(list2[j])
        j += 1

    return resultat

numbers1 = input("Введите первый отсортированный список чисел через пробел: ")
numbers2 = input("Введите второй отсортированный список чисел через пробел: ")

list1 = [int(x) for x in numbers1.split()]
list2 = [int(x) for x in numbers2.split()]

result = merge_sorted_lists(list1, list2)

print("Объединённый отсортированный список:", result)
