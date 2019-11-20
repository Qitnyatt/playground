# https://www.codewars.com/kata/split-strings/train/python


def solution(s):
    if len(s) % 2:
        s = f'{s}_'
    return [s[i:i + 2] for i in range(0, len(s), 2)]
