# https://www.codewars.com/kata/love-vs-friendship/train/python


import string


def words_to_marks(s):
    return sum(string.ascii_lowercase.find(c) + 1 for c in s)
