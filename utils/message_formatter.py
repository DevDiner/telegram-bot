# utils/message_formatter.py

def format_news_message(news):
    return f"**{news['title']}**\n\n{news['content']}\n[Read more]({news['link']})"

def split_message(text, max_length=4096):
    """Splits a long message into smaller chunks that fit within the Telegram limit."""
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]
