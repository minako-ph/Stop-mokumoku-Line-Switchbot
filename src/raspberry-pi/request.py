import requests


def _get_request(url, headers):
    # GETリクエストの送信
    res = requests.get(url, headers=headers)
    data = res.json()
    return data


def _post_request(url, headers, payload):
    # POSTリクエストの送信
    res = requests.post(url, headers=headers, params=payload)
    data = res.json()
    return data
