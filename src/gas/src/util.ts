const prop = PropertiesService.getScriptProperties().getProperties()
const OPEN_TOKEN = prop.OPEN_TOKEN
const SECRET_KEY = prop.SECRET_KEY

export const getAuthParams = () => {
  const t = Date.now().toString()
  const nonce = Utilities.getUuid()
  const data = OPEN_TOKEN + t + nonce
  const sign = Utilities.base64Encode(
    Utilities.computeHmacSha256Signature(data, SECRET_KEY)
  ).toUpperCase()

  return { t, nonce, sign }
}

export const switchBotTurnOffReq = (deviceId: string) => {
  const { t, nonce, sign } = getAuthParams()

  const headers = {
    Authorization: OPEN_TOKEN,
    sign: sign,
    nonce: nonce,
    t: t,
    'Content-Type': 'application/json; charset=utf8',
  }

  const body = JSON.stringify({
    command: 'turnOff',
    parameter: 'default',
    commandType: 'command',
  })

  const options = {
    method: 'post',
    headers: headers,
    muteHttpExceptions: true,
    payload: body,
  } as any

  const resp = UrlFetchApp.fetch(
    `https://api.switch-bot.com/v1.1/devices/${deviceId}/commands`,
    options
  )
  console.log(resp.getContentText())
}
