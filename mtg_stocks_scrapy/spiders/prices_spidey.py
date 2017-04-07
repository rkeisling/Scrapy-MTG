import scrapy
import json
import pickle
from time import sleep
from random import uniform

def generate_needed_urls():
    all_needed_urls = []
    with open("card_convert.p", 'rb') as fin:
        card_data = pickle.load(fin)
    with open('deckbox.json') as fin:
        deckbox_data = json.loads(fin)

    for each in deckbox_data:
        name = each['name']
        cardset = each['cardset']
        ids = card_data[cardset][name]
        created_url = "http://www.mtgstocks.com" + ids['card_id']
        all_needed_urls.append(created_url)
    return all_needed_urls


class MtgSpider(scrapy.Spider):
    name = "mtg_prices"
    # put all needed urls in start_urls, probably make it a comprehension
    start_urls = generate_needed_urls()

    def parse(self, response):
        sleep(uniform(2.5, 5))
        if response.css("td.foilprice") and response.css("td.avgprice::text").extract_first(
        ) != 'N/A':
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
