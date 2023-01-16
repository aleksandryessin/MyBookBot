import requests
import time
from src.load import load_params

params = load_params()

API_URL = params['API_URL']
BOT_TOKEN = params['BOT_TOKEN']
TEXT = params['TEXT']
MAX_COUNTER = params['MAX_COUNTER']

offset = params['offset']
counter = params['counter']
chat_id = params['chat_id']


def main():
    while counter < MAX_COUNTER:
        print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

        time.sleep(1)
        counter += 1


if __name__=="__main__":
    main()
