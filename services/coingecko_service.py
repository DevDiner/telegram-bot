#services/coingecko_service.py

import requests
from config import config

class CoinGeckoService:
    def __init__(self):
        self.base_url = config.COINGECKO_BASE_URL

    def get_coin_price(self, coin_id):
        url = f"{self.base_url}/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{coin_id.capitalize()} price: ${data[coin_id]['usd']}"
        else:
            return f"Could not fetch price for {coin_id}. Please try again."

    def get_market_data(self, coin_ids):
        url = f"{self.base_url}/simple/price?ids={','.join(coin_ids)}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            market_data = []
            for coin_id in coin_ids:
                market_data.append(
                    f"{coin_id.capitalize()} - Price: ${data[coin_id]['usd']}, Market Cap: ${data[coin_id]['usd_market_cap']:,}, 24h Volume: ${data[coin_id]['usd_24h_vol']:,}"
                )
            return "\n".join(market_data)
        else:
            return "Could not fetch market data. Please try again."

    def get_trending_coins(self):
        url = f"{self.base_url}/search/trending"
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            data = response.json()
            trending_coins = [f"{coin['item']['name']} ({coin['item']['symbol']})" for coin in data['coins']]
            return "Trending Coins:\n" + "\n".join(trending_coins)
        else:
            return "Could not fetch trending coins. Please try again."

    def get_global_data(self):
        url = f"{self.base_url}/global"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['data']
            return (
                f"Global Crypto Market:\n"
                f"Market Cap: ${data['total_market_cap']['usd']:,}\n"
                f"24h Volume: ${data['total_volume']['usd']:,}\n"
                f"BTC Dominance: {data['market_cap_percentage']['btc']}%\n"
                f"ETH Dominance: {data['market_cap_percentage']['eth']}%\n"
                f"SOL Dominance: {data['market_cap_percentage']['sol']}%\n"
            )
        else:
            return "Could not fetch global data. Please try again."

    def get_coin_info(self, coin_id):
        url = f"{self.base_url}/coins/{coin_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (
                f"{data['name']} ({data['symbol'].upper()})\n\n"
                f"Market Cap Rank: {data['market_cap_rank']}\n"
                f"Current Price: ${data['market_data']['current_price']['usd']}\n"
                f"Market Cap: ${data['market_data']['market_cap']['usd']:,}\n"
                f"24h High: ${data['market_data']['high_24h']['usd']}\n"
                f"24h Low: ${data['market_data']['low_24h']['usd']}\n"
                f"Total Volume: ${data['market_data']['total_volume']['usd']:,}\n"
                f"Description: {data['description']['en'][:200]}..."  # Limiting description length
            )
        else:
            return f"Could not fetch info for {coin_id}. Please try again."

    def get_historical_data(self, coin_id, date):
        url = f"{self.base_url}/coins/{coin_id}/history?date={date}&localization=false"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (
                f"{data['name']} ({data['symbol'].upper()}) on {date}\n\n"
                f"Price: ${data['market_data']['current_price']['usd']}\n"
                f"Market Cap: ${data['market_data']['market_cap']['usd']:,}\n"
                f"24h Volume: ${data['market_data']['total_volume']['usd']:,}"
            )
        else:
            return f"Could not fetch historical data for {coin_id} on {date}. Please try again."

    def get_exchange_rates(self):
        url = f"{self.base_url}/exchange_rates"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['rates']
            rates = []
            for currency, details in data.items():
                rates.append(f"{details['name']} ({currency.upper()}): {details['value']}")
            return "Current Exchange Rates:\n" + "\n".join(rates)
        else:
            return "Could not fetch exchange rates. Please try again."

    def get_coin_market_chart(self, coin_id, days):
        url = f"{self.base_url}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            prices = data['prices']
            market_cap = data['market_caps']
            volumes = data['total_volumes']

            return (
                f"Market Chart for {coin_id.capitalize()} (Last {days} Days):\n\n"
                f"Prices: {prices}\n\n"
                f"Market Cap: {market_cap}\n\n"
                f"Volumes: {volumes}"
            )
        else:
            return f"Could not fetch market chart for {coin_id}. Please try again."

    def get_supported_coins(self):
        url = f"{self.base_url}/coins/list"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            coins = [f"{coin['name']} ({coin['symbol'].upper()})" for coin in data]
            return "Supported Coins:\n" + "\n".join(coins[:99]) + "\n...and many more."
        else:
            return "Could not fetch supported coins. Please try again."
