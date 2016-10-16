# encoding:utf-8
__author__ = 'irmo'

import socket
import sys
from led import TrafficLight
from led_config import config_led


class Server(socket.socket):
    def __init__(self, host, port):
        super(Server, self).__init__()
        config = config_led()
        self.traffic_lightss = TrafficLight(*config)
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
        func_name = data.decode('utf-8')
        print(func_name)
        self.deal(func_name)

    def close(self):
        self.sock.close()
        print('Socket closed.')


    def deal(self, func_name):
        if func_name == 'setLightOn':
            self.traffic_lights.all_on()
        elif func_name == 'setLightOff':
            self.traffic_lights.all_off()
        elif func_name == 'setRedLight':
            self.traffic_lights.red_up()
        elif func_name == 'setGreenLight':
            self.traffic_lights.green_up()
        elif func_name == 'setYellowLight':
            self.traffic_lights.yellow()


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
