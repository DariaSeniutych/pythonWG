num = int(input("введи число: "))
if num % 7 == 0:
    print("магическое число!")
else:
    digits_sum = 0
    temp = num
    while temp > 0:
        digits_sum += temp % 10
        temp //= 10
    print(digits_sum)