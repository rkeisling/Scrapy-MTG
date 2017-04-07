import scrapy
import json
from time import sleep
from random import uniform


class MtgSpider(scrapy.Spider):
    name = "mtg_prices"
    # put all needed urls in start_urls, probably make it a comprehension
    start_urls = [
        "http://www.mtgstocks.com/cards/29470",
        "http://www.mtgstocks.com/cards/30449",
        "http://www.mtgstocks.com/cards/25999"
        ]

    def parse(self, response):
        sleep(uniform(2.5, 5))
        if response.css("td.foilprice") and response.css(
                "td.avgprice::text").extract_first() != 'N/A':
            yield {
                "cardname": response.css("div.col-md-7 h2 a::text").extract_first(),
                "cardset": response.css("div.col-md-7 h5 a::text").extract_first(),
                "nonfoil_price": response.css("td.avgprice::text").extract_first(),
                "foil_price": response.css("td.foilprice::text").extract_first()
            }
        elif not response.css("td.foilprice"):
            yield {
                "cardname": response.css("div.col-md-7 h2 a::text").extract_first(),
                "cardset": response.css("div.col-md-7 h5 a::text").extract_first(),
                "nonfoil_price": response.css("td.avgprice::text").extract_first()
            }
        else:
            yield {
                "cardname": response.css("div.col-md-7 h2 a::text").extract_first(),
                "cardset": response.css("div.col-md-7 h5 a::text").extract_first(),
                "foil_price": response.css("td.foilprice::text").extract_first()
            }
