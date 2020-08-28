# -*- coding: utf-8 -*-
'''
程序运行说明
在xiaohua目录下运行
scrapy crawl xiaohua
会失败
而再spiders目录下运行
scrapy runspider xiaohuar.py
则会成功
稍后来改正在pycharm下也能运行
'''
import scrapy
from xiaohua.items import XiaohuaItem


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    start_urls = ['http://www.521609.com/gaozhongxiaohua/']
    base_url = 'http://www.521609.com'
    urls = 'http://www.521609.com/gaozhongxiaohua/list5%d.html'

    def parse(self, response):

        # 获取到包含图片的li列表
        li_list = response.xpath('//*[@id="content"]//div[@class="index_img list_center"]/ul/li')
        for li in li_list:
            # 匹配图片的地址,图片名称
            img_url = self.base_url + li.xpath('.//img/@src').extract_first()
            img_name = li.xpath('.//img/@alt').extract_first() + '.jpg'
            item = XiaohuaItem() # 实例化对象
            # 将数据封装到item中，这里只能用['img_ur']的形式，不能用点的方式
            item['img_url'] = img_url
            item['img_name'] = img_name
            yield item

        # 拼接页码，并递归调用自己，达到处理所有页码的目的
        for i in range(1, 12):
            new_url = self.urls % i
            yield scrapy.Request(url=new_url, callback=self.parse)