import os
from dotenv import load_dotenv
from line import _send_remind_message
from switchbot import get_device_status, get_device_list

load_dotenv()

# 環境変数を参照
WIFI_ADDRESS = os.getenv('WIFI_ADDRESS')

# ------------
# メイン処理
# ------------

# 自身の端末のwifi接続状況を確認
stream = os.popen(f'arp -a | grep {WIFI_ADDRESS}')
wifitRes = stream.read()
wifiResLength = len(wifitRes)

# wifiに自身の端末が接続されていなければ処理実行
if wifiResLength == 0:

    # デバイス一覧の取得
    list = get_device_list()

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
        kashitsukiStatus = get_device_status(kashitsukiId)
        print(kashitsukiStatus)
        # 加湿器に電流がながれていればエアコンの電流を確認
        if (kashitsukiStatus['electricCurrent'] > 0):
            airconStatus = get_device_status(airconId)
            print(airconStatus)
            # エアコンに電流が流れていなければ
            # if (airconStatus['electricCurrent'] == 0):
            if (airconStatus['electricCurrent'] > 0):
                # リマインド実行
                _send_remind_message()
