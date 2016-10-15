# -*- coding: utf-8 -*-
import requests
import sys


def callAPI(text):
    url = 'https://api.projectoxford.ai/luis/v1/application' + \
          '?id=bd9d9b8f-ac87-4bc9-94de-f3aeb734ead6&subscription-key=86ef114a9ce94ca9a56bda305d09b1b4'
    request_url = url + '&q=' + text
    r = requests.get(request_url)
    if r.status_code != 200:
        raise ConnectionError
    getFunc(r.json())


def getFunc(j):
    priority_func = j['intents'][0]
    func = priority_func['intent']
    score = priority_func['score']
    print(func, '(', score, ')')


def main():
    text = input('Please input a sentence in Chinese: ')
    callAPI(text)


if __name__ == '__main__':
    sys.exit(int(main() or 0))
