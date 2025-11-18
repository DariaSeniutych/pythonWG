def unique_elements(spisok):
    vse_elementy = []

    def raskryt(x):
        if type(x) == list:
            for item in x:
                raskryt(item)
        else:
            vse_elementy.append(x)

    raskryt(spisok)

    resultat = []
    for item in vse_elementy:
        if item not in resultat:
            resultat.append(item)

    return resultat

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))