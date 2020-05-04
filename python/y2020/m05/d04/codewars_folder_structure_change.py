#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import shutil
import sys

import requests
from bs4 import BeautifulSoup


def main():
    assert len(''.join(sys.argv[1:])) != 0, ''.join(sys.argv[1:])
    path = pathlib.Path(''.join(sys.argv[1:]))
    assert path.exists(), path
    assert path.is_dir(), path
    print(path)
    for item in path.glob('**/*'):
        if not item.is_file():
            continue
        if f'{item}'.find('.idea') != -1:
            continue
        if item.name == '.gitkeep':
            continue
        if item.name.lower() == 'README.md'.lower():
            continue
        print('=' * 80)
        print(item)
        url = 'https://www.codewars.com/'
        line = None
        with open(f'{item}', 'r', encoding='utf-8') as fh_in:
            for current_line in fh_in.read().splitlines(keepends=False):
                if current_line.find(url) != -1:
                    line = current_line
                    print(line)
                    break
            else:
                raise Exception('FIND FAIL')
        line = line[line.find(url):].strip()
        print(line)
        req = requests.get(line)
        soup = BeautifulSoup(req.text, 'lxml')
        css_selector_kyu = '.items-center > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
        kyu_rank = soup.select(css_selector_kyu)[0].text
        assert kyu_rank in [f'{x} kyu' for x in range(1, 8 + 1)], kyu_rank
        kyu_rank_dir = {f'{x} kyu': f'kyu_{x}' for x in range(1, 8 + 1)}.get(kyu_rank)
        language = line.split('/')[-1]
        (path / language / kyu_rank_dir).mkdir(parents=True, exist_ok=True)
        new_fullpath = path / language / kyu_rank_dir / item.name
        shutil.move(f'{item}', f'{new_fullpath}')
        print('=' * 80)


if __name__ == '__main__':
    main()
