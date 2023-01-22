import os
from dotenv import load_dotenv
from request import _post_request

load_dotenv()

# 環境変数を参照
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANELL_SECRET = os.getenv('CHANELL_SECRET')
LINE_ID = os.getenv('LINE_ID')


def _send_remind_message():
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }
    payload = {
        'to': LINE_ID,
        "messages": [
            {
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
        ]
    }
    res = _post_request(url, headers, payload)
    print(res)
