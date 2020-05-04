# https://www.codewars.com/kata/merging-sorted-integer-arrays-without-duplicates/train/python


def merge_arrays(first, second):
    return sorted(set(first + second))
