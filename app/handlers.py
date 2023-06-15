import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, InputFile
from config import bot, dp
from keyboards.inlineKeyboard.InlineKeyboard import (
    IWantLikeThisInlineKeyboard,
    LetsGoInlineKeyboard,
)
from media.text.text import (
    AboutMyRoad,
    HelloMessageWithName,
    LetsGo,
    StartMessage,
    ThankYouForStory,
    WishesAfterTime,
    WishesInTime,
)
from states import Story, User


@dp.message_handler(commands=["start"])
async def start(message: types.Message, state: FSMContext):
    await message.delete()
    await bot.send_message(chat_id=message.chat.id, text=StartMessage)
    await User.name.set()
    await asyncio.sleep(60 * 30)
    if await state.get_state() == "User:name":
        await bot.send_message(
            chat_id=message.chat.id,
            text=LetsGo,
            reply_markup=LetsGoInlineKeyboard,
        )
        await state.reset_state()


@dp.message_handler(state=User.name)
async def newUser(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.reset_state()
    await bot.send_message(
        chat_id=message.chat.id,
        text=HelloMessageWithName.format(name=message.text),
    )
    await asyncio.sleep(5)
    await bot.send_message(
        chat_id=message.chat.id, text=LetsGo, reply_markup=LetsGoInlineKeyboard
    )


@dp.message_handler(state=Story.UserStory)
async def StoryIsTold(message: types.Message, state: FSMContext):
    await state.reset_state()
    await bot.send_message(chat_id=message.chat.id, text=ThankYouForStory)
    await asyncio.sleep(2)
    await bot.send_message(chat_id=message.chat.id, text=AboutMyRoad)
    Bpoint = InputFile("media/audio/Bpoint.ogg")
    await asyncio.sleep(5)
    await bot.send_voice(chat_id=message.chat.id, voice=Bpoint)
    await asyncio.sleep(35)
    StoryImage = InputFile("media/image/Story.png")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=StoryImage,
        reply_markup=IWantLikeThisInlineKeyboard,
    )
    StoryVideo = InputFile("media/video/StoryVideo.mp4")
    await bot.send_video_note(chat_id=message.chat.id, video_note=StoryVideo)


@dp.message_handler(content_types=ContentType.PHOTO)
async def WishesWasScipped(message: types.Message, state: FSMContext):
    WaitingWish = await state.get_data()
    print(WaitingWish["WaitingWishes"])
    if WaitingWish["WaitingWishes"] == "Yes":
        await state.update_data({"WaitingWishes": "No"})
        await bot.send_message(chat_id=message.chat.id, text=WishesInTime)
    if WaitingWish["WaitingWishes"] == "After":
        await state.update_data({"WaitingWishes": "No"})
        await bot.send_message(chat_id=message.chat.id, text=WishesAfterTime)


# Автоматическое удаление любого сообщения(опционально)
@dp.message_handler()
async def spamReduce(message: types.Message):
    await message.delete()
