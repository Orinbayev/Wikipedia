from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
 
    keyboard=[
        [
            KeyboardButton(text="Uzbek", ), KeyboardButton(text="Rus"),
            KeyboardButton(text="English")
            
        ],
    
    ],
    resize_keyboard=True
)


