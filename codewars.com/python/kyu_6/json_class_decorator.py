# https://www.codewars.com/kata/json-class-decorator/train/python


import json


def jsonattr(filepath):
    def inner(cls):
        with open(filepath, 'r') as f_in:
            data = json.load(f_in)
        for attr in data:
            setattr(cls, attr, data[attr])
        return cls

    return inner
