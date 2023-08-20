import os
import argparse

from src.communicator.MultiProcessComms import MultiProcessComms


def init():
    os.system("sudo hciconfig hci0 piscan")
    multiprocess_communication_process = MultiProcessComms()
    multiprocess_communication_process.start()



if __name__ == '__main__':
    init()
 