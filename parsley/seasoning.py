import re


def regex_parse(col, string):
        regex = f"r'({col}|\"{col}\"):(\d+\.\d*|\d+|\w+|\"\d+\"|\"\w+\")" # pylint: disable=anomalous-backslash-in-string
        found = re.findall(regex, string)
        regex2 = r'[^,\[\]](\w+[^,]):'
        removed = re.sub(regex2, '', found)
        return removed