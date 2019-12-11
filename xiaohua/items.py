# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaItem(scrapy.Item):
    # 保存图片地址，名称
    # define the fields for your item here like:
    img_url = scrapy.Field()
    img_name = scrapy.Field()
