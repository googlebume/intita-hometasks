class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено {amount}. Новий баланс: {self.__balance}")
        else:
            print("Сума повинна бути більшою за 0")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}. Новий баланс: {self.__balance}")
        else:
            print("Недостатньо коштів або некоректна сума")

    def get_balance(self):
        return self.__balance


account = BankAccount("Сергій", 1000)

account.deposit(500)
account.withdraw(300)
print("Баланс:", account.get_balance())

account.__balance = 999999
print("Баланс після прямої зміни:", account.get_balance())
