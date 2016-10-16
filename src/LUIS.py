# -*- coding: utf-8 -*-
import requests
import sys


def callAPI(text):
    url = 'https://api.projectoxford.ai/luis/v1/application?id=a481ff0e-5d45-4921-b795-baf228922911&subscription-key=86ef114a9ce94ca9a56bda305d09b1b4'
    request_url = url + '&q=' + text
    r = requests.get(request_url)
    if r.status_code != 200:
        raise ConnectionError
    return getFunc(r.json())


def getFunc(j):
    priority_func = j['intents'][0]
    func = priority_func['intent']
    score = priority_func['score']
    if score < 0.3:
        print('Score is low.')
    return str(func)


def main():
    text = input('Please input a sentence in Chinese: ')
    callAPI(text)


if __name__ == '__main__':
    sys.exit(int(main() or 0))
