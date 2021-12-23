from aiogram import Bot, Dispatcher, executor, types
def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btcbutton = types.KeyboardButton("Bitcoin")
    ethbutton = types.KeyboardButton("Ethereum")
    coffe = types.KeyboardButton("Купить мне кофе")
    keyboard.add(btcbutton)
    keyboard.add(ethbutton)
    keyboard.add(coffe)
    return keyboard