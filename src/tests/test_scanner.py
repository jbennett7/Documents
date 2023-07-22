from scanner import Scanner
#from PIL import Image
import unittest

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
        for i, image in enumerate(images):
            image.save('/tmp/duplex_test-'+str(i)+'.png')

    @unittest.skip('Skipping because nothing changed')
    def test_single_page_scan(self):
        input('SINGLE PAGE SCAN TEST: place a page in the tray. Press Enter to continue...')
        self.scanner.set_mode('Color')
        im = self.scanner.single_page_scan()
        im.save('/tmp/single_test.png')

    @unittest.skip('Skipping because nothing changed')
    def test_multi_page_scan(self):
        input('MULTIPLE PAGE SCAN TEST: ' +
              'Place multiple pages in the tray and press enter to continue...')
        images = self.scanner.multi_page_scan()
        for i,image in enumerate(images):
            image.save('/tmp/multi_test-'+str(i)+'.png')

if __name__ == '__main__':
    unittest.main()
