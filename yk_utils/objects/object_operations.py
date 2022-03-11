""" Objects operations file """
from urllib.parse import urlparse, urljoin
from yk_utils.objects.exceptions import BadUrl
import datetime


def convert_to_string(input_value):
    """
    :param input_value:
    :return:
    """
    return input_value.__str__()


def datetime2str(value: datetime.datetime):
    """
    :param value:
        datetime instance object.
    :return:
        str with the conversion
    """
    if not isinstance(value, datetime.datetime):
        raise TypeError("Value is not datetime.")

    return value.__str__()


def get_url_domain(url: str) -> str:
    """
    Gets the domain of the given url
    :param url: url
    :return: url main domain
    """
    return urlparse(url).hostname.split('.')[-2]


def is_valid_url(url: str) -> bool:
    """
    Checks the format validity of the given url.
    :param url: url
    :return: True if valid. False otherwise.
    """
    result = urlparse(url)
    return all([result.scheme, result.netloc])


def get_url(base: str, relative: str = "") -> str:
    """
    Joins both base and relative url and checks for its validity.
    If not valid will raise BadUrl exception.
    :param base: base url path to be specified
    :param relative: relative path to be specified
    :return:
    """
    absolute = urljoin(base, relative)
    if is_valid_url(absolute):
        return absolute
    raise BadUrl(f"Bad URL '{absolute}'")
