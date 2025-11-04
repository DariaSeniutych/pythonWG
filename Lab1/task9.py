ip = input("введи ip-адрес: ")
parts = ip.split(".")
if len(parts) != 4:
    print("неверный формат")
else:
    p1, p2, p3, p4 = parts
    if (p1.isdigit() and 0 <= int(p1) <= 255 and
        p2.isdigit() and 0 <= int(p2) <= 255 and
        p3.isdigit() and 0 <= int(p3) <= 255 and
        p4.isdigit() and 0 <= int(p4) <= 255):
        print("корректный ip-адрес")
    else:
        print("некорректный ip-адрес")