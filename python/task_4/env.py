TOKEN = '7532474605:AAG2MGWN7ZZ4bzw679Vhtk5nXJ85c2QvU28'

COMMANDS = {
    "/add_task": {
        "command": "add_task",
        "description": "Додати нове завдання"
    },
    "/print_all": {
        "command": "print_all",
        "description": "Вивести всі таски"
    },
    "/help": {
        "command": "help",
        "description": "Допомога з командами"
    },
    "/remove_by_id": {
        "command": "remove_by_id",
        "description": "Видалити таску за номером"
    },
    "/edit_task": {
        "command": "edit_task",
        "description": "Редагувати таску за номером"
    },
    "/watch_weather": {
        "command": 'watch_weather',
        "description": "Подивитися погоду в будь-якому місці"
    }
}

def CITY_COORDS_API(city, country):
    return f'https://api.api-ninjas.com/v1/geocoding?city={city}&country={country}'

CITY_WEATHER_API = 'https://api.open-meteo.com/v1/forecast'