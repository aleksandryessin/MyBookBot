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



def main1(params):

    API_URL = params['API_URL']
    BOT_TOKEN = params['BOT_TOKEN']
    TEXT = params['TEXT']
    MAX_COUNTER = params['MAX_COUNTER']

    offset: int = -2
    counter: int = 0
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


def main2(params):


    API_URL = params['API_URL']
    API_CATS_URL = params['API_CATS_URL']
    BOT_TOKEN = params['BOT_TOKEN']
    ERROR_TEXT = params['ERROR_TEXT']

    offset: int = -2
    counter: int = 0
    cat_response: requests.Response
    cat_link: str


    while counter < 100:
        print('attempt =', counter)
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                cat_response = requests.get(API_CATS_URL)
                if cat_response.status_code == 200:
                    cat_link = cat_response.json()['file']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                else:
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

        time.sleep(1)
        counter += 1


if __name__=="__main__":
    main2(params)
