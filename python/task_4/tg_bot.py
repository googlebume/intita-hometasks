from telegram.ext import Application, CommandHandler, MessageHandler, filters
from utils.handlers.task_handler.tasks_handler import BaseTasksHandler
from utils.handlers.crypto.crypto import Crypto
from utils.handlers.support.support import Support
from utils.handlers.file.base_file_handler import BaseFileHandler

from env import TOKEN, COMMANDS

from utils.handlers.file.base_file_handler import BaseFileHandler

crypto = Crypto()
baseDatabaseHandler = BaseFileHandler()
task_handler = BaseTasksHandler(tasks=[], crypto=crypto, fileHandler = baseDatabaseHandler)
support = Support(commands=COMMANDS)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler(COMMANDS["/add_task"]["command"], task_handler.add_task))
    app.add_handler(CommandHandler(COMMANDS["/print_all"]["command"], task_handler.print_all_tasks))
    app.add_handler(CommandHandler(COMMANDS["/remove_by_id"]["command"], task_handler.remove_task))
    app.add_handler(CommandHandler(COMMANDS["/edit_task"]["command"], task_handler.edit_task))
    app.add_handler(CommandHandler(COMMANDS["/help"]["command"], support.help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
