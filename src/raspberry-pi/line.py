import os
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import FlexSendMessage

load_dotenv()

# 環境変数を参照
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANELL_SECRET = os.getenv('CHANELL_SECRET')
LINE_ID = os.getenv('LINE_ID')

# LINE
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def _send_remind_message():
    payload = {
        "type": "flex",
        "altText": "加湿器を消し忘れていませんか？",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "加湿器を消し忘れていませんか？"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "加湿器を消す",
                            "data": "stop"
                        }
                    }
                ]
            }
        }
    }
    container_obj = FlexSendMessage.new_from_json_dict(payload)
    line_bot_api.push_message(LINE_ID, messages=container_obj)
