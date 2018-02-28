import json
from sys import argv


def load_data(filepath):
    with open(filepath, 'r') as json_data_file:
        return json.load(json_data_file)


def get_biggest_bar(python_object):
    return max(python_object['features'], key=lambda item: item['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(python_object):
    return min(python_object['features'], key=lambda item: item['properties']['Attributes']['SeatsCount'])


def get_closest_bar(python_object, longitude, latitude):
    return min(python_object['features'], key=lambda item:
    [abs(item['geometry']['coordinates'][0] - float(longitude)), abs(item['geometry']['coordinates'][1] - float(latitude))])


if __name__ == '__main__':
    try:
        python_obj_data = load_data(argv[1])
        print('\nThe biggest bar: \n')
        print(json.dumps(get_biggest_bar(python_obj_data), ensure_ascii=False, indent=4))
        print('\nThe smallest bar: \n')
        print(json.dumps(get_smallest_bar(python_obj_data), ensure_ascii=False, indent=4))
        print('\nThe closest bar: \n')
        print(json.dumps(get_closest_bar(python_obj_data, argv[2], argv[3]), ensure_ascii=False, indent=4))
    except ValueError:
        print('ERROR:\nthere is no JSON data in the file {0}\nspecify the JSON data file'.format(argv[1]))
    except IndexError:
        print('ERROR:\nnot enough arguments\ntry $ python bars.py <path to json file> <longitude> <latitude>')
