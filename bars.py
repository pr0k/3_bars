import json
import argparse


class MyArgParcer(argparse.ArgumentParser):
    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self.description = (
            '|Find out and output the smallest bar'
            'the biggest bar and the nearest bar|'
        )
        self.add_argument(
            '-v',
            '--verbosity',
            help='increase output verbosity',
            action='store_true',
        )
        self.add_argument(
            'bars_json',
            help='the path to the data file in json format about bars',
        )
        self.add_argument('longitude', help='float number', type=float)
        self.add_argument('latitude', help='float number', type=float)


def load_data(filepath):
    with open(filepath, 'r') as json_data_file:
        return json.load(json_data_file)


def get_biggest_bar(bars_list):
    return max(
        bars_list,
        key=lambda item: item['properties']['Attributes']['SeatsCount'],
    )


def get_smallest_bar(bars_list):
    return min(
        bars_list,
        key=lambda item: item['properties']['Attributes']['SeatsCount'],
    )


def get_closest_bar(bars_list, args):
    return min(
        bars_list,
        key=lambda item: [
            abs(item['geometry']['coordinates'][0] - args.longitude),
            abs(item['geometry']['coordinates'][1] - args.latitude),
        ],
    )


def prettify_json(python_obj):
    return json.dumps(python_obj, ensure_ascii=False, indent=4, sort_keys=True)


def print_info_bar(some_bar):
    print(
        'Name:\t\t{}'.format(
            some_bar['properties']['Attributes']['Name']
        ),
        'Address:\t{}'.format(
            some_bar['properties']['Attributes']['Address']
        ),
        'Seats Count:\t{}'.format(
            some_bar['properties']['Attributes']['SeatsCount']
        ),
        'Coordinates:\t{}'.format(
            some_bar['geometry']['coordinates']
        ),
        sep='\n',
        end='\n\n',
    )


if __name__ == '__main__':
    myparcer = MyArgParcer()
    args = myparcer.parse_args()
    bars_list = load_data(args.bars_json)['features']

    if args.verbosity:
        print(
            '\n\The biggest bar\\\n',
            prettify_json(get_biggest_bar(bars_list)),
        )
        print(
            '\n\The smallest bar\\\n',
            prettify_json(get_smallest_bar(bars_list)),
        )
        print(
            '\n\The closest bar\\\n',
            prettify_json(get_closest_bar(bars_list, args))
        )
    else:
        print('\n\The biggest bar\\')
        print_info_bar(get_biggest_bar(bars_list))
        print('\The smallest bar\\')
        print_info_bar(get_smallest_bar(bars_list))
        print('\The closest bar\\')
        print_info_bar(get_closest_bar(bars_list, args))
