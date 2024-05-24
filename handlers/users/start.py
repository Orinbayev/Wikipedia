from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
import wikipedia



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!\nWikipedia botga xush kelipsiz!\n\nTilni o'zgartirish uchun /til buyrugini bering.")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday ma'lumot topilmadi.")
