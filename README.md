# Crypto News Telegram Bot

A Python-based Telegram bot that integrates with cryptocurrency data from CoinGecko's API and a flexible news fetching service (CoinTelegraph or any other API). This bot provides real-time cryptocurrency updates and posts the latest news in a specified chat, making it reusable for multiple projects.

## Features

- **Real-time Cryptocurrency Prices**: Fetches the current price of a specific cryptocurrency.
- **Market Data**: Provides market data for multiple cryptocurrencies (e.g., price, market cap, 24-hour volume).
- **Trending Coins**: Lists the top trending cryptocurrencies.
- **Global Market Data**: Displays the global cryptocurrency market statistics (e.g., market cap, 24-hour volume, BTC/ETH dominance).
- **Coin Information**: Detailed information about a specific cryptocurrency (e.g., market cap rank, current price, 24-hour high/low).
- **Historical Data**: Fetches historical price data for a specific cryptocurrency on a specific date.
- **Exchange Rates**: Displays the current exchange rates between cryptocurrencies and fiat currencies.
- **Coin Market Charts**: Provides the market chart data for a coin over a specified number of days.
- **News Fetching Service**: Fetches the latest cryptocurrency news from CoinTelegraph or a user-specified API endpoint and posts it in the chat.
- **Real-time Scraper Logs and Updates**: Displays status messages and updates while scraping the latest news to improve the user experience.

## Project Structure

- `interfaces/`: Contains the abstract interface for the news fetcher, making it easy to extend the bot for new APIs.
- `services/`: Contains the services for fetching news, interacting with CoinGecko's API, and Telegram bot services.
  - `api_news_fetcher.py`: A service for interacting with an external news API.
  - `cointelegraph_news_fetcher.py`: A service that fetches news from CoinTelegraph using the scraper.
  - `coingecko_service.py`: Service that fetches data from CoinGecko.
  - `telegram_service.py`: Manages interaction with the Telegram bot API.
  - `news_poster_service.py`: Fetches the news and posts it in the specified Telegram chat.
- `utils/`: Utility modules such as logging and message formatting.

## Getting Started
## Important Directory and Docker Configuration Notes

To ensure the Telegram bot and the Cointelegraph news scraper work seamlessly, you have two directory organization options:

1. **Telegram Bot Directory within the News Scraper Directory**: Place the entire Telegram bot project within the Cointelegraph news scraper directory.
   
2. **Separate Directories for Bot and Scraper**: If you prefer to keep the Telegram bot and Cointelegraph scraper as independent modules at the same directory level, ensure the following:
   - Both directories must be at the same level in your file structure.
   - Place the `Dockerfile` and `docker-compose.yml` files at the same level as both directories.
   - This configuration allows you to run both modules together and ensures they communicate smoothly when deployed in Docker containers.

### Example Directory Structure

Here’s an example of the recommended directory structure for both setups:

#### Option 1: Telegram Bot Inside News Scraper Directory
```
cointelegraph_news_scraper/
├── telegram_bot/                 # Place Telegram bot files here
├── services/
├── utils/
├── main.py
├── Dockerfile                    # For the combined service
└── docker-compose.yml            # For the combined service
```

#### Option 2: Telegram Bot and News Scraper as Independent Modules
```
project_root/
├── cointelegraph_news_scraper/    # Scraper files here
│   ├── services/
│   ├── utils/
│   ├── main.py
├── telegram_bot/                  # Telegram bot files here
├── Dockerfile                     # Shared Dockerfile
└── docker-compose.yml             # Shared docker-compose file
```

In **Option 2**, `Dockerfile` and `docker-compose.yml` are at the `project_root` level. This configuration allows Docker to run both the scraper and bot in separate containers while ensuring connectivity between them.

### Prerequisites

- Python 3.6 or later
- Telegram Bot Token (obtained from [BotFather](https://core.telegram.org/bots#botfather))
- Telegram API ID and Hash (obtained from [my.telegram.org](https://my.telegram.org))
- Coingecko API key
- Docker 
- Cointelegraph-news-scraper [Optional]
- Mobile Number

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DevDiner/cointelegraph-news-scraper.git
   git clone https://github.com/DevDiner/tg_news_bot.git
   cd tg_news_bot
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the environment variables:**

   Copy the `.env.example` file to `.env` and fill in the necessary values:

   ```bash
   cp .env.example .env
   ```

   Update the following fields in `.env`:

   - `BOT_TOKEN`: Your Telegram bot token.
   - `API_ID`: Your Telegram API ID.
   - `API_HASH`: Your Telegram API Hash.
   - `PHONE_NUMBER`: Your phone number linked to Telegram.
   - `NEWS_FETCHER_TYPE`: Set to either `cointelegraph` (to use the CoinTelegraph scraper) or `api` (to use a custom API endpoint).
   - `API_NEWS_URL`: (Required only if `NEWS_FETCHER_TYPE=api`) The URL of the external news API.
   - `COINGECKO_BASE_URL`: The base URL for CoinGecko's API (usually does not need modification).

4. **Run the bot:**

   ```bash
   python main.py
   ```

### Commands

Once your bot is running, you can interact with it using the following commands:

- `/start`: Start the bot and receive a welcome message.
- `/news`: Fetch the latest news from the database (run `/fetch_latest_news` first to update the database).
- `/fetch_latest_news`: Scrape the latest news from CoinTelegraph or API and post it in the chat.
- `/price <coin_id>`: Fetch the current price of a specific cryptocurrency (e.g., `/price bitcoin`).
- `/market <coin_ids>`: Fetch the market data for multiple cryptocurrencies (e.g., `/market bitcoin ethereum`).
- `/trending`: View the top trending cryptocurrencies.
- `/global`: Get an overview of the global cryptocurrency market.
- `/coininfo <coin_id>`: Get detailed information about a specific coin (e.g., `/coininfo bitcoin`).
- `/history <coin_id> <date>`: Get historical data for a specific coin on a specific date (e.g., `/history bitcoin 30-12-2022`).
- `/exchange`: Get the current exchange rates between cryptocurrencies and fiat currencies.
- `/chart <coin_id> <days>`: Get the market chart data for a coin over a specified number of days (e.g., `/chart bitcoin 30`).
- `/coins`: List the first 20 supported coins from CoinGecko.
- `/help`: List all available commands.

### Enhanced User Experience

- **Real-time Scraper Status**: When running the `/fetch_latest_news` command, the bot provides real-time updates on the scraping process, including status messages and any delays in fetching.
- **Error Handling**: If any errors occur during news fetching or posting, the bot will notify the user in the chat.

## Project Configuration

The project configuration is managed through environment variables. To modify these, edit the `.env` file. Here are the available configuration options:

- `BOT_TOKEN`: The bot token from Telegram.
- `API_ID`: The API ID from Telegram.
- `API_HASH`: The API hash from Telegram.
- `PHONE_NUMBER`: The phone number associated with your Telegram account.
- `NEWS_FETCHER_TYPE`: Can be `cointelegraph` (for CoinTelegraph scraper) or `api` (for external API).
- `API_NEWS_URL`: The API URL used if `NEWS_FETCHER_TYPE` is set to `api`.
- `COINGECKO_BASE_URL`: The CoinGecko API base URL (default is `https://api.coingecko.com/api/v3`).
- `LOG_LEVEL`: The log level for the application (`info`, `debug`, `warning`, `error`).



## Deployment Guide

## Running the Bot Using Docker

### Prerequisites

1. **Docker**: Install Docker on your system using the official [Docker documentation](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Ensure Docker Compose is installed to manage multi-container Docker applications.
   - Install Docker Compose: 
     ```bash
     sudo apt install docker-compose
     ```

### Step-by-Step Guide to Running the Bot and MongoDB Using Docker Compose

#### 1. **Creating a Docker Network**

To allow the two services (MongoDB and the Telegram bot) to communicate, we need to create a Docker network. If your `docker-compose.yml` uses an external network, create it manually:

```bash
docker network create network_1
```

#### 2. **Docker Compose File Overview**

Ensure that your `docker-compose.yml` file contains the following structure to define two services: one for MongoDB and one for the Telegram bot. The file also specifies the use of a common network:

```yaml
version: '3.8'

services:
  # MongoDB service
  mongo:
    image: mongo:5.0  # MongoDB image version
    container_name: #container name
    profiles: ["all", "mongo"]
    ports:
      -  # Expose MongoDB's port to the host machine
    volumes:
      - # Persistent storage for MongoDB data
    networks:
      - #hetwork name, connect to the external network

  # Telegram bot service
  telegram_bot:
    image: #image name
    profiles: ["all", "bot"]
    build:
      context: .  # The directory where Dockerfile is located
      dockerfile: Dockerfile  # Ensure you have a valid Dockerfile in this directory
    container_name: #container name
    ports:
      - # Expose the bot’s port if needed
    volumes:
      - :/app/.env  # Load environment variables
    restart: on-failure  # Automatically restart the bot on failure
    networks:
      -   # same as above, connect to the external network

volumes:
  mongo_data:
    driver: local  # MongoDB persistent data

networks:
  network_1:
    external: true  # Use the existing external network
```

#### 3. **Building and Running the Docker Services**

To build and run the services (MongoDB and Telegram bot), use the following commands:

- **Build and Start Services**:
  
  ```bash
  docker compose --profile all up --build
  ```

This command will build the images if they aren't already built and start the services in the specified profiles (`mongo` and `bot`).

- **Run in the Background**:
  
  If you want to run the services in the background and not tie up the terminal, use `nohup`:
  
  ```bash
  nohup docker compose --profile all up --build > docker-compose.log 2>&1 &
  ```

This command will:
  - Run the services in the background.
  - Log output to `docker-compose.log`.
  - Keep running after you log out of the session.

- **Stopping the Services**:
  
  To stop all the services and clean up resources (like containers and networks), use:

  ```bash
  docker compose --profile all down
  ```

#### 4. **Checking Logs and Debugging**

- **To Check Logs**:
  
  To monitor the logs of the running services, use:

  ```bash
  docker logs telegram_bot
  docker logs mongo_db
  ```

  You can also follow the logs in real-time using the `-f` flag:

  ```bash
  docker logs -f telegram_bot
  docker logs -f mongo_db
  ```

---

## Deploying on Raspberry Pi 5 Model B Using Docker Compose

To deploy the entire service (MongoDB and Telegram bot) on a Raspberry Pi 5 Model B, follow these steps:

### 1. **Install Docker on Raspberry Pi**

- **Update your system**:
  
  ```bash
  sudo apt update
  sudo apt upgrade
  ```

- **Install Docker**:
  
  Docker has an official installation script that works well with Raspberry Pi:
  
  ```bash
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  ```

- **Install Docker Compose**:
  
  To manage multi-container applications, install Docker Compose:
  
  ```bash
  sudo apt install docker-compose
  ```

### 2. **Deploy the Application Using Docker Compose**

- **Transfer the Project Files**:
  
  Use SCP or another transfer method to copy the project directory containing your `Dockerfile` and `docker-compose.yml` to your Raspberry Pi.

- **Create the Network**:

  As with any other system, create the network if required:

  ```bash
  docker network create network_1
  ```

- **Build and Run the Services**:
  
  Once you have transferred the files, navigate to the project directory on your Raspberry Pi and run:

  ```bash
  docker compose --profile all up --build
  ```

  If you want the process to run in the background, use:

  ```bash
  nohup docker compose --profile all up --build > docker-compose.log 2>&1 &
  ```

### 3. **Accessing the Services**

Once the services are up and running, you can interact with your Telegram bot as usual. MongoDB will be running and accessible on port 27020, and the bot will be available on port 8080.

### 4. **Maintaining the Service on Raspberry Pi**

- **Stopping Services**:
  
  Use the following to stop and remove the services:

  ```bash
  docker compose --profile all down
  ```

- **Monitoring Logs**:

  You can monitor the logs for both services on Raspberry Pi by using the same commands:

  ```bash
  docker logs -f telegram_bot
  docker logs -f mongo_db
  ```

---


## Running Services Without Docker Compose

If you want to run your MongoDB and Telegram bot services **manually using Docker** without relying on Docker Compose, follow the steps below:

### Step 1: Build the Docker Images

1. **Navigate to the project directory**:
   
   Open a terminal and navigate to the folder where your `Dockerfile` is located.

   ```bash
   cd /path/to/your/project
   ```

2. **Build the Docker image for the Telegram bot**:
   
   Use the `docker build` command to create a Docker image for the Telegram bot service. The `-t` flag is used to name the image (e.g., `tg_bot_1`).

   ```bash
   docker build -t tg_bot_1 .
   ```

   This will build the Docker image from your `Dockerfile`.

### Step 2: Run MongoDB as a Container

To run MongoDB as a service, execute the following command:

```bash
docker run --name mongo_db -d -p 27020:27017 -v mongo_data:/data/db mongo:5.0
```

- `--name mongo_db`: Names the container `mongo_db`.
- `-d`: Runs the container in the background (detached mode).
- `-p 27020:27017`: Maps port 27020 on your host to port 27017 in the MongoDB container.
- `-v mongo_data:/data/db`: Maps a Docker volume (`mongo_data`) to persist MongoDB data.

This command starts MongoDB and allows it to persist data in the `mongo_data` volume. The MongoDB container is now running and accessible on port 27020.

### Step 3: Run the Telegram Bot Service

Once the MongoDB container is running, you can start the Telegram bot using the Docker image you built earlier.

1. **Run the Telegram bot**:

   ```bash
   docker run --name telegram_bot --env-file ./telegram_bot/.env -p 8080:8080 --network="host" tg_bot_1
   ```

   - `--name telegram_bot`: Names the container `telegram_bot`.
   - `--env-file [env path]: Specifies the environment file that contains your configuration.
   - `-p 8080:8080`: Exposes the bot's port 8080 to the host.
   - `--network="host"`: Runs the container on the host network so it can communicate with the MongoDB service.
   - `tg_bot_1`: The name of the Docker image built for the Telegram bot.

This will start the bot in the foreground. If you want it to run in the background (detached mode), use the `-d` flag:

```bash
docker run --name telegram_bot --env-file [env path] -p 8080:8080 --network="host" -d tg_bot_1
```

### Step 4: Verify Both Services Are Running

You can verify the running containers by using the following command:

```bash
docker ps
```

This command will list all running containers, and you should see `mongo_db` and `telegram_bot` listed.

### Step 5: Stopping the Containers

- To stop the MongoDB container:

  ```bash
  docker stop mongo_db
  ```

- To stop the Telegram bot container:

  ```bash
  docker stop telegram_bot
  ```

### Step 6: Remove the Containers

If you need to remove the containers after stopping them, use:

```bash
docker rm mongo_db telegram_bot
```

This will remove both the MongoDB and Telegram bot containers.

### Step 7: View Logs

You can view logs for each service by running:

- For MongoDB:

  ```bash
  docker logs mongo_db
  ```

- For the Telegram bot:

  ```bash
  docker logs telegram_bot
  ```

### Step 8: Manual Networking (Optional)

If you don't want to use `--network="host"` for the Telegram bot and MongoDB to communicate, you can manually create a Docker network and attach both containers to it:

1. **Create a network**:

   ```bash
   docker network create [network name]
   ```

2. **Run MongoDB on the custom network**:

   ```bash
   docker run --name mongo_db --network [network name] -d -p [mongo port:mongo port] -v mongo_data:/data/db mongo:5.0
   ```

3. **Run the Telegram bot on the same network**:

   ```bash
   docker run --name telegram_bot --env-file ./telegram_bot/.env --network network_1 -p 8080:8080 -d tg_bot_1
   ```

By connecting both services to the same network (`network_1`), they will be able to communicate directly using container names (e.g., the Telegram bot can access MongoDB using `mongo_db:27017`).

---

## Guide to Deploy the Services on a Raspberry Pi 5 Model B

If you're using a Raspberry Pi 5 Model B, you can deploy the services using the same steps as described above but with Raspberry Pi-specific Docker installations.

### Step 1: Install Docker on Raspberry Pi

Follow these steps to install Docker on your Raspberry Pi:

1. **Update the Raspberry Pi system**:

   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. **Install Docker**:

   Use the official Docker installation script:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

3. **Install Docker Compose**:

   To manage multi-container Docker applications, install Docker Compose:

   ```bash
   sudo apt install docker-compose
   ```

### Step 2: Build and Run the Docker Containers on Raspberry Pi

After setting up Docker and Docker Compose, transfer your project files to the Raspberry Pi and follow the steps mentioned earlier:

1. **Build the Docker image**:

   ```bash
   docker build -t tg_bot_1 .
   ```

2. **Run MongoDB on Raspberry Pi**:

   ```bash
   docker run --name mongo_db -d -p [mongo port: mongo port] -v mongo_data:/data/db mongo:5.0
   ```

3. **Run the Telegram bot on Raspberry Pi**:

   ```bash
   docker run --name telegram_bot --env-file [file path].env -p [port:port] --network="host" tg_bot_1
   ```

4. **Check Logs**:

   You can check the logs to ensure the bot is running correctly:

   ```bash
   docker logs telegram_bot
   ```

Now your services will be up and running on your Raspberry Pi.

---


### Deploying to AWS EC2 (Free Tier)

1. **Create an EC2 Instance**:
   - Use the AWS EC2 dashboard to create a new instance, selecting the free tier (t2.micro).
   - Configure security groups to allow SSH (port 22) and your bot’s application port (e.g., 8080).

2. **Transfer Docker Image to EC2**:
   - Use `scp` to transfer your Docker image:
     ```bash
     scp -i your-key.pem telegram_bot_aws.tar ubuntu@your-ec2-ip:~
     ```
   - SSH into the instance:
     ```bash
     ssh -i your-key.pem ubuntu@your-ec2-ip
     ```
   - Extract and load the Docker image:
     ```bash
     tar -xf telegram_bot_aws.tar
     docker load < telegram_bot_aws.tar
     ```

3. **Run Docker Compose**:
   - Make sure the `docker-compose.yml` file

 is correctly configured as shown above and run:
     ```bash
     docker-compose up -d
     ```

### Deploying to Google Cloud Run

1. **Build and Push the Docker Image**:
   - Use `gcloud` CLI to build and push the Docker image to Google Container Registry.

2. **Deploy with Google Cloud Run**:
   - Deploy using:
     ```bash
     gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/telegram_bot_1 --platform managed --region us-central1 --allow-unauthenticated --port 8080
     ```

3. **Setting up MongoDB**:
   - Ensure your MongoDB service (e.g., Atlas or Dockerized MongoDB) is accessible from Google Cloud Run.

### Future Enhancements

- **Optimizing Docker Image Size**: Reduce image size to fit within free-tier limits.
- **Alternative Cloud Solutions**: Experiment with other cloud providers or on-premise solutions to ensure a 24/7 runtime without additional costs.
- **Deploy from Local VM to Cloud**: Include comprehensive steps for deploying from a local VM to Google Cloud and AWS EC2 instances.

## Running the Tests

If you have written tests for this project, you can run them using `pytest`:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
