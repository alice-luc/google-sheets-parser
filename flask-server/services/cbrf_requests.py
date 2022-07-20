import pydash as _
import requests
import xmltodict

from data.constants import HEADERS, CBR_URL


def get_usd_rate_from_central_bank(date: str | None) -> float:
    url = CBR_URL + f'?date_req={date}' if date else CBR_URL
    response = requests.get(url, headers=HEADERS)

    tree_raw = xmltodict.parse(response.text)
    tree = tree_raw['ValCurs']['Valute']

    usd_data = _.find(tree, lambda el: el['CharCode'] == "USD")
    usd_rate = float(usd_data['Value'].replace(',', '.'))
    return usd_rate


# def get_usd_rate_from_central_bank_by_date() -> float:
#     pass

# print(get_usd_rate_from_central_bank())

# print(usd_rate)


# import json
# # for currency in tree.iter('Item'):
#
# print(json.dumps(tree))
#
# with open('cb.xml', 'w') as file:
#     file.write(response.text)

# with open('cb.xml', encoding='utf-8') as file:
#     tree_raw = xmltodict.parse(file.read())
