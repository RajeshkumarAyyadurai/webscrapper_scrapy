# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KupatanaItem(scrapy.Item):
    # define the fields for your item here like:
    CATEGORY = scrapy.Field()
    PHONENUMBER = scrapy.Field()
    HYPERLINK = scrapy.Field()
