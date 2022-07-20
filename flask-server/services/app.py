# import pydash as _
# from pprint import pprint
import json

from services.gsheets_parser import get_data_from_gsheets as get_table
from services.cbrf_requests import get_usd_rate_from_central_bank as get_actual_usd_rate


def get_completed_data_from_gsheets() -> list:

    gsheets_data = get_table()
    # pprint(gsheets_data)

    # gsheets_data['стоимость, руб'] = _get_converted_values(gsheets_data)

    # return gsheets_data

    return _get_converted_values(gsheets_data)


def _get_converted_values(data: list) -> list:
    # delivery_dates = data['срок поставки']
    # delivery_prices = data['стоимость,$']
    rates_in_rubles = []
    # for el in delivery_dates[1:]:
    #     index = delivery_dates.index(el)
    #     rate = get_actual_usd_rate(el)
    #     price_in_usd = float(delivery_prices[index].replace(',', '.'))
    #     rates_in_rubles.append(price_in_usd * rate)
    data[0].append('стоимость, руб')
    usd_index = data[0].index('стоимость,$')
    date_index = data[0].index('срок поставки')

    for el in data[1:]:
        el[date_index] = el[date_index].replace(".", "/")
        rate = get_actual_usd_rate(el[date_index])
        price_in_usd = float(el[usd_index].replace(',', '.'))
        el.append(price_in_usd * rate)
    with open('test.json', 'w') as file:
        file.write(json.dumps(data))
    return data


if __name__ == "__main__":
    get_completed_data_from_gsheets()
