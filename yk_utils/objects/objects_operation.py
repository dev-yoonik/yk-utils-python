import datetime.datetime

def find_str(reference_string: str, pattern: str):
    """
    find position of char or substring
    :param reference_string:
        string
    :param pattern:
        Character or substring
    :return:
        index in the string
    """
    index = 0
    if pattern in reference_string:
        initial_character = pattern[0]
        for character in reference_string:
            if initial_character == character:
                if reference_string[index:index + len(pattern)] == pattern:
                    return index
            index += 1
    return -1


def convert_to_string(input_value):
    """
    :param input_value:
    :return:
    """
    return input_value.__str__()


def datetime2str(value: datetime):
    """
    :param value:
        datetie instance object.
    :return:
        str with the conversion
    """
    if not isinstance(value, datetime):
        raise TypeError("Value is not datetime.")

    return value.__str__()
