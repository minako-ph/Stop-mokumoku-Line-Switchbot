import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# 環境変数を参照
OPEN_TOKEN = os.getenv('OPEN_TOKEN')

API_HOST = 'https://api.switch-bot.com'

# デバイスを取得するエンドポイント
DEBIVELIST_URL = f"{API_HOST}/v1.0/devices"

# リクエスト情報
HEADERS = {
    'Authorization': OPEN_TOKEN,
    'Content-Type': 'application/json; charset=utf8'
}


def _get_request(url):
    # GETリクエストの送信
    res = requests.get(url, headers=HEADERS)
    data = res.json()
    if data['message'] == 'success':
        return data
    return {}


def _post_request(url, params):
    # POSTリクエストの送信
    res = requests.post(url, data=json.dumps(params), headers=HEADERS)
    data = res.json()
    if data['message'] == 'success':
        return res.json()
    return {}


def get_device_list():
    # デバイス一覧の取得
    try:
        result = _get_request(DEBIVELIST_URL)["body"]
        return result
    except:
        return


def get_virtual_device_list():
    # デバイス一覧の取得
    devices = get_device_list()
    result = devices['deviceList']
    return result


# def send_air_condition(deviceId, temperature, mode, fanspeed, power_state):
#     url = f"{API_HOST}/v1.0/devices/{deviceId}/commands"
#     params = {
#         "command": "setAll",
#         "parameter": f"{temperature},{mode},{fanspeed},{power_state}",
#         "commandType": "command"
#     }
#     res = _post_request(url, params)
#     if res['message'] == 'success':
#         return res
#     return {}

def main():
    data = get_virtual_device_list()
    for device in data:
        if device['deviceName'] == 'プラグ＜加湿器＞':
            print(device)
            break


main()
