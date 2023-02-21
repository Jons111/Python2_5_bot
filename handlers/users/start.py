from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.taomlar_uchun import taomlar_buttons
from keyboards.inline.tillar_uchun import tillar_buttons
from loader import dp, bot
from aiogram.types import CallbackQuery

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.message_handler(text='Taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum botga hush kelibsiz, {message.from_user.first_name}!",reply_markup=taomlar_buttons)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"O'zbek tili tanlandi",reply_markup=menu_buttons)



















