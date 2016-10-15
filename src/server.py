#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import socket
import sys


def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket Bound")
    s.listen(5)
    print("Listening for connections...")
    conn, addr = s.accept()
    data = input("Enter data to be sent: ")
    print(type(data))
    conn.send(data.encode('utf-8'))


def main():
    host = "127.0.0.1"
    port = 7779
    connect(host, port)


if __name__ == '__main__':
    sys.exit(int(main() or 0))
