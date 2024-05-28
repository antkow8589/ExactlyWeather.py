from aiogram import Bot, Dispatcher
import asyncio
from handlers import other_handlers, weather_handlers
from Config import Some_thing


async def main():
    bot = Bot(token=Some_thing.key_Token) #здесь необходимо ввести свой токен
    dp = Dispatcher()
    dp.include_routers(other_handlers.router,weather_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
