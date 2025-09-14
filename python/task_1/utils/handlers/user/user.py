from .interfaces import IUser

class User(IUser):
    def __init__(self, name, friends_count):
        self.name = name
        self.friends_count = friends_count
        self.budget = 0

    def get_name(self):
        return self.name

    def get_friends_count(self):
        return self.friends_count

    def get_budget(self):
        return self.budget

    def set_budget(self, value):
        self.budget = value