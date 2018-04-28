# -*- coding: utf-8 -*-
import scrapy


class HuizeSpider(scrapy.Spider):
    name = "huize"
    allowed_domains = ["www.huize.com"]
    start_urls = ['https://search.huize.com/p-1-%E5%A4%AA%E5%B9%B3%E6%B4%8B%E4%BF%9D%E9%99%A9-0-0-1']
    page_num=1
    def page_num_count(self):
        n=self.page_num+1
        self.page_num=n
        return n
    with open()
    def parse(self, response):
        sel = scrapy.Selector(response)
        sel2 = scrapy.Selector(response)
        # 获取当页个商品列表
        a_lists = sel.xpath('//div[@class="hz-product-item"]/div/div/h2/a/@href').extract()
        for list in a_lists:
            # print(list)  # //www.huize.com/product/detail-364.html?DProtectPlanId=10123
            new_list = "https:" + list
            # print(new_list)
            yield scrapy.Request(new_list, callback=self.parse_list, dont_filter=True)
        # 获取下一页信息
        # //*[@id="kkpager"]/div/span/a[last()]
        next_page = sel.xpath('//div[@class="layout-inner-primary"]/div[3]/div/span/a[last()-1]/text()').extract()
        # print(next_page)
        if next_page == '下一页':
            next_url = sel.xpath('//div[@class="layout-inner-primary"]/div[3]/div/span/a[last()-1]/@href').extract()
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)

        # 构造第二页
        # page_num_count
        print('*'*100)
        print(self.page_num_count())
        print('*'*100)
        next_page_url='https://search.huize.com/p-{}-%E5%A4%AA%E5%B9%B3%E6%B4%8B%E4%BF%9D%E9%99%A9-0-0-1'.format(self.page_num_count())
        yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)

    # 获取用户全部评论信息
    def parse_list(self, response):
        sel = scrapy.Selector(response)
        url_user_opinion = sel.xpath('//div[@class="user-comments"]/div/div[3]/div/div/a/@href').extract()
        url_user = "https://www.huize.com" + url_user_opinion[0]
        yield scrapy.Request(url_user, callback=self.parse_info, dont_filter=True)

    # 获取用户评论
    def parse_info(self, response):
        sel = scrapy.Selector(response)
        # 获取用户评论数据
        user_comments = sel.xpath(
            '//div[@class="detail-product-comment"]/div[3]/div/ul/li/div[@class="hz-comment-main"]/div[2]/div[1]/text()').extract()
        a = 0
        for comment in user_comments:
            a += 1
            print(str(a) + ":" + comment)

