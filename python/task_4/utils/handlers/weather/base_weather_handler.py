import requests
from telegram import Update
from telegram.ext import ContextTypes
from env import CITY_WEATHER_API, CITY_COORDS_API


class BaseWeatherHandler:
    def __init__(self):
        self.city = "Berlin"
        self.country = "Germany"
        self.temperature_key = "temperature_2m"

    def get_city_coords(self, city: str, country: str):
        response = requests.get(CITY_COORDS_API(city, country))

        if response.status_code != 200:
            print(f"Error getting coords: {response.status_code}")
            return None

        data = response.json()
        if not data:
            print("No data for city")
            return None

        coords = {
            "latitude": data[0]["latitude"],
            "longitude": data[0]["longitude"]
        }
        return coords

    async def get_weather_in_city(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) < 1:
            await update.message.reply_text("Введіть назву міста, наприклад: /watch_weather Kyiv Ukraine")
            return

        self.city = context.args[0]
        self.country = context.args[1] if len(context.args) > 1 else ""

        coords = self.get_city_coords(self.city, self.country)
        if not coords:
            await update.message.reply_text("Не вдалося отримати координати міста.")
            return

        params = {
            "latitude": coords["latitude"],
            "longitude": coords["longitude"],
            "hourly": self.temperature_key
        }

        response = requests.get(CITY_WEATHER_API, params=params)

        if response.status_code == 200:
            data = response.json()
            temps = data.get("hourly", {}).get(self.temperature_key, [])
            current_temp = temps[-1] if temps else "невідомо"

            await update.message.reply_text(
                f"Поточна температура у {self.city}: {current_temp}°C"
            )
        else:
            await update.message.reply_text(
                f"Помилка при отриманні погоди: {response.status_code}"
            )
