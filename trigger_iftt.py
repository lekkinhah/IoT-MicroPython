import urequests

WEBHOOK_URL = 'https://maker.ifttt.com/trigger/temperature/c4Oll9kTfsIJMDHlGq6kBo'

def call_webhook():
    print('Invoking webhook')
    response = urequests.post('https://maker.ifttt.com/trigger/temperature/with/key/c4Oll9kTfsIJMDHlGq6kBo',
                              json={'value1': 'temperature'})
    print(response.status_code)
    if response is not None and response.status_code < 400:
        print('Webhook invoked')
    else:
        print('Webhook failed' )
