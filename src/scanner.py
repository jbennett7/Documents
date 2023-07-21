import sane
import numpy
from PIL import Image
from enum import Enum

class NoDeviceFoundError(Exception):
    pass

class ModeError(Exception):
    pass

class Scanner(object):
    def __init__(self):
        self.sane_version = sane.init()
        # Use the id of the option as the key
        self.__key = lambda x: x[0]

    def initialize_device(self) -> None:
        """initialize_device() -> None"""
        device = sane.get_devices()
        if device:
            self.__dev = sane.open(device[0][0])
        else:
            raise NoDeviceFoundError

    def get_device_parameters(self) -> tuple[str, int, tuple[int, int], int, int]:
        """get_device_parameters() -> tuple[str, int, tuple[int, int], int, int]"""
        self.__params = self.__dev.get_parameters()
        return self.__params

#    def get_options(self) -> list[tuple[int, str, str, str, str, bytes, str, str]]:
#        """get_options() -> list[tuple[int, str, str, str, str, bytes, str, str]]
#
#        SANE Device Options:
#        (id: int, name: str, title: str, desc: str, unit: str,
#         size: bytes, cap: str, constraint: str)"""
#        self.__device_options = {}
#        options = self.__dev.get_options()
#        return(options)

    def get_modes(self) -> list[str]:
        """get_modes() -> list[str]"""
        return self.__dev['mode'].constraint

    def set_mode(self, new_mode: str) -> None:
        """set_mode() -> bool"""
        if new_mode not in self.get_modes():
            raise ModeError
        self.__dev.mode = new_mode

    def get_current_mode(self) -> str:
        """get_current_mode() -> str"""
        return self.__dev.mode

    def single_page_scan(self) -> Image:
        """single_page_scan() -> Image"""
        im = self.__dev.scan()
        return im

    def multi_page_scan(self) -> list[Image]:
        """multi_page_scan() -> list[Image]"""
        images = []
        for i, pageim in enumerate(self.__dev.multi_scan()):
            images.append(pageim)
        return images

    def __del__(self):
        try:
            self.__dev.close()
        except AttributeError:
            pass

