#
# File    : report.py
# Author  : Kazune Takahashi
# Created : 11/14/2019, 12:03:11 PM
# Powered by Visual Studio Code
#


def get_description():
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
