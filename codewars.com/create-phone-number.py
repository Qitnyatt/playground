# https://www.codewars.com/kata/create-phone-number/train/python


def create_phone_number(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
