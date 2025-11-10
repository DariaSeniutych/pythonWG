#
# сначала сгенерировать, а потом создать некоторую структуру, (словарь)
# в которой будут храниться id клиента и номер его банковской карты
# номер карты содержит 16 цифр
# когда эта структура сгенерирована, пользователь вводит свой id и номер карты,
# если они уже существуют, значит сообщаем об этом,
# в противном случае - добавляем номер id в свою структуру
#

import random

clients = {}
num_initial_clients = 3

for i in range(1, num_initial_clients + 1):
    client_id = i
    card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    clients[client_id] = card_number

print("исходная база клиентов:")
for cid, card in clients.items():
    print(f"id: {cid},  номер карты: {card}")

user_id = int(input("введи ваш id: "))
user_card = input("введи номер своей карты: ").strip()

if len(user_card) != 16 or not user_card.isdigit():
    print("номер карты должен содержать именно 16 цифр")
else:
    if user_id in clients:
        if clients[user_id] == user_card:
            print("данный клиент с именно таким номером карты уже существует")
        else:
            print(f"id {user_id} уже существует, но с другой картой, добавить повторно нельзя")
    else:
        clients[user_id] = user_card
        print("новый клиент добавлен в систему")
        print(f"теперь в базе: id {user_id} с номером карты {user_card}")

