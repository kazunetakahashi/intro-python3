#
# File    : 04-10.py
# Author  : Kazune Takahashi
# Created : 11/14/2019, 11:50:58 AM
# Powered by Visual Studio Code
#


def start_end(func):
    def new_func(*args, **kwargs):
        print("start")
        res = func(*args, **kwargs)
        print("end")
        return res
    return new_func


@start_end
def sum_range():
    sum = 0
    for i in range(10):
        sum += i
    return sum


x = sum_range()

print(x)
