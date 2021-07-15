#介绍scrapy 爬虫框架
#环境：  需要安装visual studio     lxml scrapy
'''
bench  不依赖项目爬取一个网页 
scrapy bench    查看电脑性能 每分钟爬取多少网页
scrapy view http://www.baidu.com   下载网页，并用浏览器打开
-------------------------------------------------------------
创建项目：
1.scrapy startproject first   创建一个名字为first的爬虫模板
2.scrapy genspider -l    查看模板下有哪些项目
3.scrapy genspider -t basic test baidu.com    创建爬虫项目(要在模板文件夹下执行)
4.scrapy crawl test --nolog  直接运行爬虫
5.scrapy list    展示项目下可以使用的爬虫文件

基本爬虫：
1.修改setting.py  改为ROBOTSTXT_OBEY = False
2.修改setting.py   去掉注释  改为FirstPipeline
            # Configure item pipelines
            # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
            ITEM_PIPELINES = {
                'first.pipelines.FirstPipeline': 300,
            }
3.item.py 下 content = scrapy.Field()#存储内容   创建容器
4.test.py    from first.items import FirstItem
       下创建规则
        item=FirstItem()
        item["content"] = response.xpath("/html/head/title/text()").extract()
        yield item
5.pipelines.py 输出结果 
        class FirstPipeline(object):
            def process_item(self, item, spider):
                print(item["content"])
                return item
---------------------------------------------------------------
自动爬虫创建项目（自动一层一层爬）：
1.scrapy startproject qsauto   创建一个名字为first的爬虫模板
2.cd qsauto
3.scrapy genspider -t crawl qsbk qiushibaike.com    创建自动爬虫项目

修改：
1.setting.py  USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'   设置模拟浏览器
2.qsbk.py
    # -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from qsauto.items import QsautoItem

class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    #start_urls = ['https://www.qiushibaike.com/text/']

    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )
    def start_requests(self):
        ua = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
        yield Request('https://www.qiushibaike.com/text/',headers=ua)
        #return super().start_requests()  
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i["content"] = response.xpath("//meta[@name='description']/@content").extract()
        print(i["content"])
        return i
---------------------------------------------------------------------------------------------------
自动爬虫创建项目（通过For循环）：
scrapy startproject qsauto1
cd qsauto1
scrapy genspider -t basic tszn hellobi.com


'''
from scrapy.spider import Spider


class CHelper_scrapy(object):
    def __init__(self): 
        pass 
    def test(self):

        return "null"
