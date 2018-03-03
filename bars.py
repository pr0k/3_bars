import json
import argparse


def args_from_parser():
    __parser = argparse.ArgumentParser(
        '|Find out and output the smallest bar '
        'the biggest bar and the nearest bar|\n'
    )
    __parser.add_argument(
        '-v',
        '--verbosity',
        help='increase output verbosity',
        action='store_true',
    )
    __parser.add_argument(
        'bars_json',
        help='the path to the data file in json format about bars',
    )
    __parser.add_argument('longitude', help='float number', type=float)
    __parser.add_argument('latitude', help='float number', type=float)
    return __parser.parse_args()


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


def prettify_bar(some_bar):
    return (
        'Name:\t\t{}\nAddress:\t{}\nSeats Count:\t{}\nCoordinates:\t{}'.format(
            some_bar['properties']['Attributes']['Name'],
            some_bar['properties']['Attributes']['Address'],
            some_bar['properties']['Attributes']['SeatsCount'],
            some_bar['geometry']['coordinates'],
        )
    )


def print_info_bars(bars_list, args):
    if args.verbosity:
        print(
            '\The biggest bar\\',
            prettify_json(get_biggest_bar(bars_list)),
            '\The smallest bar\\',
            prettify_json(get_smallest_bar(bars_list)),
            '\The closest bar\\',
            prettify_json(get_closest_bar(bars_list, args)),
            sep='\n\n',
        )
    else:
        print(
            '\The biggest bar\\',
            prettify_bar(get_biggest_bar(bars_list)),
            '\The smallest bar\\',
            prettify_bar(get_smallest_bar(bars_list)),
            '\The closest bar\\',
            prettify_bar(get_closest_bar(bars_list,args)),
            sep='\n\n',
        )


if __name__ == '__main__':
    args = args_from_parser()
    bars_list = load_data(args.bars_json)['features']
    print_info_bars(bars_list, args)
