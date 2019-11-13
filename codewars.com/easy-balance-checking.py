# https://www.codewars.com/kata/easy-balance-checking/train/python


import re


def balance(book):
    result = []
    total_expense = []
    cash = 0.0
    for line in book.splitlines():
        purified_line = re.sub(r'[^a-zA-Z0-9. ]', '', line)
        search = re.search(r'(\d+?\.\d+)|\d+$', purified_line, re.MULTILINE)
        if search:
            money = float(search.group(0))
            if result:
                cash -= money
                total_expense.append(money)
                purified_line = purified_line.replace(search.group(0), '')
                result.append(f'{purified_line}{money:02.2f} Balance {cash:02.2f}')
            else:
                cash = money
                result.append(f'Original Balance: {cash:02.2f}')
    result.append(f'Total expense  {sum(total_expense):02.2f}')
    result.append(f'Average expense  {sum(total_expense) / len(total_expense):02.2f}')

    return '\r\n'.join(result)
