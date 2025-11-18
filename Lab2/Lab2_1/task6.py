s = input("введи элементы списка через пробел: ")
parts = s.split()

clean = []
for x in parts:
    if x not in clean:
        clean.append(x)

print("список без дубликатов:", clean)