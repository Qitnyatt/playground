# https://www.codewars.com/kata/find-the-parity-outlier/train/python


def find_outlier(integers):
    if integers[0] % 2 != integers[1] % 2:
        if integers[2] % 2 == integers[1] % 2:
            return integers[0]
        return integers[1]
    sign = integers[0] % 2
    for x in integers:
        if x % 2 != sign:
            return x
