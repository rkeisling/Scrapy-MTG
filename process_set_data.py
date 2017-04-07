import json
import scrapy
import pickle


def get_file_contents(filename):
    with open(filename) as fin:
        # the dicts in the big list is in the format of
        # {'set_name': <set_name as str>, 'set_num': <set_num as str>}
        return json.loads(fin.read())


def reformat_data(data):
    new_dict = {each['set_num']: each['set_name'] for each in data}
    return new_dict


def pickle_data(data):
    with open('card_sets.p', 'wb') as fin:
        pickle.dump(data, fin)


def main():
    new_data = reformat_data(get_file_contents('set_nums.json'))
    pickle_data(new_data)


if __name__ == '__main__':
    main()
