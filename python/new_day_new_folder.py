#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from datetime import datetime


def new_day_new_folder(base_dir: pathlib.Path) -> None:
    curr_dir = base_dir
    for piece in 'y%Y/m%m/d%d'.split('/'):
        curr_dir = curr_dir.joinpath(datetime.strftime(datetime.utcnow(), piece))
        curr_dir.mkdir(parents=True, exist_ok=True)
        (curr_dir / '__init__.py').touch()


def main():
    new_day_new_folder(pathlib.Path(__file__).parent)


if __name__ == '__main__':
    main()
