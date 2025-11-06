import json


# исключения
class CurrencyMismatchError(Exception):
    """Ошибка валюты при проведении операции."""
    pass


class InsufficientFundsError(Exception):
    """Ошибка: недостаточно средств при снятии."""
    pass


class AccountAlreadyExistsError(Exception):
    """Ошибка: счёт в данной валюте уже существует."""
    pass


class ClientNotFoundError(Exception):
    """Ошибка: клиент не найден"""
    pass


class AccountNotFoundError(Exception):
    """Ошибка: счёт не найден"""
    pass


class Account:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств.")
        self.balance -= amount

    def to_dict(self):
        return {"currency": self.currency, "balance": self.balance}

    @staticmethod
    def from_dict(data):
        account = Account(data["currency"])
        account.balance = data["balance"]
        return account


class Client:
    def __init__(self, client_id, name, surname):
        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.accounts = {}  # {валюта: объект счёта}

    def create_account(self, currency):
        if currency in self.accounts:
            raise AccountAlreadyExistsError(f"Счёт в валюте {currency} уже существует.")
        new_account = Account(currency)
        self.accounts[currency] = new_account
        print(f"Открыт счёт в валюте {currency} для клиента {self.name} {self.surname}")

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFoundError(f"Счёт в валюте {currency} не найден.")
        del self.accounts[currency]
        print(f"Закрыт счёт в валюте {currency} для клиента {self.name} {self.surname}")

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFoundError(f"Счёт в валюте {currency} не найден.")
        return self.accounts[currency]

    def get_all_accounts(self):
        return list(self.accounts.values())

    def generate_statement(self):
        statement = f"Выписка клиента {self.name} {self.surname} (ID: {self.client_id})\n"
        statement += "=" * 50 + "\n"
        total = 0
        for currency, account in self.accounts.items():
            statement += f"{currency}: {account.balance:.2f}\n"
            total += account.balance
        statement += "-" * 50 + "\n"
        statement += f"Общий баланс: {total:.2f}\n"
        return statement

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "surname": self.surname,
            "accounts": {currency: account.to_dict() for currency, account in self.accounts.items()}
        }

    @staticmethod
    def from_dict(data):
        client = Client(data["client_id"], data["name"], data["surname"])
        for currency, acc_data in data["accounts"].items():
            account = Account.from_dict(acc_data)
            client.accounts[currency] = account
        return client


class Bank:
    def __init__(self, clients=None):
        self.clients = clients if clients is not None else {}
        self.next_client_id = 1

    def add_client(self, name, surname):
        client_id = self.next_client_id
        self.next_client_id += 1
        new_client = Client(client_id, name, surname)
        self.clients[client_id] = new_client
        print(f"Клиент {name} {surname} добавлен. ID: {client_id}")
        return new_client

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ClientNotFoundError(f"Клиент с ID {client_id} не найден.")
        return self.clients[client_id]

    def open_account(self, client_id, currency):
        client = self.get_client(client_id)
        try:
            client.create_account(currency)
        except AccountAlreadyExistsError as e:
            print(e)

    def close_account(self, client_id, currency):
        client = self.get_client(client_id)
        try:
            client.close_account(currency)
        except AccountNotFoundError as e:
            print(e)

    def deposit(self, client_id, currency, amount):
        client = self.get_client(client_id)
        try:
            account = client.get_account(currency)
            account.deposit(amount)
            print(f"Пополнено {amount:.2f} {currency} на счёт клиента {client.name}.")
        except (AccountNotFoundError, ValueError) as e:
            print(e)

    def withdraw(self, client_id, currency, amount):
        client = self.get_client(client_id)
        try:
            account = client.get_account(currency)
            account.withdraw(amount)
            print(f"Снято {amount:.2f} {currency} со счёта клиента {client.name}.")
        except (AccountNotFoundError, InsufficientFundsError, ValueError) as e:
            print(e)

    def transfer(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        if from_currency != to_currency:
            raise CurrencyMismatchError("Перевод возможен только в одной валюте.")

        from_client = self.get_client(from_client_id)
        to_client = self.get_client(to_client_id)

        try:
            from_account = from_client.get_account(from_currency)
            to_account = to_client.get_account(to_currency)

            from_account.withdraw(amount)
            to_account.deposit(amount)

            print(f"Переведено {amount:.2f} {from_currency} от {from_client.name} к {to_client.name}.")
        except (AccountNotFoundError, InsufficientFundsError, ValueError) as e:
            print(e)

    def show_all_accounts(self, client_id):
        client = self.get_client(client_id)
        print("\n--- Все счета клиента ---")
        for currency, account in client.accounts.items():
            print(f"{currency}: {account.balance:.2f}")
        total = sum(acc.balance for acc in client.accounts.values())
        print(f"Общий баланс: {total:.2f}")

    def save_state(self, filename="bank_state.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
        print(f"Состояние банка сохранено в {filename}")

    def load_state(self, filename="bank_state.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            clients = {}
            for client_id_str, client_data in data["clients"].items():
                client_id = int(client_id_str)
                clients[client_id] = Client.from_dict(client_data)

            bank = Bank(clients)
            bank.next_client_id = data["next_client_id"]
            print(f"Состояние банка загружено из {filename}")
            return bank
        except FileNotFoundError:
            print("Файл не найден. Создан новый банк.")
            return Bank()
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            return Bank()

    def to_dict(self):
        return {
            "clients": {
                client_id: client.to_dict()
                for client_id, client in self.clients.items()
            },
            "next_client_id": self.next_client_id
        }


def main():
    try:
        bank = Bank().load_state()
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        bank = Bank()
        print("Создан новый банк.")

    while True:
        print("\n Банковское приложение ")
        print("1. Добавить клиента")
        print("2. Открыть счёт")
        print("3. Закрыть счёт")
        print("4. Пополнить счёт")
        print("5. Снять деньги")
        print("6. Перевести деньги")
        print("7. Показать все счета клиента")
        print("8. Сохранить состояние")
        print("9. Выход")

        choice = input("Выберите действие (1-9): ").strip()

        if choice == "1":
            name = input("Имя: ").strip()
            surname = input("Фамилия: ").strip()
            bank.add_client(name, surname)

        elif choice == "2":
            try:
                client_id = int(input("ID клиента: "))
                currency = input("Валюта (USD, EUR, BYN): ").strip().upper()
                bank.open_account(client_id, currency)
            except ValueError:
                print("ID должен быть числом.")
            except ClientNotFoundError as e:
                print(e)

        elif choice == "3":
            try:
                client_id = int(input("ID клиента: "))
                currency = input("Валюта: ").strip().upper()
                bank.close_account(client_id, currency)
            except ValueError:
                print("ID должен быть числом.")
            except ClientNotFoundError as e:
                print(e)

        elif choice == "4":
            try:
                client_id = int(input("ID клиента: "))
                currency = input("Валюта: ").strip().upper()
                amount = float(input("Сумма: "))
                bank.deposit(client_id, currency, amount)
            except ValueError:
                print("ID и сумма должны быть числами.")
            except ClientNotFoundError as e:
                print(e)

        elif choice == "5":
            try:
                client_id = int(input("ID клиента: "))
                currency = input("Валюта: ").strip().upper()
                amount = float(input("Сумма: "))
                bank.withdraw(client_id, currency, amount)
            except ValueError:
                print("ID и сумма должны быть числами.")
            except ClientNotFoundError as e:
                print(e)

        elif choice == "6":
            try:
                from_client_id = int(input("ID отправителя: "))
                from_currency = input("Валюта отправителя: ").strip().upper()
                to_client_id = int(input("ID получателя: "))
                to_currency = input("Валюта получателя: ").strip().upper()
                amount = float(input("Сумма: "))
                bank.transfer(from_client_id, from_currency, to_client_id, to_currency, amount)
            except ValueError:
                print("ID и сумма должны быть числами.")
            except (ClientNotFoundError, CurrencyMismatchError) as e:
                print(e)

        elif choice == "7":
            try:
                client_id = int(input("ID клиента: "))
                bank.show_all_accounts(client_id)
            except ValueError:
                print("ID должен быть числом.")
            except ClientNotFoundError as e:
                print(e)

        elif choice == "8":
            bank.save_state()
            print("Состояние сохранено.")

        elif choice == "9":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()