from telegram import Update
from telegram.ext import ContextTypes

class BaseTasksHandler:
    def __init__(self, crypto, tasks=None):
        self.tasks = tasks or []
        self.crypto = crypto

    def check_task_id(self, idx: int) -> str:

        if not isinstance(idx, int) or idx < 0 or idx >= len(self.tasks):
            return None
        return self.tasks[idx].get("id")

    async def add_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        try:
            task_text = " ".join(context.args) if context.args else "Без назви"

            if len(task_text) > 500:
                await update.message.reply_text(" Текст таски занадто довгий (максимум 500 символів)")
                return
            
            for task in self.tasks:
                if task.get("task", "").lower() == task_text.lower():
                    await update.message.reply_text(f"Така таска вже існує: {task['task']}")
                    return

            task = {
                "id": self.crypto.gen_id(task_text),
                "task": task_text
            }
            self.tasks.append(task)
            
            await update.message.reply_text(f"Завдання додано: {task_text}")
            return task
            
        except Exception as e:
            await update.message.reply_text(f"Помилка при додаванні таски: {str(e)}")
            print(f"Error in add_task: {e}")
    
    async def print_all_tasks(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            if not self.tasks:
                await update.message.reply_text("Список тасок порожній")
                return
            
            tasks_list = []
            for counter, task in enumerate(self.tasks, start=1):
                task_text = task.get("task", "Без назви")
                tasks_list.append(f"{counter}. {task_text}")
            
            message = "Всі таски:\n\n" + "\n".join(tasks_list)
            if len(message) > 4000:
                await update.message.reply_text("Всі таски:\n")
                for i in range(0, len(tasks_list), 20):
                    chunk = "\n".join(tasks_list[i:i+20])
                    await update.message.reply_text(chunk)
            else:
                await update.message.reply_text(message)
                
        except Exception as e:
            await update.message.reply_text(f"Помилка при виведенні тасок: {str(e)}")
            print(f"Error in print_all_tasks: {e}")

    async def remove_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            if not context.args:
                await update.message.reply_text(
                    "Вкажіть номер таски для видалення\n"
                    "Приклад: /remove_by_id 1"
                )
                return
            
            try:
                task_number = int(context.args[0])
            except ValueError:
                await update.message.reply_text("Номер таски має бути числом")
                return
            
            if task_number < 1:
                await update.message.reply_text("Номер таски має бути більше 0")
                return
            
            task_id = task_number - 1
            
            if task_id >= len(self.tasks):
                await update.message.reply_text(
                    f"Таски з номером {task_number} не існує\n"
                    f"Всього тасок: {len(self.tasks)}"
                )
                return
            
            task_text = self.tasks[task_id].get("task", "Без назви")
            del self.tasks[task_id]
            
            await update.message.reply_text(f"Таска '{task_text}' видалена")
            
        except Exception as e:
            await update.message.reply_text(f"Помилка при видаленні таски: {str(e)}")
            print(f"Error in remove_task: {e}")

    async def edit_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            if not context.args or len(context.args) < 2:
                await update.message.reply_text(
                    "Неправильний формат команди\n"
                    "Використання: /edit_task <номер> <новий текст>\n"
                    "Приклад: /edit_task 1 Новий текст таски"
                )
                return
            
            try:
                task_number = int(context.args[0])
            except ValueError:
                await update.message.reply_text("Номер таски має бути числом")
                return
            
            if task_number < 1:
                await update.message.reply_text("Номер таски має бути більше 0")
                return
            
            task_id = task_number - 1
            
            if task_id >= len(self.tasks):
                await update.message.reply_text(
                    f"Таски з номером {task_number} не існує\n"
                    f"Всього тасок: {len(self.tasks)}"
                )
                return
            
            new_task_text = " ".join(context.args[1:])
            
            if len(new_task_text) > 500:
                await update.message.reply_text("Текст таски занадто довгий (максимум 500 символів)")
                return
            
            if not new_task_text.strip():
                await update.message.reply_text("Текст таски не може бути порожнім")
                return
            
            for idx, task in enumerate(self.tasks):
                if idx != task_id and task.get("task", "").lower() == new_task_text.lower():
                    await update.message.reply_text(f"Таска з таким текстом вже існує: {task['task']}")
                    return
            
            old_text = self.tasks[task_id].get("task", "")
            self.tasks[task_id]['task'] = new_task_text
            self.tasks[task_id]['id'] = self.crypto.gen_id(new_task_text)
            
            await update.message.reply_text(
                f"Таску оновлено:\n"
                f"Було: {old_text}\n"
                f"Стало: {new_task_text}"
            )
            
        except Exception as e:
            await update.message.reply_text(f"Помилка при редагуванні таски: {str(e)}")
            print(f"Error in edit_task: {e}")