import unittest

from simple_image_downloader import SimpleImageDownloader
class SimpleImageDownloaderTest(unittest.TestCase):
    def test_download_image(self):
        d = SimpleImageDownloader(url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
        self.assertTrue(d.image_download(),bytes)
        self.assertTrue(d.image_read(),str)

if __name__ == '__main__':
    unittest.main()