import scrapy
import json
from time import sleep
from random import uniform


def get_set_conversions(filename):
    with open(filename) as fin:
        # the dicts in the big list is in the format of
        # {'set_name': <set_name as str>, 'set_num': <set_num as str>}
        return json.loads(fin.read())

class MtgSpider(scrapy.Spider):
    name = "mtg_cards"
    start_urls = [
        "http://www.mtgstocks.com" + each[
            'set_num'] for each in get_set_conversions(
                'set_nums.json')]

    def parse(self, response):
        sleep(uniform(2.5, 5))
        for card in response.css("td a.screenshot"):
            yield {
                "cardset": response.url[24:],
                "cardname": card.css('a::text').extract_first(),
                "card_id": card.css('a::attr(href)').extract_first()
            }


