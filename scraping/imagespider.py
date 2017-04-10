# Spider to extract image and text information from basenotes.com

from perfumes.items import PerfumesItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import json

# Get list of urls from url_list.json file

with open('/Users/abhisekswain/Desktop/Kojak/perfumes/perfumes/url_list.json') as json_data:
    d = json.load(json_data)
    links = []
    for i in d:
        print len(i['link'])
        for j in i['link']:
            links.append(j)

# Spider class

class ImageSpider(scrapy.Spider):
    name = "imagespider"
    start_urls = links
    def parse(self, response):
        yield {'image_urls' : response.xpath('//div[@class = "fraginfoimage"]/img/@src').extract(),
            'name' : response.xpath('//div/h1/span[1]/text()').extract(),
            'year' : response.xpath('//div[contains(@class,"dirleft50")]//td/a/text()').extract()[0],
            'house' : response.xpath('//div[contains(@class,"dirleft50")]//td/a/text()').extract()[1],
            'gender' : response.xpath('//div[contains(@class,"dirleft50")]//td[3]/text()').extract(),
            'availability' : response.xpath('//div[contains(@class,"dirleft50")]//td[2]/text()').extract(),
            'about' : response.xpath('//div[contains(@class, "dirright50")]/div[@class = "diraboutblurb"]/text()').extract(),
            'topnotes' : response.xpath('//div[contains(@class, "notespyramid")]/ol/li[1]/div/ul/li/a/text()').extract(),
            'heartnotes' : response.xpath('//div[contains(@class, "notespyramid")]/ol/li[2]/div/ul/li/a/text()').extract(),
            'basenotes' : response.xpath('//div[contains(@class, "notespyramid")]/ol/li[3]/div/ul/li/a/text()').extract()
        }
