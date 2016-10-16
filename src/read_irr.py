import os, sys, select, subprocess
from relay import RelayLED


class IrrReader:
    def __init__(self):
        pass

    def read_irr():
        args = ['mode2', '-d', '/dev/lirc0']
        p1 = subprocess.Popen(args, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(args, stdout=subprocess.PIPE)

        space_list = []
        pulse_list = []
        led = RelayLED()
        try:
            while True:
                rlist, wlist, xlist = select.select([p1.stdout, p2.stdout], [], [])
                for stdout in rlist:
                    output = os.read(stdout.fileno(), 1024).decode('utf-8')

                    if output:
                        # sys.stdout.write(output)
                        # sys.stdout.write('indicator: ' + output)
                        o = output.split()
                        if len(o) == 4:
                            for wave, length in zip(o[::2], o[1::2]):
                                if wave == 'space':
                                    space_list.append(int(length))
                                elif wave == 'pulse':
                                    pulse_list.append(int(length))

                            if len(space_list) == 36 and len(pulse_list) == 36:
                                led.toggle()

        except KeyboardInterrupt:
            print('Exist Now....')
            sys.exit(0)

if __name__ == '__main__':
    reader = IrrReader()
    IrrReader.read_irr()