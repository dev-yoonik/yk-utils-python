""" File handling """
import json


def read_json_from_file(filename: str) -> dict:
    """Load json configuration file.
    :param filename:
        Path to file.
    :return:
        Loaded configuration as a dict.
    """
    if not filename:
        raise ValueError('Filename must be provided.')

    config = None
    with open(filename) as f:
        config = json.load(f)
    return config


def write_json_to_file(dictionary: dict, filename: str) -> None:
    """
    Write dictionary to file
    :param dictionary:
        dictionary to be stored.
    :param filename:
        path to config file.
    """
    if not filename:
        raise ValueError('Filename must be provided.')

    with open(filename, 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)
