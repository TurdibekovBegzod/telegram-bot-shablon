from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.types import BotCommand
import admin
import user
import logging
import sys
import zoneinfo
import os
from dotenv import load_dotenv

load_dotenv()  # 🔥 .env ni yuklaydi

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPERADMIN = int(os.getenv("SUPERADMIN"))  # 🔥 string → int

log_format = "%(asctime)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    datefmt=date_format,
    stream=sys.stdout
)

logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
tz = zoneinfo.ZoneInfo("Asia/Tashkent")


async def startup(bot: Bot):
    await bot.send_message(text="Bot ishga tushdi! ✅", chat_id=SUPERADMIN)

async def shutdown(bot: Bot):
    await bot.send_message(text="Bot ishdan to'xtadi! ❌", chat_id=SUPERADMIN)

async def start():
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    dp.include_router(admin.router)
    dp.include_router(user.router)

    await bot.set_my_commands([
        BotCommand(command="start", description="Refresh the Bot!"),
        BotCommand(command="help", description="HELP!")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    run(start())
