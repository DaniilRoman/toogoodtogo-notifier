from datetime import datetime


def __new_price(item: dict) -> str:
    price_item = item['item']['price_including_taxes']
    return __get_formatted_price(price_item)


def __old_price(item: dict) -> str:
    price_item = item['item']['value_including_taxes']
    return __get_formatted_price(price_item)


def __price_postfix(item: dict) -> str:
    return item['item']['value_including_taxes']['code']


def __get_formatted_price(price_item: dict) -> str:
    to_divide = 10 ** price_item['decimals']
    return f"{price_item['minor_units'] / to_divide}"  # {price_item['code']}"


def __convert_time(time: str) -> str:
    parsed_time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    return f"{parsed_time.time().hour}:{parsed_time.time().minute}"


def __is_today_postfix(time: str) -> str:
    parsed_time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    postfix = "tomorrow"
    if datetime.now().date() == parsed_time.date():
        postfix = "today"
    return postfix
