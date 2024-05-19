from aiogram import Bot, Dispatcher
import asyncio
from handlers import other_handlers, weather_handlers


async def main():
    bot = Bot(token="6999539382:AAHgD0caDapEknHPDFhzQUb_C8-YAkTAeX8")
    dp = Dispatcher()
    dp.include_routers(other_handlers.router,weather_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
