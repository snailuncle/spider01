# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuizeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    product_url = scrapy.Field()
    user_opinion = scrapy.Field()
    comment = scrapy.Field()