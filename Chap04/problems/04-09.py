#
# File    : 04-09.py
# Author  : Kazune Takahashi
# Created : 11/14/2019, 11:32:58 AM
# Powered by Visual Studio Code
#


def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i


for i in get_odds():
    print(i)
