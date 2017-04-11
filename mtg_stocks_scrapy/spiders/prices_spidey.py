import json
import pickle
from time import sleep
from random import uniform
import scrapy


def generate_needed_urls():
    """
    Makes all urls using deckbox information along with all card information (from MTGStocks).
    """
    all_needed_urls = []
    with open("card_convert.p", 'rb') as fin:
        card_data = pickle.load(fin)
    with open('deckbox.json') as fin:
        deckbox_data = json.loads(fin.read())

    for each in deckbox_data:
        name = each['name']
        cardset = each['cardset']
        try:
            set_dict = card_data[cardset]
        except KeyError:
            try:
                set_dict = card_data[fix_set_transitions(cardset)]
            except KeyError:
                continue
        try:
            card_dict = set_dict[name]
        except KeyError:
            try:
                card_dict = set_dict[fix_card_transitions(name)]
            except KeyError:
                continue
        created_url = "http://www.mtgstocks.com" + card_dict['card_id']
        all_needed_urls.append(created_url)
    return all_needed_urls


def fix_set_transitions(cardset):
    """
    Changes the set to the MTGStocks variant (which in some cases there isn't one).
    """
    set_transfer_dict = {'Welcome Deck 2016': None}
    if 'Core Set' in cardset:
        cardset = '{0} ({1}{2})'.format(cardset[:10], cardset[0], cardset[8:10])
    else:
        cardset = set_transfer_dict[cardset]
    return cardset


def fix_card_transitions(name):
    """
    Changes some minor card spelling to the MTGStocks variant.
    """
    card_transfer_dict = {'Aetherspouts': 'AEtherspouts',
                          'Aether Adept': 'AEther Adept',
                          'Aether Gale': 'AEther Gale',
                          'Aether Searcher': 'AEther Searcher',
                          'Aether Vial': 'AEther Vial',
                          'Aetherling': 'AEtherling',
                          'Aethertow': 'AEthertow',
                          'Scornful Aether-Lich': 'Scornful AEther-Lich',
                          'Unravel the Aether': 'Unravel the AEther',
                          'Yet Another Aether Vortex': 'Yet Another AEther Vortex',
                          'Forest': None,
                          'Swamp': None,
                          'Mountain': None,
                          'Plains': None,
                          'Island': None}
    return card_transfer_dict[name]


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
