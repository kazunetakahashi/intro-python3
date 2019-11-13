#
# File    : list.py
# Author  : Kazune Takahashi
# Created : 2019/11/11 12:02:03
# Powered by Visual Studio Code
#

number_list = [n for n in range(1, 6)]
print(number_list)

n = 5
m = 6
cells = [(i, j) for i in range(0, n) for j in range(0, m)]
for cell in cells:
    print(cell)

phrase = "Sunaemon met Dr. Tanimura in Otemachi."
dic = {letter: phrase.count(letter) for letter in set(phrase)}
print(dic)
