# https://www.codewars.com/kata/alphabetical-addition/train/python


import string


def add_letters(*letters):
    index = sum(
        string.ascii_lowercase.find(letter) + 1 for letter in letters
    ) % len(string.ascii_lowercase) - 1
    return string.ascii_lowercase[index]
