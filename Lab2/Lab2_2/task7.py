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

a = [1, 3, 5]
b = [2, 4, 6]
print(merge_sorted_lists(a, b))