# создаем класс дорожные знаки, от него соответсвенно есть разные виды дорожных знаков.
# у каждого знака есть свой номер, название и описание того, что этот знак подразумевает.
# пользователь выбирает категорию знаков, добавляет соответсвующий знак с его описанием
# и это все должно сохранятся в отдельный текстовый файл.
#  также надо продемонстрировать процесс наследования классов
# в каждой главе берем по два-три знака, не больше

'''
class RoadSign:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def info(self):
        return f"Знак {self.number}: {self.name}"


class Preduprezhdayushiy(RoadSign):
    pass


class Signs_of_prioretets(RoadSign):
    pass


class Zapreshchayushiy(RoadSign):
    pass


class Predpisyvayushiy(RoadSign):
    pass


signs = [
    Preduprezhdayushiy("1.1", "Железнодорожный переезд со шлагбаумом"),
    Preduprezhdayushiy("1.2", "Железнодорожный переезд без шлагбаума"),

    Signs_of_prioretets("2.1", "Главная дорога"),
    Signs_of_prioretets("2.2", "Конец главной дороги"),

    Zapreshchayushiy("3.1", "Въезд запрещён"),
    Zapreshchayushiy("3.2", "Движение запрещено"),

    Predpisyvayushiy("4.1", "Движение прямо"),
    Predpisyvayushiy("4.2", "Объезд препятствия справа")
]


def show_all_signs():
    where = input("вывести в? (t — терминал, f — файл): ").strip().lower()
    lines = [s.info() for s in signs]
    if where == "t":
        for line in lines:
            print(" -", line)
    elif where == "f":
        with open("signs1.txt", "a", encoding="utf-8") as f:
            f.write("\n все знаки: \n")
            for line in lines:
                f.write(line + "\n")
            f.write("\n")
        print("список добавлен в signs1.txt")
    else:
        print("неизвестный выбор")


def add_manual_sign():
    number = input("номер знака: ").strip()
    name = input("название: ").strip()
    cat = number.split('.')[0]
    if cat == "1":
        sign = Preduprezhdayushiy(number, name)
    elif cat == "2":
        sign = Signs_of_prioretets(number, name)
    elif cat == "3":
        sign = Zapreshchayushiy(number, name)
    elif cat == "4":
        sign = Predpisyvayushiy(number, name)
    else:
        print("неизвестная категория")
        return None
    signs.append(sign)
    return sign


def add_manual_sign():
    number = input("номер знака: ").strip()
    name = input("название: ").strip()
    cat = number.split('.')[0]

while True:
    print("1 — предупреждающие")
    print("2 — знаки приоритета")
    print("3 — запрещающие")
    print("4 — предписывающие")
    print("5 — добавить знак вручную")
    print("6 — показать все знаки")
    print("0 — выход")
    kategorya = input("выбери действие (0–6): ").strip()

    if kategorya == "0":
        print("выход")
        break

    if kategorya == "1":
        nachalo = 0
    elif kategorya == "2":
        nachalo = 2
    elif kategorya == "3":
        nachalo = 4
    elif kategorya == "4":
        nachalo = 6
    elif kategorya == "5":
        new_sign = add_manual_sign()
        if new_sign:
            with open("signs1.txt", "a", encoding="utf-8") as f:
                f.write(new_sign.info() + "\n")
            print("знак добавлен в signs1.txt")
        continue
    elif kategorya == "6":
        show_all_signs()
        continue
    else:
        print("неправильный выбор")
        continue

    print("\n выбери знак:")
    print("1.", signs[nachalo].name)
    print("2.", signs[nachalo + 1].name)

    vybor = input("номер знака (только 1 или 2): ").strip()
    if vybor == "1":
        vybrannyy_znak = signs[nachalo]
    elif vybor == "2":
        vybrannyy_znak = signs[nachalo + 1]
    else:
        print("неправильный выбор")
        continue

    with open("signs1.txt", "a", encoding="utf-8") as f:
        f.write(vybrannyy_znak.info() + "\n")

    print("знак добавлен в signs1.txt")
'''

# пользовательские искл
class InvalidSignNumberError(Exception):
   pass


class UnknownCategoryError(Exception):
  pass


class EmptyNameError(Exception):
  pass

class RoadSign:
    def __init__(self, number, name):
        if not number or '.' not in number:
            raise InvalidSignNumberError(number)
        if not name.strip():
            raise EmptyNameError()
        self.number = number.strip()
        self.name = name.strip()

    def info(self):
        return f"знак {self.number}: {self.name}"

    def __str__(self):
        return self.info()


class Preduprezhdayushiy(RoadSign):
    def __init__(self, number, name):
        super().__init__(number, name)
        self.category = "предупреждающие"


class Signs_of_prioretets(RoadSign):
    def __init__(self, number, name):
        super().__init__(number, name)
        self.category = "знаки приоритета"


class Zapreshchayushiy(RoadSign):
    def __init__(self, number, name):
        super().__init__(number, name)
        self.category = "запрещающие"


class Predpisyvayushiy(RoadSign):
    def __init__(self, number, name):
        super().__init__(number, name)
        self.category = "предписывающие"


try:
    signs = [
        Preduprezhdayushiy("1.1", "Железнодорожный переезд со шлагбаумом"),
        Preduprezhdayushiy("1.2", "Железнодорожный переезд без шлагбаума"),

        Signs_of_prioretets("2.1", "Главная дорога"),
        Signs_of_prioretets("2.2", "Конец главной дороги"),

        Zapreshchayushiy("3.1", "Въезд запрещён"),
        Zapreshchayushiy("3.2", "Движение запрещено"),

        Predpisyvayushiy("4.1", "Движение прямо"),
        Predpisyvayushiy("4.2", "Объезд препятствия справа")
    ]
except (InvalidSignNumberError, EmptyNameError) as e:
    print(f"ошибка при создании начальных знаков: {e}")
    signs = []


def show_all_signs():
    where = input("вывести в? (t — терминал, f — файл): ").strip().lower()
    if not signs:
        print("нет доступных знаков((")
        return
    lines = [s.info() for s in signs]
    try:
        if where == "t":
            print("\n все знаки:")
            for line in lines:
                print(line)
        elif where == "f":
            with open("signs1.txt", "a", encoding="utf-8") as f:
                f.write("\n все знаки:\n")
                for line in lines:
                    f.write(line + "\n")
                f.write("-" * 30 + "\n")
            print("список добавлен в signs1.txt")
        else:
            print("неизвестный выбор, нужно использовать либо 't', либо 'f'")
    except Exception as e:
        print(f"ошибка при записи в файл: {e}")


def add_manual_sign():
    try:
        number = input(" номер знака: ").strip()
        name = input(" название знака: ").strip()

        cat = number.split('.')[0]
        if cat == "1":
            sign = Preduprezhdayushiy(number, name)
        elif cat == "2":
            sign = Signs_of_prioretets(number, name)
        elif cat == "3":
            sign = Zapreshchayushiy(number, name)
        elif cat == "4":
            sign = Predpisyvayushiy(number, name)
        else:
            raise UnknownCategoryError(cat)

        signs.append(sign)


        with open("signs1.txt", "a", encoding="utf-8") as f:
            f.write(f"{sign.category}: {sign.info()}\n")
        print(f"знак '{sign.name}' добавлен и сохранён в файлик")
        return sign

    except (InvalidSignNumberError, EmptyNameError, UnknownCategoryError) as e:
        print(f"ошибка: {e}")
        return None
    except Exception as e:
        print(f"ошибка: {e}")
        return None



while True:
    print("\n Меню ")
    print("1 — Предупреждающие")
    print("2 — Знаки приоритета")
    print("3 — Запрещающие")
    print("4 — Предписывающие")
    print("5 — Добавить знак вручную")
    print("6 — Показать все знаки")
    print("0 — Выход")

    choice = input("Выберите действие (0–6): ").strip()

    if choice == "0":
        print("выход из программы")
        break

    try:
        if choice in ("1", "2", "3", "4"):
            category_map = {"1": 0, "2": 2, "3": 4, "4": 6}
            start_index = category_map[choice]

            print("\n выберите знак:")
            print(f"1. {signs[start_index].name}")
            print(f"2. {signs[start_index + 1].name}")

            sel = input("введите 1 или 2: ").strip()
            if sel == "1":
                selected_sign = signs[start_index]
            elif sel == "2":
                selected_sign = signs[start_index + 1]
            else:
                print("неверный выбор")
                continue


            try:
                with open("signs1.txt", "a", encoding="utf-8") as f:
                    f.write(f"{selected_sign.__class__.__bases__[0].__name__}: {selected_sign.info()}\n")
                print(f"знак '{selected_sign.name}' добавлен в файл")
            except Exception as e:
                print(f"ошибка при записи в файл: {e}")

        elif choice == "5":
            add_manual_sign()

        elif choice == "6":
            show_all_signs()

        else:
            print("неверный ввод, нужно выбрать от 0 до 6")

    except IndexError:
        print("недостаточно знаков в выбранной категории")
    except Exception as e:
        print(f"неожиданная ошибка в меню: {e}")
