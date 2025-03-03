import requests
from bs4 import BeautifulSoup

def crawl_coindesk():
    """爬取 CoinDesk 網站的加密貨幣新聞"""
    url = "https://www.coindesk.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    # 根據網站結構解析新聞
    articles = soup.select('.article-card')
    for article in articles:
        title = article.select_one('.headline').text.strip()
        link = article.select_one('a')['href']
        news_items.append({
            "title": title,
            "link": link,
            "source": "CoinDesk"
        })

    return news_items
