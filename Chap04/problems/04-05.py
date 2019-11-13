#
# File    : 04-05.py
# Author  : Kazune Takahashi
# Created : 11/13/2019, 2:14:54 PM
# Powered by Visual Studio Code
#

dic = {i: i**2 for i in range(10)}
for key, value in dic.items():
    print("key:", key, ", value:", value)
