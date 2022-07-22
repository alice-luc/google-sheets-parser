# from telethon.sync import TelegramClient
# import configparser
# import logging
#
# # reading configurations from file
# config = configparser.ConfigParser()
# config.read("config.ini")
#
# # parsing configurations
# api_id = int(config['Telegram']['api_id'])
# api_hash = config['Telegram']['api_hash']
# username = config['Telegram']['username']
# user = config['Telegram']['user']
#
#
# logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%Y-%m/%dT%H:%M:%S',
#                     filename='../log/logfile.log', level=logging.DEBUG)

#
# async def notify(order_num: str) -> None:
#     client = TelegramClient(username, api_id, api_hash)
#     client.start()
#     message = f'Поставка номер {order_num} уже должна была прийти'
#     try:
#         await client.send_message(user, message)
#     except AttributeError as error:
#         logging.error(error)
