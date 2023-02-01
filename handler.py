from random import randint
from create import dp
from aiogram import types
import spy


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    img = open('photo\\girl.jpeg', 'rb')
    await message.answer_photo(img)
    spy.spy(message)
    await message.answer(f'Привет, {message.from_user.first_name}, давай поиграем? )) Я умею играть: \n \n'

                         f'\t1) в конфетки \n'
                         f'\t2) в крестики-нолики \n \n'
                         f'Выбирай, чтобы посмотреть подробности /1 или /2?')


@dp.message_handler(commands=['1'])
async def mes_sweets(message: types.Message):
    await message.answer('Отличный выбор! Сейчас расскажу правила:\n \n '
                         '🍬 На столе лежит определенное случайным образом количество конфет.\n'
                         '🍬 Играют два игрока - я и ты. Делаем ход по очереди.\n'
                         '🍬 Первый ход определяется жеребьёвкой.\n'
                         '🍬 За один ход можно взять не более чем 28 конфет.\n'
                         '🍬 Все конфеты оппонента достаются сделавшему последний ход.\n \n '
                         '🍬 Может, поддашься? Я известная сладкоежка ;)\n \n'
                         '🍬 Готов(а)? Вводи /sweets')


@dp.message_handler(commands=['2'])
async def mes_ttt(message: types.Message):
    await message.answer('Отличный выбор! Думаю, что правила ты знаешь.\n \n '
                         'Первый ход определяется жеребьёвкой.\n \n'
                         'Поехали! Вводи /ttt )))).')


@dp.message_handler(commands=['ttt'])
async def mes_idontknow(message: types.Message):
    await message.answer(f'Упс, это {message.text} я еще не умею обрабатывать. Начни сначала? /start')


@dp.message_handler(commands=['sweets'])
async def mes_sweets(message: types.Message):
    global number_of_candies
    number_of_candies = randint(50, 150)
    await message.answer(f"Количество конфет задано случайным образом и равно {number_of_candies}.")
    turn = randint(1, 2)
    if turn == 1:
        await message.answer(f"Первый ход определен жеребьевкой: ходит {message.from_user.first_name}!\n"
                             f"Введи количество конфет от 1 до 28, которое ты хочешь взять")

    else:
        await message.answer(f"Первый ход определен жеребьевкой: ходит Бот!")
        await message.answer(f'Мы с ботом берем {bot_turn()} 🍬\n'
                             f'На столе осталось {number_of_candies}.'
                             f'Теперь твой ход, {message.from_user.first_name}!')
    await sweets_game(message)


@dp.message_handler()
async def sweets_game(message: types.Message):
    global number_of_candies
    if message.text.isdigit():
        if int(message.text) in range(1, 29) and number_of_candies - int(message.text) > -1:
            number_of_candies -= int(message.text)
            await message.answer(f'Ты взял {message.text} 🍬. На столе осталось {number_of_candies} 🍬.\n ')
            if number_of_candies == 0:
                await message.answer(
                    f'Поздравляю, {message.from_user.first_name}, победа за тобой! Смотри, теперь не лопни')
                await message.answer('Жми /start для возврата в главное меню!\n '
                                     'или /sweets чтобы еще раз попробовать отобрать мои конфетки!!! 😉')
                return
            await message.answer(f'Теперь очередь Бота!')
            await message.answer(f'Мы с ботом берем {bot_turn()} 🍬! На столе осталось {number_of_candies} ')
            if number_of_candies == 0:
                await message.answer(f'{message.from_user.first_name}, Бот выиграл! Все конфетки мои! Приходи на чай 😉')
                await message.answer('Жми /start для возврата в главное меню!\n '
                                     'или /sweets чтобы еще раз попробовать отобрать мои конфетки!!! 😉')
                return
            await message.answer(f'Теперь твой ход, {message.from_user.first_name}!')
        else:
            await message.answer(f'Играй по правилам ) Введи количество конфет, от 1 до 28 штук! \n'
                                 f'А еще - на столе не может остаться отрицательное количество конфет!')



def bot_turn():
     global number_of_candies
     if number_of_candies < 28:
         bot_took = number_of_candies
     else:
         bot_took = number_of_candies % 29
         if bot_took == 0:
             bot_took = 1
     number_of_candies -= bot_took
     return bot_took

number_of_candies = 0


