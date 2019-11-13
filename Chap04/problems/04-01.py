#
# File    : 04-01.py
# Author  : Kazune Takahashi
# Created : 11/13/2019, 2:09:07 PM
# Powered by Visual Studio Code
#


def f(guess_me):
    if guess_me > 7:
        print("Too high.")
    elif guess_me == 7:
        print("Just right.")
    else:
        print("Too Low.")


for i in range(0, 10):
    print(i)
    f(i)
