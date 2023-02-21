from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Taomlar"),
            KeyboardButton(text="Ichimliklar")
        ],
        [
            KeyboardButton(text="Shirinliklar"),
            KeyboardButton(text="Milliy taomlar")
        ],
        [
            KeyboardButton(text="Adminga murojaat")
        ],
        [
            KeyboardButton(text="Kontakt",request_contact=True),
            KeyboardButton(text="Lokatsiya",request_location=True)
        ]
    ],
    resize_keyboard=True
)

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)