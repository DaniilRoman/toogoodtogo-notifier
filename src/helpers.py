def __new_price(item: dict) -> str:
    price_item = item['item']['price_including_taxes']
    return __get_formatted_price(price_item)


def __old_price(item: dict) -> str:
    price_item = item['item']['value_including_taxes']
    return __get_formatted_price(price_item)


def __get_formatted_price(price_item: dict) -> str:
    to_divide = 10 ** price_item['decimals']
    return f"{price_item['minor_units'] / to_divide} {price_item['code']}"
