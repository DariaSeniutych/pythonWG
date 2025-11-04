day = int(input("введи день рождения: "))
month = int(input("Введи месяц рождения: "))

if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    sign = "возерог"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "водолей"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    sign = "рыбы"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "овен"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "телец"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    sign = "близнецы"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    sign = "рак"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "лев"
elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
    sign = "дева"
elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
    sign = "весы"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "скорпион"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "стрелец"

else:
    sign = "неверная дата"

print(f"ваш знак зодиака: {sign}")