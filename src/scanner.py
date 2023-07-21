import sane
import numpy
from PIL import Image

class NoDeviceFoundError(Exception):
    pass

class Scanner(object):
    def __init__(self):
        self.sane_version = sane.init()
        self.__initialize_device()

    def __initialize_device(self):
        device = sane.get_devices()
        if device:
            self.__dev = sane.open(device)
        else:
            raise NoDeviceFoundError

    def __del__(self):
        try:
            self.__dev.close()
        except AttributeError:
            pass

