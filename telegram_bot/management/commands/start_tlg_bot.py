from django.core.management.base import BaseCommand

from telegram_bot.telegram_bot import start_bot


class Command(BaseCommand):
    help = "Запуск телеграм бота"

    def handle(self, *args, **kwargs):
        print("Start Telegram Bot")
        start_bot()
