password = input("введи свой пароль: ")

if len(password) < 16:
    print("слишком короткий")
elif password.isdigit() or password.isalpha():
    print("слабый пароль")
else:
    print("надежный пароль")