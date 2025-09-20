from utils.handlers.events.repository import EventsRepository
from utils.handlers.events.interfaces import IEventsRepository
from utils.handlers.user.user import User
from utils.handlers.user.interfaces import IUser, IUserService
from utils.handlers.user.service import UserService

from utils.type_guards.float_guard import safe_input_float
from utils.type_guards.int_guard import safe_input_int
from utils.type_guards.str_guard import safe_input_str
ф =12
print(ф)
def main():
    name = safe_input_str("Введіть ваше ім'я: ")
    friends_count = safe_input_int("Скільки друзів ви плануєте запросити? ", min_value=0)
    
    user: IUser = User(name, friends_count)
    repo: IEventsRepository = EventsRepository()
    user_service: IUserService = UserService(user, repo)
    
    budget = safe_input_float("Введіть ваш бюджет (грн): ", min_value=0)
    user_service.set_budget(budget)

    while True:
        events = user_service.change_event()
        print("\nДоступні заходи:")
        for i, (event, price) in enumerate(events.items(), 1):
            print(f"{i}. {event} (ціна за 1 учасника: {price} грн)")

        event_choice = safe_input_int("Оберіть захід (номер): ", min_value=1)
        if event_choice > len(events):
            print("Некоректний вибір заходу. Спробуйте ще раз.")
            continue
        
        event_name = list(events.keys())[event_choice - 1]
        event_price = events[event_name]

        participants = safe_input_int(
            f"Введіть кількість учасників (включаючи себе): ", min_value=1
        )

        total_cost = event_price * participants
        budget = user_service.get_budget()

        if total_cost > budget:
            print(f"Недостатньо коштів! Потрібно {total_cost} грн, а у вас лише {budget} грн.")
            print("Оберіть дешевший захід або зменшіть кількість учасників.")
            continue
        else:
            budget -= total_cost
            user_service.set_budget(budget)
            print(f"Захід '{event_name}' для {participants} учасників заброньовано!")
            print(f"Залишок бюджету: {budget} грн.")

        again = safe_input_str("Бажаєте спланувати ще захід? (так/ні): ").lower()
        if again != "так":
            print("Планування завершено. Гарного відпочинку!")
            break

if __name__ == "__main__":
    main()