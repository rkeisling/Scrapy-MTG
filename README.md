This project uses the scrapy framework for Python.
It scrapes my inventory of Magic the Gathering cards from deckbox.org and then scrapes pricing information from mtgstocks.com (which uses TCGPlayer pricing and is updated daily).
As of 04/13/17, it stores the pricing information in JSON files. The card ids used to build urls for mtgstocks.com and the set/card information (all of it, ever; card_convert.p and card_nums_all.json are both very large files) are stored in pickled files. card_sets.p contains the set ids for mtgstocks.com.
