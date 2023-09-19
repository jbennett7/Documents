#from PIL import Image
import unittest

from scanner.scanner import Scanner, Page

@unittest.skip('Skipping because nothing changed')
class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner()
        self.scanner.initialize_device()

    @unittest.skip('Skipping because nothing changed')
    def test_get_device_parameters(self):
        print(f'Testing Device parameters: {self.scanner.get_device_parameters()}')

    @unittest.skip('Skipping because nothing changed')
    def test_get_modes(self):
        print(f'Device modes: {self.scanner.get_modes()}')

    @unittest.skip('Skipping because nothing changed')
    def test_set_mode_color(self):
        self.scanner.set_mode('Color')
        print(f'Device Mode: {self.scanner.get_current_mode()}')

    @unittest.skip('Skipping because nothing changed')
    def test_set_source_duplex(self):
        self.scanner.set_source('ADF Duplex')
        self.scanner.set_mode('Color')
        print(f'Device Source: {self.scanner.get_current_source()}')
        input('DUPLEX SOURCE TEST: ' +
              'Place multiple pages in the tray and press enter to continue...')
        images = self.scanner.multi_page_scan()
        for image in images:
            image.show()

    @unittest.skip('Skipping because nothing changed')
    def test_legal_scan(self):
        input('Testing LEGAL scan, place a page in the tray...')
        self.scanner.set_page(Page.LEGAL)
        im = self.scanner.single_page_scan()
        im.show()

    @unittest.skip('Skipping because nothing changed')
    def test_letter_scan(self):
        input('Testing LETTER scan, place a page in the tray...')
        self.scanner.set_page(Page.LETTER)
        im = self.scanner.single_page_scan()
        im.show()

    @unittest.skip('Skipping because nothing changed')
    def test_single_page_scan(self):
        input('SINGLE PAGE SCAN TEST: place a page in the tray. Press Enter to continue...')
        self.scanner.set_mode('Color')
        im = self.scanner.single_page_scan()
        im.show()

    @unittest.skip('Skipping because nothing changed')
    def test_multi_page_scan(self):
        input('MULTIPLE PAGE SCAN TEST: ' +
              'Place multiple pages in the tray and press enter to continue...')
        images = self.scanner.multi_page_scan()
        for image in images:
            image.show()

if __name__ == '__main__':
    unittest.main()
