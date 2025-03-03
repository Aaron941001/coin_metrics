from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from ..config import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

def send_analysis_to_users(user_ids, analysis):
    """發送分析結果給 Line 用戶"""
    for user_id in user_ids:
        line_bot_api.push_message(
            user_id,
            TextSendMessage(text=analysis)
        )
