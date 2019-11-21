# https://www.codewars.com/kata/count-and-group-character-occurrences-in-a-string/train/python


import collections


def get_char_count(s):
    c = collections.Counter()
    for ch in s.lower():
        if ch.isalpha() or ch.isdigit():
            c[ch] += 1
    result = collections.defaultdict(list)
    for el in c.most_common():
        result[el[1]].append(el[0])
    for k in result:
        result[k] = sorted(result[k])
    return dict(result)
