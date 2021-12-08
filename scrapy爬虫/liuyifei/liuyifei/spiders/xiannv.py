
import scrapy
from liuyifei.items import LiuyifeiItem #从项目文件的.items文件中继承类
from scrapy.selector import Selector #这应该是一个选择器

class XiannvSpider(scrapy.Spider):#继承scrapy.Spider类
    name = 'xiannv'
    allowed_domains = ['zhihu.com']
    start_urls = [u'https://www.zhihu.com/search?type=content&q=刘亦菲']

    def parse(self, response):#response就是网页数据HTML
        selector = Selector(response)
        item = LiuyifeiItem
        articles = selector.xpath('//span[@class="Highlight"]') #从HTML文件中找到要的信息
        for article in articles:
            miaoshu = article.extract()
            item['miaoshu'] = miaoshu
            yield item
        #pass
