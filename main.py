import os
import requests
import json
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


def make_sign(token: str, secret: str):
    nonce = ''
    t = int(round(time.time() * 1000))
    string_to_sign = bytes(f'{token}{t}{nonce}', 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    return sign, str(t), nonce


def make_request_header(token: str, secret: str) -> dict:
    sign, t, nonce = make_sign(token, secret)
    headers = {
        "Authorization": token,
        "sign": sign,
        "t": str(t),
        "nonce": nonce
    }
    return headers


def _get_request(url):
    # GETリクエストの送信
    headers = make_request_header(OPEN_TOKEN, SECRET_KEY)
    res = requests.get(url, headers=headers)
    data = res.json()
    if data['message'] == 'success':
        return data
    return {}


def _post_request(url, params):
    # POSTリクエストの送信
    headers = make_request_header(OPEN_TOKEN, SECRET_KEY)
    res = requests.post(url, data=json.dumps(params), headers=headers)
    data = res.json()
    if data['message'] == 'success':
        return res.json()
    return {}


def get_device_list():
    # デバイス一覧の取得
    try:
        url = API_BASE + "/devices"
        result = _get_request(url)["body"]['deviceList']
        return result
    except:
        return


def get_device_status(deviceId: str):
    # デバイス状態の取得
    try:
        url = API_BASE + "/devices/" + deviceId + "/status"
        result = _get_request(url)["body"]
        return result
    except:
        return


def main():
    # デバイス一覧の取得
    list = get_device_list()
    print(list)

    # 各デバイスのIDを取得
    kashitsukiId = ''
    airconId = ''
    for device in list:
        if device['deviceName'] == 'プラグミニ.加湿器':
            kashitsukiId = device['deviceId']
        if device['deviceName'] == 'プラグミニ.エアコン':
            airconId = device['deviceId']

    # 加湿器の電流を確認
    if (kashitsukiId != ''):
        print(airconStatus)
        kashitsukiStatus = get_device_status(kashitsukiId)
        # 加湿器に電流がながれていればエアコンの電流を確認
        if (kashitsukiStatus['electricCurrent'] > 0):
            airconStatus = get_device_status(airconId)
            print(airconStatus)
            if (airconStatus['electricCurrent'] == 0):
                # リマインド実行


main()
