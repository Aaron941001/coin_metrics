from apscheduler.schedulers.background import BackgroundScheduler
from ..crawlers.sites import coindesk
from ..analysis.processors import analyze_news
from ..bot.handlers import send_analysis_to_users
from ..config import CRAWL_INTERVAL

scheduler = BackgroundScheduler()

def crawl_and_analyze_job(user_ids):
    """爬蟲和分析的定時任務"""
    # 爬取新聞
    news_items = coindesk.crawl_coindesk()

    # 分析新聞
    analysis = analyze_news(news_items)

    # 發送結果
    send_analysis_to_users(user_ids, analysis)

def start_scheduler(user_ids):
    """啟動排程器"""
    job = scheduler.add_job(
        crawl_and_analyze_job,
        'interval',
        minutes=CRAWL_INTERVAL,
        args=[user_ids]
    )
    scheduler.start()
    return job
