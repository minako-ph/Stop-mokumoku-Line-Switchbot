
from request import _get_request

# デバイスを取得するエンドポイント
API_BASE = 'https://api.switch-bot.com/v1.1'


def get_device_list():
    # デバイス一覧の取得
    url = API_BASE + "/devices"
    result = _get_request(url)["body"]['deviceList']
    return result


def get_device_status(deviceId: str):
    # デバイス状態の取得
    url = API_BASE + "/devices/" + deviceId + "/status"
    result = _get_request(url)["body"]
    return result
