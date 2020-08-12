#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !@Time: 2020/8/12 11:45
# !@Author: Zhang-sl
import requests
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO as Bytes2Data

class SimpleImageDownloader(object):

    def __init__(self, url):
        self.url = url

    def image_download(self):
        bt = requests.get(self.url, stream=True)  # request下载图片
        return bt

    def image_read(self):
        if self.image_download().status_code == 200:
            im = Image.open(Bytes2Data(self.image_download().content))  # PIL读取图片
            return im
        else:
            return None

    def image_show(self):
        if self.image_read() is not None:
            plt.imshow(self.image_read())  # matplotlib显示图片
            plt.show()
