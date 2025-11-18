def flatten_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            sublist = lst.pop(i) #удаляем вложенный список
            flatten_list(sublist) #выравниваем его с помощью рекурсии
            for item in reversed(sublist): #обратно вставляем в то же место
                lst.insert(i, item)
        else:
            i += 1
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)