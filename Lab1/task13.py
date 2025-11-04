import random
number = random.randint(1, 100)
guess = None
while guess != number:
    guess = int(input("угадай число от 1 до 100: "))
    if guess > number:
        print("меньше")
    elif guess < number:
        print("больше")
print("угадано!")