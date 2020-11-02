import re

regColonDash = re.compile(
    r'^[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}$')
regDot = re.compile(r'^[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}$')


def isValidMac(mac):

    valid = False

    if regColonDash.match(mac) != None or regDot.match(mac) != None:
        valid = True

    return valid
