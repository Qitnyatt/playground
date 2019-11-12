# https://www.codewars.com/kata/multiple-of-index/train/python


def multiple_of_index(arr):
    return [x for i, x in enumerate(arr) if i != 0 and not x % i]
