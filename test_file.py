import json
import pickle

def generate_needed_urls():
    all_needed_urls = []
    with open("card_convert.p", 'rb') as fin:
        card_data = pickle.load(fin)
    with open('deckbox.json') as fin:
        deckbox_data = json.loads(fin.read())

    for each in deckbox_data:
        name = each['name']
        cardset = each['cardset']
        if cardset == 'Welcome Deck 2016':
            continue
        ids = card_data[cardset][name]
        created_url = "http://www.mtgstocks.com" + ids['card_id']
        all_needed_urls.append(created_url)
    return all_needed_urls


if __name__ == '__main__':
    print(generate_needed_urls())
