import logging

import telepot
from decouple import config
from tgtg import TgtgClient

from src.dynamodb import DynamodbConfig, ItemStoreService
from src.items_getter import get_items_str

TELEGRAM_CHAT_IDS = config("TELEGRAM_CHAT_ID").split(",")
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")

TGTG_ACCESS_TOKEN = config("TGTG_ACCESS_TOKEN")
TGTG_REFRESH_TOKEN = config("TGTG_REFRESH_TOKEN")
TGTG_USER_ID = config("TGTG_USER_ID")

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_REGION_NAME = config("AWS_REGION_NAME")

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
                    filemode="w")

dynamodb_config = DynamodbConfig(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION_NAME)
item_store_service = ItemStoreService(dynamodb_config)

tgtg_client = TgtgClient(
    access_token=TGTG_ACCESS_TOKEN,
    refresh_token=TGTG_REFRESH_TOKEN,
    user_id=TGTG_USER_ID)


def __get_creds(email: str) -> dict:
    client = TgtgClient(email=email)
    credentials = client.get_credentials()
    logging.info(credentials)
    return credentials


def __send_telegram_message(msg):
    if msg == "":
        logging.info("Nothing to send")
    else:
        bot = telepot.Bot(TELEGRAM_TOKEN)
        bot.getMe()
        for chat_id in TELEGRAM_CHAT_IDS:
            bot.sendMessage(chat_id, msg)


if __name__ == '__main__':
    msg = get_items_str(tgtg_client, item_store_service)
    __send_telegram_message(msg)
