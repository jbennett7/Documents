import sane
import numpy
from PIL import Image
from enum import Enum

class NoDeviceFoundError(Exception):
    pass

class ModeError(Exception):
    pass

class SourceError(Exception):
    pass

class Page(Enum):
    LEGAL = 355
    LETTER = 280

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

    def get_sources(self) -> list[str]:
        """get_sources() -> list[str]"""
        return self.__dev['source'].constraint

    def set_source(self, new_source: str) -> None:
        """set_source(new_source: str) -> None"""
        if new_source not in self.get_sources():
            raise SourceError
        self.__dev.source = new_source

    def get_current_source(self) -> str:
        """get_current_source -> str"""
        return self.__dev.source

    def get_modes(self) -> list[str]:
        """get_modes() -> list[str]"""
        return self.__dev['mode'].constraint

    def set_mode(self, new_mode: str) -> None:
        """set_mode() -> bool"""
        if new_mode not in self.get_modes():
            raise ModeError
        self.__dev.mode = new_mode

    def set_page(self, page_size: Page) -> str:
        """set_page_legal(self) -> str"""
        self.__dev.page_height = page_size.value

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

