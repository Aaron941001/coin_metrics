import openai
from ..config import LLM_API_KEY

openai.api_key = LLM_API_KEY

def analyze_news(news_items):
    """使用 LLM 分析加密貨幣新聞"""
    if not news_items:
        return "無新聞可分析"

    # 構建提示
    prompt = "分析以下加密貨幣新聞，提供市場情緒摘要和可能的影響：\n\n"
    for item in news_items:
        prompt += f"- {item['title']} (來源: {item['source']})\n"

    # 呼叫 LLM API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message['content']
