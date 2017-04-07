import scrapy
import json
from time import sleep
from random import uniform


class MtgSpider(scrapy.Spider):
    name = "deckbox"
    start_urls = [
        "https://deckbox.org/sets/1029760?p=1"
        ]
    def parse(self, response):
        all_trs = response.css('table.set_cards tr')
        sleep(uniform(2.5, 5))
        for tr in all_trs:
            if tr.css("td a.simple::text").extract_first() != None:
                name = tr.css("td a.simple::text").extract_first()
                inv_count = tr.css("td.inventory_count::text").extract_first()
                cardset = tr.css("div.mtg_edition_container img::attr(data-title)").extract_first().split('(')[0].strip()
                if tr.css("td.minimum_width img.s_colors::attr(data-title)").extract_first() == "Foil":
                    foil = True
                else:
                    foil = False
                yield {
                    "name": name,
                    "cardset": cardset,
                    "foil": foil,
                    "inv_count": int(inv_count)
                }
        next_page = response.xpath('//a[contains(., "Next")]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
