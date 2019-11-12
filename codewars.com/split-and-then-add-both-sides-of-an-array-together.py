# https://www.codewars.com/kata/split-and-then-add-both-sides-of-an-array-together/train/python


import itertools


def split_and_add(numbers, n):
    while n >= 1 and len(numbers) != 1:
        lhs, rhs = numbers[:len(numbers) // 2], numbers[len(numbers) // 2:]
        g = itertools.zip_longest(reversed(lhs), reversed(rhs), fillvalue=0)
        numbers = list(reversed([sum(x) for x in g]))
        n -= 1
    return numbers
