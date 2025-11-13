import numpy as np
expenses = np.array([
    1200,  # январь
    1100,  # февраль
    900,   # март
    800,   # апрель
    750,   # май
    1500,  # июнь
    1600,  # июль
    1550,  # август
    900,   # сентябрь
    850,   # октябрь
    1000,  # ноябрь
    1300   # декабрь
])

winter_indices = [11, 0, 1]
winter_sum = np.sum(expenses[winter_indices])

summer_indices = [5, 6, 7]
summer_sum = np.sum(expenses[summer_indices])

print("Зимние месяцы (декабрь, январь, февраль):")
print(f"Расходы: {winter_sum} руб")
print("Летние месяцы (июнь, июль, август):")
print(f"Расходы: {summer_sum} руб")
print()

if winter_sum > summer_sum:
    print("Больше денег тратится на проезд ЗИМОЙ")
elif summer_sum > winter_sum:
    print("Больше денег тратится на проезд ЛЕТОМ")
else:
    print("Расходы на проезд зимой и летом одинаковы")

max_expense = np.max(expenses)
# np.where возвращает кортеж, берем первый элемент и +1 для нумерации с 1
max_months = np.where(expenses == max_expense)[0] + 1

print(f"\n Максимальные расходы: {max_expense} руб")
print(f" Номера месяцев с максимальными расходами: {max_months.tolist()}")