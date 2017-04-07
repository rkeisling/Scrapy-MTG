import scrapy


class MtgSpider(scrapy.Spider):
    name = "mtg_sets"
    start_urls = [
        'http://www.mtgstocks.com/sets'
    ]

    def parse(self, response):
        for each_set in response.css('li.list'):
            yield {
                "set_num": each_set.css('a::attr(href)').extract_first(),
                "set_name": each_set.css('a::text').extract_first()
            }
