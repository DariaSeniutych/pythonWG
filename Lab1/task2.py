s = input("введи строку: ")
vowels = "aeiouAEIOU"
translator = str.maketrans('', '', vowels)
result = s.translate(translator)
print("результат:", result)