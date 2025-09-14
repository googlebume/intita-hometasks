from .interfaces import IUserService

class UserService(IUserService):
    def __init__(self, user, event_repository):
        self.user = user
        self.event_repository = event_repository

    def set_budget(self, amount):
        self.user.set_budget(amount)

    def get_budget(self):
        return self.user.get_budget()

    def change_event(self):
        return self.event_repository.get_all_events()

    def invite_friends(self, count):
        self.user.friends_count = count