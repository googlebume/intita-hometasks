class IUser:
    def get_name(self):
        """Повертає ім'я користувача"""

    def get_friends_count(self):
        """Повертає кількість друзів"""

    def get_budget(self):
        """Повертає бюджет користувача"""

    def set_budget(self, value):
        """Встановлює бюджет користувача"""


class IUserService:
    def set_budget(self, amount):
        """Встановлює бюджет користувача"""

    def get_budget(self):
        """Повертає бюджет користувача"""

    def change_event(self):
        """Повертає список заходів"""

    def invite_friends(self, count):
        """Встановлює кількість друзів"""
