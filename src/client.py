#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import socket
import sys


def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("socket connected!!!")
    text = input('Input the message to send: ')
    sock.send(text.encode('utf-8'))
    sock.close()


def main():
    host = "127.0.0.1"
    port = 7777
    connect(host, port)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
