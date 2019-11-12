# https://www.codewars.com/kata/speed-control/train/python


def gps(s, x):
    if not x or len(x) == 1:
        return 0
    return round(
        max(
            (3600.0 * (x[i + 1] - x[i])) / s
            for i in range(0, len(x) - 1)
        )
    )
