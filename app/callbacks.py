import asyncio
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from config import bot, dp
from keyboards.inlineKeyboard.InlineKeyboard import (
    AcceptCallInlineKeyboard,
    IThinkItsNotForMe,
    MeditateOrMaraphone,
    SoHard,
    WantToBuy,
    WhatInMaraphone,
    WhatPrice,
)
from media.text.text import (
    AboutHomework,
    AboutTime,
    AfterDeadline,
    HomeWorkDeadLine,
    MaybeCall,
    MeditationAchive,
    NewLife,
    NotBought,
    NotesAboutDeadline,
    StoryDidNotSend,
    TellYourStory,
    WaitingYourStory,
)
from states import Story


@dp.callback_query_handler(text="LetsGo")
async def LetsGoButtonPressed(
    callback: types.CallbackQuery, state: FSMContext
):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "LetsGoPressed" not in ButtonAlreadyPressed:
        await state.update_data({"LetsGoPressed": "Yes"})
        TelephoneCall = InputFile("media/image/TelephoneCall.png")
        await bot.send_photo(
            chat_id=callback.from_user.id, photo=TelephoneCall
        )
        await asyncio.sleep(2)
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=MaybeCall,
            reply_markup=AcceptCallInlineKeyboard,
        )


@dp.callback_query_handler(text="AcceptCall")
async def AcceptButtonPressed(
    callback: types.CallbackQuery, state: FSMContext
):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "AcceptCallPressed" not in ButtonAlreadyPressed:
        await state.update_data({"AcceptCallPressed": "Yes"})
        AboutMyPast = InputFile("media/audio/AboutMyPast.ogg")
        await bot.send_voice(chat_id=callback.from_user.id, voice=AboutMyPast)
        await asyncio.sleep(36)
        await bot.send_message(
            chat_id=callback.from_user.id, text=TellYourStory
        )
        await Story.UserStory.set()
        await asyncio.sleep(60 * 60)
        if await state.get_state() == "Story:UserStory":
            await bot.send_message(
                chat_id=callback.from_user.id, text=WaitingYourStory
            )
        await asyncio.sleep(60 * 60)
        if await state.get_state() == "Story:UserStory":
            await bot.send_message(
                chat_id=callback.from_user.id, text=StoryDidNotSend
            )
            await state.reset_state()
            Bpoint = InputFile("media/audio/Bpoint.ogg")
            await bot.send_voice(chat_id=callback.from_user.id, voice=Bpoint)
            await asyncio.sleep(35)
            StoryImage = InputFile("media/image/Story.png")
            await bot.send_photo(
                chat_id=callback.from_user.id, photo=StoryImage
            )
            StoryVideo = InputFile("media/video/StoryVideo.mp4")
            await bot.send_video_note(
                chat_id=callback.from_user.id, video_note=StoryVideo
            )


@dp.callback_query_handler(text="WantLikeThis")
async def SendWork(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "WantLikeThisPressed" not in ButtonAlreadyPressed:
        await state.update_data({"WantLikeThisPressed": "Yes"})
        photo = InputFile("media/image/HomeWork.png")
        await bot.send_photo(
            chat_id=callback.from_user.id, photo=photo, caption=AboutHomework
        )
        await asyncio.sleep(2)
        voice = InputFile("media/audio/AboutWish.ogg")
        await bot.send_voice(chat_id=callback.from_user.id, voice=voice)
        await bot.send_document(
            chat_id=callback.from_user.id,
            document=InputFile("media/files/Research.html"),
        )
        await asyncio.sleep(35)
        await bot.send_audio(
            chat_id=callback.from_user.id,
            caption=HomeWorkDeadLine,
            audio=InputFile("media/audio/Meditate.mp3"),
            reply_markup=MeditateOrMaraphone,
        )
        now = datetime.now()
        deadline = datetime(
            year=now.year, month=now.month, day=now.day + 1, hour=0, minute=0
        )
        timer = (deadline - now).total_seconds()
        await state.update_data({"WaitingWishes": "Yes"})
        await asyncio.sleep(timer)
        WaitingWish = await state.get_data()
        if WaitingWish["WaitingWishes"] == "Yes":
            bot.send_message(chat_id=callback.from_user.id, text=AfterDeadline)
            await state.update_data({"WaitingWishes": "After"})


@dp.callback_query_handler(text="Meditation")
async def ListenMeditation(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "Meditation" not in ButtonAlreadyPressed:
        await state.update_data({"Meditation": "Yes"})
        await bot.answer_callback_query(callback_query_id=callback.id)
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=InputFile("media/image/Meditation.png"),
        )
        await bot.send_voice(
            chat_id=callback.from_user.id,
            voice=InputFile("media/audio/meditation.ogg"),
        )
        await asyncio.sleep(36)
        await bot.send_message(
            chat_id=callback.from_user.id, text=MeditationAchive
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=NotesAboutDeadline,
            reply_markup=WhatInMaraphone,
        )


@dp.callback_query_handler(text="WhatInMaraphone")
async def AboutMaraphone(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "Meditation" not in ButtonAlreadyPressed:
        await state.update_data({"Meditation": "No"})
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=InputFile("media/image/Broshure.png"),
        )
        await bot.send_voice(
            chat_id=callback.from_user.id,
            voice=InputFile("media/audio/MaraphoneCart.ogg"),
            reply_markup=SoHard,
        )


@dp.callback_query_handler(text="SoHard")
async def AfterSoHard(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "SoHard" not in ButtonAlreadyPressed:
        await state.update_data({"SoHard": "Yes"})
        await bot.send_message(chat_id=callback.from_user.id, text=AboutTime)
        await asyncio.sleep(10)
        MediaGroup = types.MediaGroup()
        MediaGroup.attach_photo(photo=InputFile("media/image/Правила 11.png"))
        MediaGroup.attach_photo(photo=InputFile("media/image/Правила 12.png"))
        MediaGroup.attach_photo(photo=InputFile("media/image/Правила 13.png"))
        MediaGroup.attach_photo(photo=InputFile("media/image/Правила 14.png"))
        MediaGroup.attach_photo(photo=InputFile("media/image/Правила 15.png"))
        await bot.send_media_group(
            chat_id=callback.from_user.id, media=MediaGroup
        )
        await bot.send_voice(
            chat_id=callback.from_user.id,
            voice=InputFile("media/audio/GrandWishes.ogg"),
            reply_markup=WhatPrice,
        )
        await state.update_data({"Bought": "No"})
        await asyncio.sleep(10)
        status = await state.get_data()
        if status["Bought"] == "No":
            await bot.send_voice(
                chat_id=callback.from_user.id,
                voice=InputFile("media/audio/AboutNextStream.ogg"),
                reply_markup=IThinkItsNotForMe,
            )


@dp.callback_query_handler(text="Price")
async def Price(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "Price" not in ButtonAlreadyPressed:
        await state.update_data({"Price": "Yes"})
        MediaGroup = types.MediaGroup()
        MediaGroup.attach_photo(photo=InputFile("media/image/Тариф1.png"))
        MediaGroup.attach_photo(photo=InputFile("media/image/Тариф2.png"))
        await bot.send_media_group(
            chat_id=callback.from_user.id, media=MediaGroup
        )
        await bot.send_voice(
            chat_id=callback.from_user.id,
            voice=InputFile("media/audio/VoiceWithSurprise.ogg"),
            reply_markup=WantToBuy,
        )


@dp.callback_query_handler(text="NotForMe")
async def NotForMe(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    ButtonAlreadyPressed = await state.get_data()
    if "NotForMe" not in ButtonAlreadyPressed:
        await state.update_data({"NotForMe": "Yes"})
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="МЖ работает 8 из 10",
            reply_markup=WantToBuy,
        )
        await asyncio.sleep(10)
        status = await state.get_data()
        if status["Bought"] == "No":
            await bot.send_voice(
                chat_id=callback.from_user.id,
                voice=InputFile("media/audio/YouDoubt.ogg"),
            )
            if status["Meditation"] == "Yes":
                await bot.send_photo(
                    chat_id=callback.from_user.id,
                    photo=InputFile("media/image/Чек-лист.png"),
                )
                await asyncio.sleep(30)
                await bot.send_message(
                    chat_id=callback.from_user.id,
                    text=NewLife,
                    reply_markup=WantToBuy,
                )
            if status["Meditation"] == "No":
                await bot.send_photo(
                    chat_id=callback.from_user.id,
                    photo=InputFile("media/image/Meditation.png"),
                )
                await bot.send_voice(
                    chat_id=callback.from_user.id,
                    voice=InputFile("media/audio/meditation.ogg"),
                )
                await asyncio.sleep(36)
                await bot.send_message(
                    chat_id=callback.from_user.id,
                    text=NewLife,
                    reply_markup=WantToBuy,
                )
            await asyncio.sleep(10)
            status = await state.get_data()
            if status["Bought"] == "No":
                await bot.send_message(
                    chat_id=callback.from_user.id, text=NotBought
                )
