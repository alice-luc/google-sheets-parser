import json

import pydash as _

from gsheets_parser import get_data_from_gsheets as get_table
from cbrf_requests import get_usd_rate_from_central_bank as get_usd_rate


def get_completed_data_from_gsheets():
    gsheets_data = get_table()
    usd_rate = get_usd_rate()

    rate_in_rub = _.map_(gsheets_data['стоимость,$'], lambda el: float(el.replace(',', '.'))*usd_rate)
    gsheets_data['стоимость, руб'] = rate_in_rub

    with open('sample.json', 'w') as file:
        file.write(json.dumps(gsheets_data))
    print(gsheets_data)


if __name__ == "__main__":
    get_completed_data_from_gsheets()
