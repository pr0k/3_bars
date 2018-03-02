import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as json_data_file:
        return json.load(json_data_file)


def get_biggest_bar(bars_dict):
    return max(
        bars_dict,
        key=lambda item: item['properties']['Attributes']['SeatsCount'],
    )


def get_smallest_bar(bars_dict):
    return min(
        bars_dict,
        key=lambda item: item['properties']['Attributes']['SeatsCount'],
    )


def get_closest_bar(bars_dict, args):
    return min(
        bars_dict,
        key=lambda item: [
            abs(item['geometry']['coordinates'][0] - args.longitude),
            abs(item['geometry']['coordinates'][1] - args.latitude),
        ],
    )


def print_info_bar(some_bar):
    print(
        '\nName:          {}'.format(
            some_bar['properties']['Attributes']['Name']
        ),
        'Address:       {}'.format(
            some_bar['properties']['Attributes']['Address']
        ),
        'Seats Count:   {}'.format(
            some_bar['properties']['Attributes']['SeatsCount']
        ),
        'Coordinates:   {}'.format(
            some_bar['geometry']['coordinates']
        ),
        sep='\n',
        end='\n\n',
    )


def prettify_json(python_obj):
    return json.dumps(python_obj, ensure_ascii=False, indent=4, sort_keys=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            '|Find out and output the smallest bar, '
            'the biggest bar and the nearest bar|'
        ),
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
    args = parser.parse_args()
    bars_python_dict = load_data(args.bars_json)['features']

    if args.verbosity:
        print(
            '\nThe biggest bar:\n\n',
            prettify_json(get_biggest_bar(bars_python_dict)),
        )
        print(
            '\nThe smallest bar:\n\n',
            prettify_json(get_smallest_bar(bars_python_dict)),
        )
        print(
            '\nThe closest bar\n\n',
            prettify_json(get_closest_bar(bars_python_dict, args))
        )
    else:
        print('The biggest bar:')
        print_info_bar(get_biggest_bar(bars_python_dict))
        print('The smallest bar:')
        print_info_bar(get_smallest_bar(bars_python_dict))
        print('The closest bar:')
        print_info_bar(get_closest_bar(bars_python_dict, args))
