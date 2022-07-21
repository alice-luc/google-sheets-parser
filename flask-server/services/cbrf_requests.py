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

