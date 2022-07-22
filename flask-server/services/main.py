# import asyncio
# from datetime import datetime

from services.gsheets_parser import get_data_from_gsheets as get_table
from services.cbrf_requests import get_usd_rate_from_central_bank as get_actual_usd_rate
# from services.telegram_notification import notify


def get_completed_data_from_gsheets() -> list:

    gsheets_data = get_table()
    return _get_converted_values(gsheets_data)


def _get_converted_values(data: list) -> list:

    data[0].append('стоимость, руб')
    usd_index = data[0].index('стоимость,$')
    rate = get_actual_usd_rate(None)
    # order_index = data[0].index('заказ №')

    for el in data[1:]:
        """ 
            In case we need to make a requests for the past dates on each element
            Replace this function with the on at the end of the document  
        """
        # if datetime.strptime(el[date_index], '%d/%m/%y') < datetime.now():
        #     asyncio.run(notify(el[order_index]))

        price_in_usd = float(el[usd_index].replace(',', '.'))
        el.append(price_in_usd * rate)

    return data


if __name__ == "__main__":
    get_completed_data_from_gsheets()


# def _get_converted_values(data: list) -> list:
#
#     data[0].append('стоимость, руб')
#     usd_index = data[0].index('стоимость,$')
#     date_index = data[0].index('срок поставки')
#     rate = get_actual_usd_rate(None)
#     # order_index = data[0].index('заказ №')
#     for el in data[1:]:
#         """
#             In case we need to make a requests for the past dates on each element
#             Replace this function with the on at the end of the document
#         """
#         el[date_index] = el[date_index].replace(".", "/")
#        if datetime.strptime(el[date_index], '%d/%m/%y') < datetime.now():
#            rate = get_actual_usd_rate(el[date_index])
#
#         #  asyncio.run(notify(el[order_index]))
#
#         price_in_usd = float(el[usd_index].replace(',', '.'))
#         el.append(price_in_usd * rate)
#
#     return data
