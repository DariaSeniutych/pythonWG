import datetime

def log_calls(imya_fayla):
    def dekorator(funktsiya):
        def obertka(*args):
            vremya = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            imya_funktsii = funktsiya.name

            argumenty = str(args)

            soobshenie = vremya + " — вызов " + imya_funktsii + " с аргументами: " + argumenty + "\n"

            f = open(imya_fayla, "a", encoding="utf-8")
            f.write(soobshenie)
            f.close()

            resultat = funktsiya(*args)
            return resultat

        return obertka

     return dekorator

@log_calls("moy_log.txt")
def summa(a, b):
    return a + b
print(summa(5, 3))
print(summa(100, 200))