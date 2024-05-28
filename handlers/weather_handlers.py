from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_state import UserStates
import aiohttp
import requests
from Config import Some_thing

router = Router()


@router.message(F.text == "Погода сейчас ☀️", UserStates.user_choose_button)
async def get_city_weather(message: Message, state: FSMContext):
    await message.answer(
        text="Введите название города:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choose_city)


@router.message(F.text, UserStates.user_choose_city)
async def get_city_weather(message: Message, state: FSMContext):
    city = message.text.strip().lower()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Some_thing.key_API}&units=metric&lang=ru'


    weather_data = requests.get(url=url).json()
    await message.reply(
        text=
             f"Погода сейчас:\n"
             f"Состояние: {weather_data['weather'][0]['main']}\n"
             f"Температура: {weather_data['main']['temp']} С;\n"
             f"Давление: {weather_data['main']['pressure']} гектопаскаль\n"
             f"Ветер: {weather_data['wind']['speed']} м/c\n"
             f"Влажность: {weather_data['main']['humidity']}%\n "
             f"Для возврата в меню нажмите /start")

    # await message.reply('Ты вернулся в главное меню',reply_markup=)

@router.message(F.text == "Погода на 3 дня 🌝", UserStates.user_choose_button)
async def get_city_weather(message: Message, state: FSMContext):
    await message.answer(
        text="Введите название города:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choose_another_city)


@router.message(F.text, UserStates.user_choose_another_city)
async def get_city_weather(message: Message, state: FSMContext):
    city = message.text
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={Some_thing.key_API}&units=metric&lang=ru'
    weather_data = requests.get(url=url).json()
    # print(weather_data["main"]["temp"])

    await message.reply(
        text=
             f"Погода на 3 дня:\n"
             f"\nДата: {weather_data['list'][0]['dt_txt']}\n"
             f"Состояние: {weather_data['list'][0]['weather'][0]['description']}\n"
             f"Температура: {weather_data['list'][0]['main']['temp']} С;\n"
             f"Давление: {weather_data['list'][0]['main']['pressure']} гектопаскаль\n"
             f"Ветер: {weather_data['list'][0]['wind']['speed']} м/c\n"
             f"Влажность: {weather_data['list'][0]['main']['humidity']} %"
             f"\n"   
             f"\nДата: {weather_data['list'][10]['dt_txt']}\n"
             f"Состояние: {weather_data['list'][10]['weather'][0]['description']}\n"
             f"Температура: {weather_data['list'][10]['main']['temp']} С;\n"
             f"Давление: {weather_data['list'][10]['main']['pressure']} гектопаскаль\n"
             f"Ветер: {weather_data['list'][10]['wind']['speed']} м/c\n"
             f"Влажность: {weather_data['list'][10]['main']['humidity']} %"
             f"\n"   
             f"\nДата: {weather_data['list'][18]['dt_txt']}\n"
             f"Состояние: {weather_data['list'][18]['weather'][0]['description']}\n"
             f"Температура: {weather_data['list'][18]['main']['temp']} С;\n"
             f"Давление: {weather_data['list'][18]['main']['pressure']} гектопаскаль\n"
             f"Ветер: {weather_data['list'][18]['wind']['speed']} м/c\n"
             f"Влажность: {weather_data['list'][18]['main']['humidity']}\n %"
             f"Для возврата в меню нажмите /start"
             f"\n"

    )