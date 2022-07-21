import json

from services.gsheets_parser import get_data_from_gsheets as get_table
from services.cbrf_requests import get_usd_rate_from_central_bank as get_actual_usd_rate


def get_completed_data_from_gsheets() -> list:

    gsheets_data = get_table()
    return _get_converted_values(gsheets_data)


def _get_converted_values(data: list) -> list:

    data[0].append('стоимость, руб')
    usd_index = data[0].index('стоимость,$')
    date_index = data[0].index('срок поставки')

    for el in data[1:]:
        el[date_index] = el[date_index].replace(".", "/")
        rate = get_actual_usd_rate(el[date_index])

        price_in_usd = float(el[usd_index].replace(',', '.'))
        el.append(price_in_usd * rate)
    # with open('test.json', 'w') as file:
    #     file.write(json.dumps(data))
    return data


if __name__ == "__main__":
    get_completed_data_from_gsheets()
