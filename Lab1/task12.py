minutes = int(input("колво минут: "))
sms = int(input("колво смс: "))
internet = float(input("инет в мб: "))

base = 39.99
extra = max(0, minutes - 60) * 0.89 + max(0, sms - 30) * 0.59 + max(0, internet - 1) * 0.79
total = (base + extra) * 1.02  # сразу с налогом 2%

print(f"базовая сумма: {base:.2f} руб.")
print(f"дополнительно: {extra:.2f} руб.")
print(f"налог: {(base + extra) * 0.02:.2f} руб.")
print(f"итого: {total:.2f} руб.")