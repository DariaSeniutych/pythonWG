# создаем класс дорожные знаки, от него соответсвенно есть разные виды дорожных знаков.
# у каждого знака есть свой номер, название и описание того, что этот знак подразумевает.
# пользователь выбирает категорию знаков, добавляет соответсвующий знак с его описанием
# и это все должно сохранятся в отдельный текстовый файл.
#  также надо продемонстрировать процесс наследования классов
# в каждой главе берем по два-три знака, не больше
#напиши прям очень-очень простой код, но выполняя все мои требования


class RoadSighs:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def info(self):
        return f"Знак {self.number}: {self.name}"


class Preduprezhdayushiy(RoadSighs):
    pass

class Signs_of_prioretets(RoadSighs):
    pass

class Zapreshchayushiy(RoadSighs):
    pass

class Predpisyvayushiy(RoadSighs):
    pass

signs = [
    Preduprezhdayushiy("1.1", "Железнодорожный переезд со шлагбаумом"),
    Preduprezhdayushiy("1.2", "Железнодорожный переезд без шлагбаумом"),

    Signs_of_prioretets("2.1", "Главная дорога"),
    Signs_of_prioretets("2.2", "Конец главной дороги"),

    Zapreshchayushiy("3.1", "Въезд запрещён"),
    Zapreshchayushiy("3.2", "Движение запрещено"),

    Predpisyvayushiy("4.1", "Движение прямо"),
    Predpisyvayushiy("4.2", "Объезд препятствия справа")
]

print("1 — предупреждающие")
print("2 — знаки приоритета")
print("3 — запрещающие")
print("4 — предписывающие")
kategorya = input("выбери категорию 1/2/3/4: ")

if kategorya == "1":
    nachalo = 0
elif kategorya == "2":
    nachalo = 2
elif kategorya == "3":
    nachalo = 4
elif kategorya == "4":
    nachalo = 6
else:
    print("неправильный выбор")
    exit()

print("\n выбери знак:")
print("1.", signs[nachalo].name)
print("2.", signs[nachalo + 1].name)

vybor = input("номер знака (только 1 или 2): ")
if vybor == "1":
    vybrannyy_znak = signs[nachalo]
elif vybor == "2":
    vybrannyy_znak = signs[nachalo + 1]
else:
    print("неправильный выбор")
    exit()

with open("signs.txt", "a", encoding="utf-8") as f:
    f.write(vybrannyy_znak.info() + "\n")

print("знак добавлен в signs.txt")













# class RoadSighs:
#     def __init__(self):
#         pass
#
#     def signs_predyprezhdayushie(self):
#         pass
#
#     def signs_of_prioretets(self):
#         pass
#
#     def signs_zaprezhautie(self):
#         pass
#
#     def signs_predpisuvaushie(self):
#         pass
#
# class RoadSighs:
#     def __init__(self, number, name, opisanie):
#         self.number = number
#         self.name = name
#         self.opisanie = opisanie
#
#     def info(self):
#         return f"Знак {self.number}: {self.name} — {self.opisanie}"
#
# '''
#
#
#
''' signs = [
   Preduprezhdayushiy("1.1", "Железнодорожный переезд со шлагбаумом"),
   Preduprezhdayushiy("1.2", "Железнодорожный переезд без шлагбаумом"),

   Signs_of_prioretets("2.1", "Главная дорога"),
   Signs_of_prioretets("2.2", "Конец главной дороги"),

   Zapreshchayushiy("3.1", "Въезд запрещён"),
   Zapreshchayushiy("3.2", "Движение запрещено"),

   Predpisyvayushiy("4.1", "Движение прямо"),
   Predpisyvayushiy("4.2", "Объезд препятствия справа")
]'''
