from telegram import Update
from telegram.ext import ContextTypes
from .tasks_service import TaskService
from ...type_guards.str_guard import validate_task_text
from ...type_guards.int_guard import validate_task_number
from ...libs.massage_format.massage_formater import format_task_list

class BaseTasksHandler:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    async def add_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            text = " ".join(context.args) or "Без назви"
            validate_task_text(text)
            task = self.task_service.add(text)
            await update.message.reply_text(f"Завдання додано: {task['task']}")
        except Exception as e:
            await update.message.reply_text(str(e))

    async def print_all_tasks(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        tasks = self.task_service.list_all()
        message = format_task_list(tasks)
        await update.message.reply_text(message)

    async def remove_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            validate_task_number(int(context.args[0]))
            removed = self.task_service.remove(int(context.args[0]) - 1)
            await update.message.reply_text(f"Видалено таску: {removed['task']}")
        except Exception as e:
            await update.message.reply_text(str(e))

    async def edit_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            task_number = int(context.args[0])
            new_text = " ".join(context.args[1:])
            validate_task_number(task_number)
            validate_task_text(new_text)
            old, new = self.task_service.edit(task_number - 1, new_text)
            await update.message.reply_text(f"Було: {old}\nСтало: {new}")
        except Exception as e:
            await update.message.reply_text(str(e))
