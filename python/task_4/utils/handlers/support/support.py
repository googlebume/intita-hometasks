from telegram import Update
from telegram.ext import ContextTypes

class Support():

    def __init__(self, commands):
        self.commands = commands

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = "Доступні команди:\n\n"
    
        for cmd_key, cmd_data in self.commands.items():
            description = cmd_data.get("description")
            help_text += f"{cmd_key} — {description}\n"

        await update.message.reply_text(help_text)