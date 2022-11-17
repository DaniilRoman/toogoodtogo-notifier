from src.helpers import __old_price, __new_price


def __display_name(item: dict) -> str:
    return item['display_name']


def __price_change(item: dict) -> str:
    return f"{__old_price(item)} --> {__new_price(item)}"


def __time_interval(item: dict) -> str:
    return f"{item['pickup_interval']['start']} -- {item['pickup_interval']['end']}"


def __items_available(item: dict) -> str:
    return f"{item['items_available']} items available"


def __distance(item: dict) -> str:
    formatted_distance = round(item['distance'] / 1000, 2)
    return f"{formatted_distance} km"


def __item_to_str(item: dict) -> str:
    return f"""
{__display_name(item)}:
  {__price_change(item)}
  {__time_interval(item)}
  {__distance(item)}
  {__items_available(item)}
    """
