import logging

from tgtg import TgtgClient

from src.dynamodb import ItemStoreService
from src.item_to_str import item_to_str


def __get_items_str(tgtg_client: TgtgClient):
    items = tgtg_client.get_items(with_stock_only=True)
    return "\n".join([item_to_str(item) for item in items])


def get_items_str(tgtg_client: TgtgClient, item_store_service: ItemStoreService):
    try:
        actual_tickets = __get_items_str(tgtg_client)
        stored_tickets = item_store_service.get_item("tgtg_items")
        if actual_tickets != stored_tickets:
            item_store_service.save_item("tgtg_items", actual_tickets)
            return actual_tickets
        else:
            return ""
    except:
        logging.exception("Couldn't get TGTG items")
        return "Couldn't get TGTG items"
