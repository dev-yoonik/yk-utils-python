"""Handling of configuration files"""
import json
import os
import shutil

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

    with open(json_path, 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)


def check_if_directory_exists(directory: str):
    """ Check if directory exists and create if not
    :param directory:
    :return:
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def copy_file_and_rename(origin_dir: str, dest_dir: str, origin_name: str, dest_name: str):
    """ Copy file and rename it.
    :param origin_dir:
        Original directory
    :param dest_dir:
        Target directory
    :param origin_name:
        Original name
    :param dest_name:
        Target name
    :return:
        Nothing
    :raises:
        ValueError if origin file does not exist
    """
    origin_file = os.path.join(origin_dir, origin_name)
    if not os.path.exists(origin_file):
        raise ValueError('original file does not exist.')
    check_if_directory_exists(dest_dir)
    dest_file = os.path.join(dest_dir, dest_name)
    shutil.copy(origin_file, dest_file)
