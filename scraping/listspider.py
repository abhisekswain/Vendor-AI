# Get list of url's for each perfume page and store in json file
import scrapy
import string
alpha_list = list(string.ascii_lowercase)
alpha_list.append('#')
urllist = []
for char in alpha_list:
    urllist.append('http://www.basenotes.net/fragrancedirectory/?i=' + char)


class PerfumeSpider(scrapy.Spider):
    name = "listspider"
    start_urls = urllist
    def parse(self, response):
        for i in response.xpath('//div[contains(@class, "frontdiv")]/div[contains(@style, "margin")]'):
            yield {
            'link' :  response.xpath('//table/tr/td/a/@href').extract()
        }
        url = response.xpath('//a[contains(@title, "Next")]/@href').extract_first()
        next_page = url
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
