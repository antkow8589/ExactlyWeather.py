from aiogram import Bot, Dispatcher
import asyncio
from handlers import other_handlers


async def main():
    bot = Bot(token="7009499024:AAGs7qzLdnfs4bMEQng489KRxVw0qn3bCfQ")
    dp = Dispatcher()
    dp.include_routers(other_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
