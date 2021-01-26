import re


def regex_parse(value, string):
    '''Look for pattern of "key":value or
    "key":"value" and return the value'''

    regex = re.compile(
        r'\"' + value + '\":(\d+|\d+|\"\w+\")')  # pylint: disable=anomalous-backslash-in-string
    found = regex.findall(string)
    return found
