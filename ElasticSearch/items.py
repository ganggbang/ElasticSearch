# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ElasticsearchItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = Field()
    company_address = Field()
    company_phoneNum = Field()
    company_Fax = Field()
    website = Field()
    product_service = Field()
    brands = Field()
    profile = Field()
    other_info = Field()
    logo = Field()

    pass
