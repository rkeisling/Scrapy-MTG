import scrapy


class MtgSpider(scrapy.Spider):
    name = "mtg_sets"
    start_urls = [
        'http://www.starcitygames.com/cardsets/english_singles'
    ]

    def parse(self, response):
        for each_set in response.css('#english_list > div > ul > li'):
            yield {
                "set_link": each_set.css('a::attr(href)').extract_first(),
                "set_name": each_set.css('a::text').extract_first()
            }
