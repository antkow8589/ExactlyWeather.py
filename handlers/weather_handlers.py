from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_state import UserStates
import aiohttp
import requests

router = Router()


@router.message(F.text == "Погода", UserStates.user_choose_button)
async def get_city_weather(message: Message, state: FSMContext):
    await message.answer(
        text="Введите название города:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choose_city)


@router.message(F.text, UserStates.user_choose_city)
async def get_city_weather(message: Message, state: FSMContext):
    city = message.text
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=024e2078c2ad10abfde94667edee771d&units=metric"
    weather_data = requests.get(url=url).json()
    print(weather_data)
    print(weather_data["main"]["temp"])

    await message.reply(
        text=f"Описание: {weather_data['weather'][0]['main']};\n"
             f"Температура: {weather_data['main']['temp']};\n"
    )

    # async with aiohttp.ClientSession as session:
    #     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=024e2078c2ad10abfde94667edee771d&units=metric"
    #     async with session.get(url=url) as response:
    #         weather_data = await aiohttp.text()
    #         print(weather_data)
