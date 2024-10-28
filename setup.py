#setup.py

from setuptools import setup, find_packages

setup(
    name="tg_news_bot",
    version="0.1.0",
    description="A Python package for a Telegram bot integrated with a crypto news scraper.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="DevDiner",
    author_email="demosampleacc@gmail.com",
    url="https://github.com/DevDiner/tg_news_bot",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyrogram",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
