#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import socket
import sys


def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("socket connected!!!")
    msg = s.recv(1024)
    print("Message from server : " + str(msg))


def main():
    host = "127.0.0.1"
    port = 7779
    connect(host, port)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
