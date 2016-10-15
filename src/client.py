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


def main(host, port):
    connect(host, port)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('Use default argument\n\tHost: 127.0.0.1\n\tPort: 7777')
        host = '127.0.0.1'
        port = 7777
    else:
        host = sys.argv[2]
        port = int(sys.argv[3])
    sys.exit(int(main(host, port) or 0))
