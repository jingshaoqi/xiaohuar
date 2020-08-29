# -*- coding: utf-8 -*-
'''
程序运行说明
在xiaohua目录下运行
scrapy crawl xiaohuar
再spiders目录下运行
scrapy runspider xiaohuar.py
会成功
稍后来改正在pycharm下也能运行
'''
import scrapy
from urllib import parse
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
            img_src = li.xpath('.//img/@src').extract_first() # 获取相对路径
            img_url = parse.urljoin(response.url, img_src) # 拼接成完整的url路径
            img_name = li.xpath('.//img/@alt').extract_first() + '.jpg'
            item = XiaohuaItem() # 实例化对象
            # 将数据封装到item中，这里只能用['img_ur']的形式，不能用点的方式
            item['img_url'] = img_url
            item['img_name'] = img_name
            yield item

        # 拼接页码，并递归调用自己，达到处理所有页码的目的
        # 这里修改为是否能获取到下一页
        next_page = response.xpath('//div[@id="content"]//div[@class="listpage"]//ol//li//a[contains(string(), "下一页")]')
        # print(next_page)
        if next_page is not None:
            next_href = next_page.xpath('.//@href').get() # 获取相对路径
            next_page_url = parse.urljoin(response.url, next_href) # 拼接成完整的url路径
            print(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            print('emptydddddddddddd')
