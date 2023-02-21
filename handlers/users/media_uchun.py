from aiogram import types
from aiogram.types import ContentTypes, InputFile

from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text="Rasm qabul qilindi")


@dp.message_handler(text="Osh")
async def bot_echo(message: types.Message):
    rasm_manzili ="https://t.me/UstozShogird/17932"
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Osh\n "
                                                                    "Narxi : 20 000 so'm")