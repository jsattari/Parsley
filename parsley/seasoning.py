import re


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
    newlist = value.replace('[','').replace(']','').replace("'",'').replace(' ','')
    newnewlist = newlist.split(',')
    total = 0
    for i in range(0, len(newnewlist)):
        num = int(newnewlist[i])
        total = total + num
    return total

def avgup(value):
    '''Add up values from a list after formatting'''
    newlist = value.replace('[','').replace(']','').replace("'",'').replace(' ','')
    newnewlist = newlist.split(',')
    total = 0
    for i in range(0, len(newnewlist)):
        num = int(newnewlist[i])
        total = total + num
    return total / len(newnewlist)
