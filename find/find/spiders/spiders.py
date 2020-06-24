import scrapy
import re
import random


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"]

    def start_requests(self):
        ua = random.choice(self.user_agent_list)
        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Referer': 'https://gupiao.baidu.com/',
            'User-Agent': ua
        }
        urls = [
            'http://quote.eastmoney.com/center/gridlist.html#hs_a_board',
            # 'http://www.baidu.com',
            # 'https://xueqiu.com/hq',
            # 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board',
            # 'https://blog.csdn.net/xiaosa_kun/article/details/84868449',
            # 'http://www.xinhuanet.com/politics/leaders/2020-06/07/c_1126083999.htm',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.xpath('//div[@class="listDiv"]//table//thead//tr//th/text()'))
        # print(response.xpath('// *[ @ id = "listTable1"] / tbody / tr[2] / td[1]'))
        print('----------')
        # print(response.xpath('//*[@id="table_wrapper-table"]/tbody/tr[1]/td[3]/a/text()'))
        print(response.xpath('//*[@id="table_wrapper-table"]/tbody/tr[1]/td[2]/a/text()').extract()[0])

        # print(response.xpath('/html/body/div[4]/div[2]/div[5]/div/div[2]/div/div[1]/p[1]/text()'))

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
