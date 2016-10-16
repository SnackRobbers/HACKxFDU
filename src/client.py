# encoding:utf-8
__author__ = 'irmo'

import socket
import sys


def connect(host, port, msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("socket connected!!!")
    # text = input('Input the message to send: ')
    text = msg
    sock.send(text.encode('utf-8'))
    sock.close()


def main(host, port, msg):
    connect(host, port, msg)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Use default argument\n\tHost: 127.0.0.1\n\tPort: 7777')
        host = '127.0.0.1'
        port = 7777
        msg = 'SampleFunc'
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        msg = sys.argv[3]
    sys.exit(int(main(host, port, msg) or 0))
