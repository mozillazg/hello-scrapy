#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Scrapy settings for imgdl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

BOT_NAME = 'imgdl'

SPIDER_MODULES = ['imgdl.spiders']
NEWSPIDER_MODULE = 'imgdl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imgdl (+http://www.yourdomain.com)'


# 抓取频率
DOWNLOAD_DELAY = 0.25      # 250 ms of delay
# 页面抓取深度
DEPTH_LIMIT = 2
# 保存结果
DOWNLOAD_HANDLERS = {
    'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
}
# http://doc.scrapy.org/en/latest/topics/images.html#enabling-your-images-pipeline
ITEM_PIPELINES = {
    # Enabling your Images Pipeline
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}
IMAGES_STORE = os.path.join(current_dir, 'images')
# 90 days of delay for image expiration
# IMAGES_EXPIRES = 90
# # 略缩图
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (270, 270),
# }
# # 最小图片
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110
