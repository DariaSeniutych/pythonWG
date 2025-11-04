slovo = input("Введите строку: ")

if slovo == "":
    print("")
else:
    rezultat = ""
    tek_simvol = slovo[0]
    schet = 1

    for i in range(1, len(slovo)):
        if slovo[i] == tek_simvol:
            schet = schet + 1
        else:
            rezultat = rezultat + tek_simvol + str(schet)
            tek_simvol = slovo[i]
            schet = 1

    rezultat = rezultat + tek_simvol + str(schet)

    print(rezultat)