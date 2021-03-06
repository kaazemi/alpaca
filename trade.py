
import requests, json
from config import *

# ENDPOINT_URL = 'https://api.alpaca.markets'
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = f"{BASE_URL}/v2/account"
ORDERS_URL = f"{BASE_URL}/v2/orders"
HEADERS = {'APCA-API-KEY-ID': API_KEY,
            'APCA-API-SECRET-KEY':SECRET_KEY
            }
class TRADER(object):
    def __init__(self) -> None:
        super().__init__()

    def get_account(self):
        r = requests.get(ACCOUNT_URL, headers = HEADERS)
        print(r.content)
        return json.loads(r.content)
    def create_order(self,symbol, qty, side, type, time_in_force):
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force
        }
        r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
        return json.loads(r.content)

    def get_orders(self):
        r = requests.get(ORDERS_URL, headers=HEADERS)
        return json.loads(r.content)


trader = TRADER()
# response = trader.create_order("AAPL", 1, "buy", "market", "gtc")
# print(response)
# response = trader.create_order("MSFT", 1000, "buy", "market", "gtc")
orders = trader.get_orders()
print(orders)