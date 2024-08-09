import requests
from django.conf import settings


def send_telegram_message(message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}

    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f'Failed to send Telegram message: {response.text}')
    else:
        print('Telegram message sent successfully!')
