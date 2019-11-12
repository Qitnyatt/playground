# https://www.codewars.com/kata/sum-of-cubes/train/python


def sum_cubes(n):
    return sum(x ** 3 for x in range(1, n + 1))
