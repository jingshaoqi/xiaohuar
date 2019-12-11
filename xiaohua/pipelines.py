# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class XiaohuaPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 将item中存储的图片地址进行get请求发送
        url = item['img_url']
        file_name = item['img_name']
        yield Request(url, meta={'filename': file_name})

    def file_path(self, request, response=None, info=None):
        # 返回文件路径 在settings中指定 IMAGES_STORE = './imgs'
        filename = request.meta['filename']
        return filename

    def item_complete(self, request,item, info):
        # 返回item交给后续的处理
        return item
