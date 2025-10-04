#pip install python-telegram-bot

TOKEN = 'ADD_YOUR_TOKEN'

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
}

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from utils.handlers.task_handler.tasks import BaseTasksHandler
from utils.handlers.crypto.crypto import Crypto
from utils.handlers.support.support import Support

crypto = Crypto()
task_handler = BaseTasksHandler(tasks=[], crypto=crypto)
support = Support(commands=COMMANDS)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler(COMMANDS["/add_task"]["command"], task_handler.add_task))
    app.add_handler(CommandHandler(COMMANDS["/print_all"]["command"], task_handler.print_all_tasks))
    app.add_handler(CommandHandler(COMMANDS["/remove_by_id"]["command"], task_handler.remove_task))
    app.add_handler(CommandHandler(COMMANDS["/edit_task"]["command"], task_handler.edit_task))
    app.add_handler(CommandHandler(COMMANDS["/help"]["command"], support.help_command))

    app.run_polling()

main()
