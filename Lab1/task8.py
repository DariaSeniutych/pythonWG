text = input("введи строку: ").lower()
reversed_text = text[::-1]

if text == reversed_text:
    print("это палиндром")
else:
    print("это не палиндром")