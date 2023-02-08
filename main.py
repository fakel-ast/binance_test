import json
from enum import Enum

import asyncio
import websockets

from colors import TerminalColor


class BinancePropertiesEnum(Enum):
    current_price = 'c'
    high_price = 'h'


async def listen_currency_change():
    ws_url = "wss://stream.binance.com:9443/ws/btcusdt@ticker_1h"
    async with websockets.connect(ws_url) as websocket:
        while True:
            try:
                raw_currency_data = await websocket.recv()
                # parse and get prices
                currency_data = parse_json(raw_currency_data)
                current_price = float(currency_data.get(BinancePropertiesEnum.current_price.value))
                high_price = float(currency_data.get(BinancePropertiesEnum.high_price.value))

                changed_price_percent = 100 * (current_price - high_price) / current_price

                # if price increased print price with green color else red
                current_price_color = TerminalColor.green_text_color(f'Current price: {current_price}')
                if changed_price_percent < 0:
                    current_price_color = TerminalColor.red_text_color(f'Current price: {current_price}')

                # if change decreased >= 1% price this
                if changed_price_percent <= -1:
                    print(TerminalColor.red_text_color(f'Price decreased on {changed_price_percent} percent'), end=' ')

                print(current_price_color)
            except Exception as e:
                print(TerminalColor.orange_text_color(f'Program closed with error: {e}'))


def parse_json(raw_json: str):
    try:
        return json.loads(raw_json)
    except Exception as e:
        raise e


asyncio.run(listen_currency_change())
