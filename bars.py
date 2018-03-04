import json
import argparse


def args_from_parser():
    parser = argparse.ArgumentParser(
        '|Find out and output the smallest bar '
        'the biggest bar and the nearest bar|',
    )
    parser.add_argument(
        '-v',
        '--verbosity',
        help='increase output verbosity',
        action='store_true',
    )
    parser.add_argument(
        'bars_json',
        help='the path to the data file in json format about bars',
    )
    parser.add_argument('longitude', help='float number', type=float)
    parser.add_argument('latitude', help='float number', type=float)
    return parser.parse_args()


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
    output = (
        'Name:\t\t{}\nAddress:\t{}\nSeats Count:\t{}\nCoordinates:\t{}'.format(
            some_bar['properties']['Attributes']['Name'],
            some_bar['properties']['Attributes']['Address'],
            some_bar['properties']['Attributes']['SeatsCount'],
            some_bar['geometry']['coordinates'],
        )
    )
    return output


def print_bar(some_bar, bar_tag, args):
    if args.verbosity:
        print('\n\{}\\'.format(bar_tag), prettify_json(some_bar), sep='\n')
    else:
        print('\n\{}\\'.format(bar_tag), prettify_bar(some_bar), sep='\n')


if __name__ == '__main__':
    try:
        args = args_from_parser()
        bars_list = load_data(args.bars_json)['features']
        print_bar(get_biggest_bar(bars_list), 'The biggest bar', args)
        print_bar(get_smallest_bar(bars_list), 'The smallest bar', args)
        print_bar(get_closest_bar(bars_list, args), 'The closest bar', args)
    except ValueError:
        print(
            'error: there is no JSON data in the file'
            '<{0}>\n specify the JSON data file'.format(args.bars_json)
        )
    except FileNotFoundError:
        print(
            'error: file is not found\ntry $ python bars.py '
            '<path to json file> <longitude> <latitude>'
        )
