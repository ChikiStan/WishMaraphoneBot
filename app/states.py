from aiogram.dispatcher.filters.state import State, StatesGroup


class User(StatesGroup):
    name = State()


class Story(StatesGroup):
    UserStory = State()
