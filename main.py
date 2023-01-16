import requests
import time

from src.load import load_params

params = load_params()

"""
Задавая параметры через yaml-file мы исключаем возможность задавать тип переменной.
Поэтому целесоорбразнее делать это через переменный (или классы как ниже)
"""
# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = '5940850106:AAEN0Wkv7DDo16NgJJL_z18rGtPYB7AF-Wc'
# TEXT: str = 'Ничёси! Классный апдейт!'
# MAX_COUNTER: int = 100

# offset: int = -2
# counter: int = 0



def main(params):
    API_URL = params['API_URL']
    BOT_TOKEN = params['BOT_TOKEN']

    print(API_URL)
    print(BOT_TOKEN)
    TEXT = params['TEXT']
    MAX_COUNTER = params['MAX_COUNTER']

    offset = params['offset']
    counter = params['counter']
    chat_id: int

    while counter < MAX_COUNTER:
        print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

        updates = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}").json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                requests.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}")

        time.sleep(1)
        counter += 1


if __name__=="__main__":
    main(params)
