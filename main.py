#main.py

import sys
import os

# Add the directory containing 'cointelegraph_news_scraper' to sys.path
sys.path.append('/root/folder')
# Add the directory containing 'services' to sys.path
# current_dir = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, current_dir)
#sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)


import asyncio
from pyrogram import Client, filters
from config import config
from services.telegram_service import TelegramService
from services.coingecko_service import CoinGeckoService
from services.news_poster_service import NewsPosterService
from services.cointelegraph_news_fetcher import CointelegraphNewsFetcher
from services.api_news_fetcher import APINewsFetcher
from utils.log_utils import setup_logging

#for deployment of google cloud
# from flask import Flask

# # Set up Flask app
# app_flask = Flask(__name__)

# @app_flask.route("/")
# def home():
#     return "Telegram bot is running..."

#Telegram Bot Setup
logger = setup_logging()

bot_app = Client("news_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

telegram_service = TelegramService(bot_app)
coingecko_service = CoinGeckoService()

# Select the appropriate news fetcher based on the .env configuration
if config.NEWS_FETCHER_TYPE == 'cointelegraph':
    news_fetcher = CointelegraphNewsFetcher()
elif config.NEWS_FETCHER_TYPE == 'api':
    news_fetcher = APINewsFetcher(api_url=config.API_NEWS_URL)
else:
    raise ValueError("Invalid NEWS_FETCHER_TYPE specified in the .env file")

news_poster_service = NewsPosterService(bot_app, news_fetcher=news_fetcher)

@bot_app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Welcome to the Crypto News Bot! Use /news to get the latest news and /help for a list of commands.")

# Help command to list all the available commands
@bot_app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """
Here are the available commands:
- /start: Start the bot and see the welcome message.
- /fetch_latest_news: Fetch and post the latest news in the chat.(Will only post articles that are not in database)
- /news: Get the latest news articles from database. ( Please run "/fetch_latest_news" first to update database)
- /price <coin_id>: Get the price of a specific cryptocurrency (e.g., /price bitcoin).
- /market <coin_ids>: Get market data for one or more cryptocurrencies (e.g., /market bitcoin ethereum).
- /trending: Get a list of trending cryptocurrencies.
- /global: Get global cryptocurrency market data.
- /coininfo <coin_id>: Get detailed information about a specific cryptocurrency (e.g., /coininfo bitcoin).
- /history <coin_id> <date>: Get historical data for a specific cryptocurrency on a given date (e.g., /history bitcoin 30-12-2022).
- /exchange: Get the latest cryptocurrency exchange rates.
- /chart <coin_id> <days>: Get a market chart for a specific cryptocurrency over the last <days> days (e.g., /chart bitcoin 30).
- /coins: List supported coins.
"""
    await message.reply(help_text)

# Other commands
# Fetch latest news from MongoDB and send it in the chat
@bot_app.on_message(filters.command("news"))
async def send_news(client, message):
    news_list = await news_poster_service.fetch_latest_news_from_mongo()
    if news_list:
        for news in news_list:
            await message.reply(news)
    else:
        await message.reply("No news found in the database.")


# async def send_news(client, message):
#     chat_id = message.chat.id
#     await news_poster_service.fetch_and_post_latest_news(chat_id)

@bot_app.on_message(filters.command("fetch_latest_news"))
async def fetch_and_post_latest_news(client, message):
    chat_id = message.chat.id

    # Notify the user that scraping has started
    status_message = await message.reply("Fetching latest news... This may take a moment.")

    try:
        # Simulate wait time and provide periodic updates (if the scraping is long-running)
        for i in range(5):
            await asyncio.sleep(1)
            await bot_app.edit_message_text(chat_id=chat_id, message_id=status_message.id,
                                        text=f"Fetching latest news... Still fetching ({i + 1} seconds passed).")
        
        # Run the scraping process and get the latest news
        articles = await news_poster_service.fetch_and_post_news(chat_id)
        
        if not articles:
            # If no articles are fetched, notify the user
            await bot_app.edit_message_text(chat_id=chat_id, message_id=status_message.id,
                                        text="No new articles were found.")
            return

        # Once scraping is done, notify the user
        await bot_app.edit_message_text(chat_id=chat_id, message_id=status_message.id,
                                    text="Fetching complete. Posting latest news...")

        # Post each article as a separate message
        for article in articles:
            formatted_message = format_news_message(article)  # Assuming format_news_message formats the article
            await bot_app.send_message(chat_id=chat_id, text=formatted_message)

        # Notify the user that all articles have been posted
        await bot_app.send_message(chat_id=chat_id, text="All articles have been posted.")

    except Exception as e:
        # If there's an error, log it and notify the user
        logger.error(f"Error fetching and posting news: {e}", exc_info=True)
        await bot_app.edit_message_text(chat_id=chat_id, message_id=status_message.id,
                                    text="An error occurred while fetching the news. Please try again later.")


@bot_app.on_message(filters.command("price"))
async def send_price(client, message):
    coin_id = message.text.split()[1] if len(message.text.split()) > 1 else None
    if coin_id:
        price_info = coingecko_service.get_coin_price(coin_id)
        await message.reply(price_info)
    else:
        await message.reply("Please provide a coin ID, e.g., /price bitcoin , /price ethereum, /price solana")

@bot_app.on_message(filters.command("market"))
async def send_market_data(client, message):
    coin_ids = message.text.split()[1:] if len(message.text.split()) > 1 else []
    if coin_ids:
        market_data = coingecko_service.get_market_data(coin_ids)
        await message.reply(market_data)
    else:
        await message.reply("Please provide one or more coin IDs, e.g., /market bitcoin ethereum solana")

@bot_app.on_message(filters.command("trending"))
async def send_trending_coins(client, message):
    trending_coins = coingecko_service.get_trending_coins()
    await message.reply(trending_coins)

@bot_app.on_message(filters.command("global"))
async def send_global_data(client, message):
    global_data = coingecko_service.get_global_data()
    await message.reply(global_data)

@bot_app.on_message(filters.command("coininfo"))
async def send_coin_info(client, message):
    coin_id = message.text.split()[1] if len(message.text.split()) > 1 else None
    if coin_id:
        coin_info = coingecko_service.get_coin_info(coin_id)
        await message.reply(coin_info)
    else:
        await message.reply("Please provide a coin ID, e.g., /coininfo bitcoin , /coininfo ethereum, /coininfo solana")

@bot_app.on_message(filters.command("history"))
async def send_historical_data(client, message):
    try:
        coin_id = message.text.split()[1]
        date = message.text.split()[2]  # Date in format dd-mm-yyyy
        historical_data = coingecko_service.get_historical_data(coin_id, date)
        await message.reply(historical_data)
    except IndexError:
        await message.reply("Please provide a coin ID and date, e.g., /history bitcoin 30-12-2022")

@bot_app.on_message(filters.command("exchange"))
async def send_exchange_rates(client, message):
    exchange_rates = coingecko_service.get_exchange_rates()
    await message.reply(exchange_rates)

@bot_app.on_message(filters.command("chart"))
async def send_market_chart(client, message):
    try:
        coin_id = message.text.split()[1]
        days = int(message.text.split()[2])  # Number of days for the chart
        market_chart = coingecko_service.get_coin_market_chart(coin_id, days)
        await message.reply(market_chart)
    except (IndexError, ValueError):
        await message.reply("Please provide a coin ID and number of days, e.g., /chart bitcoin 30")

@bot_app.on_message(filters.command("coins"))
async def send_supported_coins(client, message):
    supported_coins = coingecko_service.get_supported_coins()
    await message.reply(supported_coins)

# Run Flask server and the bot
if __name__ == "__main__":
    # Run Flask server in a separate thread
    #import threading
    #threading.Thread(target=lambda: app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))).start()
    
    # Run the Telegram bot
    bot_app.run()