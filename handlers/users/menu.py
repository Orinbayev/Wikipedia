from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeybord import menu
import wikipedia

from loader import dp

@dp.message_handler(Command('til'))
async def   show_menu(message: Message):
    
    await message.answer("Tilni tanlang", reply_markup=menu)

@dp.message_handler(text='Uzbek')
async def   show_menu(message: Message):
    wikipedia.set_lang('uz')
    await message.answer("Siz Uzbek tilini tanladingiz!\nSizga qanay jurnal yoki ma'qola kerak💁‍♂️?", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Rus')
async def   show_menu(message: Message):
    wikipedia.set_lang('ru')
    await message.answer("Вы выбрали русский язык!\nКакой журнал или статья вам нужен💁‍♂️?", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='English')
async def   show_menu(message: Message):
    wikipedia.set_lang('en')
    await message.answer("You have chosen English!\nWhat magazine or article do you need💁‍♂️?", reply_markup=ReplyKeyboardRemove())

