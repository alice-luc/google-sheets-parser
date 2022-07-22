
GSHEETS_API_URLS = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'data/secureKey.json'
SPREADSHEETS_ID = '19axhkbnbVrIBHTvB3hTMEaJwylpMPNqaDNvEeuJs9vY'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'charset=utf-8'
}
CBR_URL = 'https://www.cbr.ru/scripts/XML_daily.asp'


NAMES_MAP = {
    "№": 'd_id',
    "заказ №": 'order_num',
    "срок поставки": 'date',
    "стоимость,$": 'usd_price',
    "стоимость, руб": 'rub_price'
}