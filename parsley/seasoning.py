import re
from statistics import median

def regex_parse(value, string):
    '''Look for pattern of "key":value or
    "key":"value" and return the value'''

    regex = re.compile(
        r'\"' + value + '\":(\d+|\d+|\"\w+\")')  # pylint: disable=anomalous-backslash-in-string
    found = regex.findall(string)
    # regex2 = r'[\"\']'
    return found


def addup(value):
    '''Add up values from a list after formatting'''
    newlist = value.replace('[', '').replace(
        ']', '').replace("'", '').replace(' ', '')
    newnewlist = newlist.split(',')
    total = 0
    for i in range(0, len(newnewlist)):
        num = int(newnewlist[i])
        total = total + num
    return total


def avgup(value):
    '''Add up values from a list after formatting'''
    newlist = value.replace('[', '').replace(
        ']', '').replace("'", '').replace(' ', '')
    newnewlist = newlist.split(',')
    total = 0
    for i in range(0, len(newnewlist)):
        num = int(newnewlist[i])
        total = total + num
    return total / len(newnewlist)


def max_val(value):
    '''Get max value from list'''
    bad_list = '[\[|\]|\s]' # pylint: disable=anomalous-backslash-in-string
    new_val = re.sub(bad_list, '', value).split(',')
    return max(new_val)


def min_val(value):
    '''Get min value from list'''
    bad_list = '[\[|\]|\s]' # pylint: disable=anomalous-backslash-in-string
    new_val = re.sub(bad_list, '', value).split(',')
    return min(new_val)


def med_val(value):
    '''Get median value from list'''
    newlist = value.replace('[', '').replace(
        ']', '').replace("'", '').replace(' ', '')
    newnewlist = newlist.split(',')
    newnewlist = [int(s) for s in newnewlist]
    return median(newnewlist)