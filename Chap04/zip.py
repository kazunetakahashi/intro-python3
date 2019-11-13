#
# File    : zip.py
# Author  : Kazune Takahashi
# Created : 2019/11/11 11:53:53
# Powered by Visual Studio Code
#

english = "Monday", "Tuesday", "Wednesday"
french = "Lundi", "Mardi", "Mercredi"

x = zip(english, french)
print(x)
l = list(x)
print(l)
d = dict(x)  # not good
print(d)
dd = dict(zip(english, french))
print(dd)

for en, fr in l:
    print('The word "', fr, '" means', en, 'in French.')
for en, fr in dd.items():
    print('The word "', fr, '" means', en, 'in French.')
