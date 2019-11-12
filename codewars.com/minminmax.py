# https://www.codewars.com/kata/minminmax/train/python


def minMinMax(arr):
    smallest = min(arr)
    largest = max(arr)
    for minimum_absent in range(smallest, largest):
        if minimum_absent not in arr:
            return [smallest, minimum_absent, largest]
