seconds = int(input("введи количество секунд: "))
minutes = seconds // 60
ostatok = seconds % 60
print(f"{minutes} минут {ostatok} секунд")