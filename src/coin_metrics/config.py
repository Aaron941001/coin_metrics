# Line Bot 配置
LINE_CHANNEL_SECRET = "your_secret"
LINE_CHANNEL_ACCESS_TOKEN = "your_token"

# LLM API 配置
LLM_API_KEY = "your_api_key"

# 爬蟲目標網站
TARGET_SITES = [
    {"name": "CoinDesk", "url": "https://www.coindesk.com/"},
    {"name": "CryptoNews", "url": "https://cryptonews.com/"},
    # 更多網站...
]

# 定時任務配置
CRAWL_INTERVAL = 60  # 分鐘
