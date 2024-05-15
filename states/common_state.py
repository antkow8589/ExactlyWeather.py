from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    user_choose_button = State()
    user_choose_city = State()
