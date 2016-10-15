# encoding:utf-8
__author__ = 'irmo'

import socket
import sys


class Server(socket.socket):
    def __init__(self, host, port):
        super(Server, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created.')
        try:
            self.sock.bind((host, port))
        except socket.error:
            print('Bind failed.')
            self.close()
            sys.exit(0)
        self.sock.listen(5)
        print('Socket listening...')
        self.receive()

    def receive(self):
        conn, addr = self.sock.accept()
        data = conn.recv(RECV_BUFFER)
        print(data.decode('utf-8'))

    def close(self):
        self.sock.close()
        print('Socket closed.')


def main(host, port):
    server = Server(host, port)
    while True:
        try:
            server.receive()
        except KeyboardInterrupt:
            server.close()
            sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Use default argument\n\tHost: 127.0.0.1\n\tPort: 7777')
        host = '127.0.0.1'
        port = 7777
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
    RECV_BUFFER = 4096
    sys.exit(int(main(host, port) or 0))
