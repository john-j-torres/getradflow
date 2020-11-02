# Returns a string containing the regEx matches from a text file 

import re

def regmatch(reg, file):

    with open(file, 'r') as f:
        lines = f.readlines()

    match = ''

    for line in lines:
        if reg.search(line) != None:
            match += line

    return match.strip()