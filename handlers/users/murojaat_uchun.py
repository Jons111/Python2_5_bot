from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_uchun import tasdiqlash_buttons,menu_buttons
from loader import dp,bot
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Forma

# Echo bot
@dp.message_handler(text="Adminga murojaat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismni kiriting",reply_markup=ReplyKeyboardRemove())
    await Forma.ism_qabul_qilish.set()

@dp.message_handler(state=Forma.ism_qabul_qilish,commands='start')
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="Bosh menu",reply_markup=menu_buttons)
    await state.finish()

@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ismi = message.text
    await state.update_data({'name':ismi})
    await message.answer(text="Familyani kiriting")
    await Forma.fam_qabul_qilish.set()

@dp.message_handler(state=Forma.fam_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    familya = message.text
    await state.update_data({'fam':familya})
    await message.answer(text="Yoshni kiriting")
    await Forma.yosh_qabul_qilish.set()


@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data({'age':yoshi})
    await message.answer(text="Telni kiriting")
    await Forma.tel_qabul_qilish.set()

@dp.message_handler(state=Forma.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    nomer = message.text
    await state.update_data({'tel':nomer})
    await message.answer(text="Manzilni kiriting")
    await Forma.manzil_qabul_qilish.set()

@dp.message_handler(state=Forma.manzil_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    manzil = message.text
    await state.update_data({'viloyat':manzil})
    await message.answer(text="Murojaatni kiriting")
    await Forma.murojaat_qabul_qilish.set()

@dp.message_handler(state=Forma.murojaat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    text = message.text
    await state.update_data({'matn':text})
    malumotlar = await state.get_data()
    user_ismi = malumotlar.get('name')
    user_fami = malumotlar.get('fam')
    user_yoshi = malumotlar.get('age')
    user_nomeri = malumotlar.get('tel')
    user_manzil = malumotlar.get('viloyat')
    user_murojaat = malumotlar.get('matn')

    malumot = f"Ism : {user_ismi}\n" \
              f"Familya : {user_fami}\n" \
              f"Yosh : {user_yoshi}\n" \
              f"Tel : {user_nomeri}\n" \
              f"Manzil : {user_manzil}\n\n" \
              f"Murojaat : {user_murojaat}\n"

    await message.answer(text=malumot,reply_markup=tasdiqlash_buttons)
    await Forma.tasdiqlash_holati.set()


@dp.message_handler(state=Forma.tasdiqlash_holati,text="Tasdiqlash")
async def bot_echo(message: types.Message,state:FSMContext):
    malumotlar = await state.get_data()
    user_ismi = malumotlar.get('name')
    user_fami = malumotlar.get('fam')
    user_yoshi = malumotlar.get('age')
    user_nomeri = malumotlar.get('tel')
    user_manzil = malumotlar.get('viloyat')
    user_murojaat = malumotlar.get('matn')

    malumot = f"Ushbu {message.from_user.first_name} foydalanuvchi murojaati :\n\n" \
              f"Ism : {user_ismi}\n" \
              f"Familya : {user_fami}\n" \
              f"Yosh : {user_yoshi}\n" \
              f"Tel : {user_nomeri}\n" \
              f"Manzil : {user_manzil}\n\n" \
              f"Murojaat : {user_murojaat}\n"

    await bot.send_message(chat_id='5883029982',text=malumot)
    await message.answer(text="Adminga yuborildi",reply_markup=menu_buttons)
    await state.finish()





@dp.message_handler(state=Forma.tasdiqlash_holati, text="Bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):

    await message.answer(text="Bekor qilindi",reply_markup=menu_buttons)
    await state.finish()












