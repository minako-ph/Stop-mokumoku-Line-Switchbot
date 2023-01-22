import os
import requests
from dotenv import load_dotenv
import time
import hashlib
import hmac
import base64

load_dotenv()

# 環境変数を参照
OPEN_TOKEN = os.getenv('OPEN_TOKEN')
SECRET_KEY = os.getenv('SECRET_KEY')

# デバイスを取得するエンドポイント
API_BASE = 'https://api.switch-bot.com/v1.1'


def _make_sign(token: str, secret: str):
    nonce = ''
    t = int(round(time.time() * 1000))
    string_to_sign = bytes(f'{token}{t}{nonce}', 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    return sign, str(t), nonce


def _make_request_header(token: str, secret: str) -> dict:
    sign, t, nonce = _make_sign(token, secret)
    headers = {
        "Authorization": token,
        "sign": sign,
        "t": str(t),
        "nonce": nonce
    }
    return headers


def _get_request(url):
    # GETリクエストの送信
    headers = _make_request_header(OPEN_TOKEN, SECRET_KEY)
    res = requests.get(url, headers=headers)
    data = res.json()
    if data['message'] == 'success':
        return data
    return {}
