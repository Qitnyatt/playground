#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import pathlib
import sys


def new_day_new_folder():
    path_pieces = []
    for template in 'y%Y/m%m/d%d'.split('/'):
        piece = datetime.strftime(datetime.utcnow(), template)
        path_pieces.append(piece)
        current_path = os.sep.join(path_pieces)
        pathlib.Path(current_path).mkdir(parents=True, exist_ok=True)
        current_path = current_path + os.sep + '__init__.py'
        if not os.path.exists(current_path):
            with open(current_path, 'a'):
                os.utime(current_path, None)


def main():
    new_day_new_folder()


if __name__ == '__main__':
    main()
