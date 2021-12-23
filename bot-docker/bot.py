import logging
import requests
import json
from functions import get_keyboard
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    await message.answer('Кнопка покажет тебе текущую цену актива в долларах', reply_markup=get_keyboard())

@dp.message_handler(lambda message:message.text == 'Bitcoin')
async def getapi(message: types.Message):
    ans = requests.get('http://172.19.0.45/btc')
    res = json.loads(ans.text)
    price = res.get('bitcoin').get('usd')
    await message.answer(price)

@dp.message_handler(lambda message:message.text == 'Ethereum')
async def getapi(message: types.Message):
    ans = requests.get('http://172.19.0.45/eth')
    res = json.loads(ans.text)
    price = res.get('ethereum').get('usd')
    await message.answer(price)

@dp.message_handler(lambda message:message.text == 'Купить мне кофе')
async def getapi(message: types.Message):
    await message.answer('https://www.buymeacoffee.com/andystep')

@dp.message_handler(commands = ['help'])
async def start(message: types.Message):
    await message.answer('Этот бот поможет тебе узнать курс биткойна или эфира в долларах, для этого нажмите на соответствующую кнопку ниже', reply_markup=get_keyboard())

@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Робот не понял вопроса, попробуйте еще раз', reply_markup=get_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)