export const doPost = (e: any) => {
  // 環境変数の受け取り
  const prop = PropertiesService.getScriptProperties().getProperties()
  const CHANNEL_ACCESS_TOKEN = prop.CHANNEL_ACCESS_TOKEN

  // 応答メッセージ用のAPI URL
  const url = 'https://api.line.me/v2/bot/message/reply'

  // WebHookで受信した応答用Token
  const replyToken = JSON.parse(e.postData.contents).events[0].replyToken
  const json = JSON.parse(e.postData.contents)

  console.log(`📣: json`)
  console.log(json)

  if (json.events[0].type === 'postback') {
    UrlFetchApp.fetch(url, {
      headers: {
        'Content-Type': 'application/json; charset=UTF-8',
        Authorization: 'Bearer ' + CHANNEL_ACCESS_TOKEN,
      },
      method: 'post',
      payload: JSON.stringify({
        replyToken: replyToken,
        messages: [
          {
            type: 'text',
            text: '加湿器を消しました',
          },
        ],
      }),
    })
  }
}
