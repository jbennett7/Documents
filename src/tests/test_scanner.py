from scanner import Scanner
import unittest

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner()
        self.scanner.initialize_device()

    def test_get_device_parameters(self):
        print(f'Testing Device parameters: {self.scanner.get_device_parameters()}')

    def test_get_options(self):
        options = self.scanner.get_options()
        print('Testing Device Options:')
        for option in options[0:5]:
            print(f'\t{option}')

    def test_single_page_scan(self):
        input("Please Place a test page in the tray and then press enter to continue...")
        self.scanner.single_page_scan()

    def test_multi_page_scan(self):
        input("Place multiple pages in the tray and press enter to continue...")
        self.scanner.multi_page_scan()

if __name__ == '__main__':
    unittest.main()
