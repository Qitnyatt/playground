#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import pathlib
import shutil
import string
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
        title = soup.find('title')
        title_str = title.string
        print(title_str)
        title_str_purified = title_str.replace('Train: ', '', 1)
        title_str_purified = title_str_purified[::-1].replace(' | Codewars'[::-1], '', 1)[::-1]
        title_str_purified = ''.join(
            x.lower() if x.lower() in string.ascii_letters + string.digits else ' '
            for x in title_str_purified) \
            .replace('  ', ' ') \
            .replace('  ', ' ') \
            .replace(' ', '_') \
            .replace('__', '_')
        title_str_purified = title_str_purified[:-1] if title_str_purified[-1] == '_' else title_str_purified
        print(title_str_purified)
        if (title_str_purified == 'codewars'):  # 404
            continue
        dir_name = item.parent.resolve().absolute()
        new_basename = title_str_purified + item.suffix
        new_fullpath: pathlib.Path = dir_name / new_basename
        if (new_fullpath.exists()):
            with open(f'{new_fullpath}', 'rb') as fh_in:
                sha1_exists_file = hashlib.sha1()
                while True:
                    data = fh_in.read(64 * 1024)
                    if not data:
                        break
                    sha1_exists_file.update(data)
                sha1_exists_file = sha1_exists_file.hexdigest()
            with open(f'{item}', 'rb') as fh_in:
                sha1_candidate_file = hashlib.sha1()
                while True:
                    data = fh_in.read(64 * 1024)
                    if not data:
                        break
                    sha1_candidate_file.update(data)
                sha1_candidate_file = sha1_candidate_file.hexdigest()

            if (sha1_exists_file != sha1_candidate_file):
                raise Exception(new_fullpath)
        print(new_fullpath)
        shutil.move(f'{item}', f'{new_fullpath}')
        print('=' * 80)


if __name__ == '__main__':
    main()
