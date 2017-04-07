"""
This file processes the card data from the scraped .json file to a usable pickled dictionary.
The dictionary is in the format of {<cardset>: {<cardname>: {<cardid>: 1, <setid>: 2}}}.

Example: {
    'Shadows over Innistrad': {
        'Convicted Killer': {
            'card_id': '/cards/30711', 'set_id': '/sets/259'
            }
        }
    }
"""
import json
import scrapy
import pickle


def get_file_contents(filename):
    with open(filename) as fin:
        # the dicts in the big list is in the format of
        # {'set_name': <set_name as str>, 'set_num': <set_num as str>}
        return json.loads(fin.read())


def reformat_data(data):
    """
    Puts the disorganized data dictionary into a more suitable and usable format.
    """
    new_dict = {}
    cardname_dict = {}
    with open('card_sets.p', 'rb') as fin:
        card_sets = pickle.load(fin)
    for each in data:
        setname = card_sets[each['cardset']]
        card_id = each['card_id']
        set_id = each['cardset']
        cardname = each['cardname']
        cardname_dict[cardname] = {'card_id': card_id, 'set_id': set_id}
        new_dict[setname] = cardname_dict
        print("Added {0} to the set {1}!".format(cardname, setname))
    return new_dict


def pickle_data(data):
    with open('card_convert.p', 'wb') as fin:
        pickle.dump(data, fin)


def main():
    new_data = reformat_data(get_file_contents('card_nums_all.json'))
    pickle_data(new_data)


if __name__ == '__main__':
    main()
