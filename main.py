import telepot
from decouple import config
from tgtg import TgtgClient

from src.item_to_str import __item_to_str

TELEGRAM_CHAT_ID = config("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
TGTG_ACCESS_TOKEN = config("TGTG_ACCESS_TOKEN")
TGTG_REFRESH_TOKEN = config("TGTG_REFRESH_TOKEN")
TGTG_USER_ID = config("TGTG_USER_ID")


def __get_creds(email: str) -> dict:
    client = TgtgClient(email=email)
    credentials = client.get_credentials()
    print(credentials)
    return credentials


def __get_items_str():
    client = TgtgClient(
        access_token=TGTG_ACCESS_TOKEN,
        refresh_token=TGTG_REFRESH_TOKEN,
        user_id=TGTG_USER_ID)

    items = client.get_items(with_stock_only=True)
    return "\n".join([__item_to_str(item) for item in items])


def __send_telegram_message(msg):
    bot = telepot.Bot(TELEGRAM_TOKEN)
    bot.getMe()
    bot.sendMessage(TELEGRAM_CHAT_ID, msg)


if __name__ == '__main__':
    msg = __get_items_str()
    __send_telegram_message(msg)
