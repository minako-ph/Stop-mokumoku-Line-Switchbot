import requests


def _get_request(url, headers):
    # GETリクエストの送信
    res = requests.get(url, headers=headers)
    data = res.json()
    return data
