import requests
import uuid


def Speech2Text(file_name, subscription_key='3c28aa450ca34f3e84403697b2c29ca1', locale='zh-CN',
                device_os='your_device_os'):
    debug = False
    url_token = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers_token = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Ocp-Apim-Subscription-Key': subscription_key}
    response_token = requests.post(url_token, headers=headers_token)
    if response_token.status_code == 200:
        token = response_token.text
    else:
        print(response_token.headers)
        print(response_token.text)
        raise Exception("Cannot get token for speech api.")
    if debug is True:
        print('Token:\t%s\n' % token)

    url_speech = 'https://speech.platform.bing.com/recognize?scenarios=websearch&appid=D4D52672-91D7-4C74-8AD8-42B1D98141A5&locale=%s&device.os=%s&version=3.0&format=json&instanceid=%s&requestid=%s' % (
        locale, device_os, uuid.uuid1(), uuid.uuid1())
    headers_speech = {
        'Content-type': 'audio/wav; codec="audio/pcm"; samplerate=16000',
        'Authorization': 'Bearer %s' % token}
    inf = open(file_name, 'rb')
    data = inf.read()
    response_speech = requests.post(url_speech, headers=headers_speech, data=data)
    if response_speech.status_code == 200:
        if debug:
            print(response_speech.json())
        response_speech = response_speech.json()
        text = response_speech['results'][0]['name']
        confidence = response_speech['results'][0]['confidence']
        return (text, confidence)
    else:
        print(response_speech.headers)
        print(response_speech.text)
        raise Exception("Speech to text error.")
    return None


if __name__ == '__main__':
    print(Speech2Text('../../../Desktop/a.wav'))
