# https://www.codewars.com/kata/numericals-of-a-string/train/python


def numericals(s):
    result = []
    seen_it = {}
    result__append = result.append
    for c in set(s):
        seen_it[c] = 0
    for c in s:
        seen_it[c] += 1
        result__append(seen_it[c])
    return ''.join(map(str, result))
