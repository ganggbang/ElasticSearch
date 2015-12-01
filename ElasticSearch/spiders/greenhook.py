# -*- coding: utf-8 -*-
#import scrapy
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ElasticSearch.items import ElasticsearchItem
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class GreenhookSpider(CrawlSpider):
    name = 'greenhook'
    allowed_domains = ['www.thegreenbook.com']
    start_urls = ['http://www.thegreenbook.com/companies/artsgate-trading-pte-ltd/']

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class=\'ID-list\']/ul/li/a')), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class=\'ComD-list\']/ul/li/a')), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class=\'ConD-list\']/ul/li/a')), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//a[@target=\"_blank\"]')), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class=\"details\"]/div/h3/a')), callback = 'parse_item_greehook'),
        Rule(SgmlLinkExtractor(restrict_xpaths = ('//div[@class=\"companyinfoWrap\"]')), callback = 'parse_item_greehook'),
        
    )

    def check_item(self, div, xpath):
        items = div.xpath(xpath).extract()
        
        if len(items) > 0:
            item = re.sub("\s{2,}","", items[0])
            return item
        else:

            return ''

    def parse_item_greehook(self, response):
        sel = Selector(response)
        
        div = sel.xpath('//div[@class=\"companyinfoWrap\"]')
        
        #company_name = re.sub("\s{2,}","", div.xpath('h2/text()').extract()[0])
        company_name = self.check_item(div, 'h2/text()')
        #self.check_item(re.sub("\s{2,}","", div.xpath('span[@itemprop=\'CompanyAddress\']/text()').extract()))
        company_address = self.check_item(div, 'span[@itemprop=\'CompanyAddress\']/text()')
        #self.check_item(re.sub("\s{2,}","", div.xpath('div/div/span[@id=\'rptCompanyDetails_2_ctl00_pnlTel\']/a/span[@class=\'phoneNum\']/text()').extract()))
        company_phoneNum = self.check_item(div, 'div/div/span[@id=\'rptCompanyDetails_2_ctl00_pnlTel\']/a/span[@class=\'phoneNum\']/text()')
        #self.check_item(re.sub("\s{2,}","", div.xpath('div/div/span[@id=\'rptCompanyDetails_2_ctl00_pnlFax\']/a/span[@class=\'faxNum\']/text()').extract()))
        company_Fax = self.check_item(div,'div/div/span[@id=\'rptCompanyDetails_2_ctl00_pnlFax\']/a/span[@class=\'faxNum\']/text()')
        website = self.check_item(div,'//a[@class=\'website\']/@href')
        #website = div.xpath('//a[@class=\'website\']/@href').extract()
        
        print company_name
        print company_address
        print company_phoneNum
        print company_Fax
        print website

        return 
