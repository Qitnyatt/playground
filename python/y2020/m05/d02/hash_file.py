#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import pathlib
import zlib
from typing import Callable
from typing import Union
from y2020.m05.d02.HashAlgorithm import HashAlgorithm


def hash_file(
        fullpath: Union[str, pathlib.Path, bytes],
        hash_algorithm: HashAlgorithm,
        callback_hashing_started: Callable[[], None] = lambda: None,
        callback_hashing_ended: Callable[[], None] = lambda: None,
        callback_hashing_progress: Callable[[float], None] = lambda x: None,
) -> str:
    if isinstance(fullpath, (str, bytes)):
        fullpath = pathlib.Path(fullpath)

    if not fullpath.exists():
        raise Exception(fullpath)
    if not fullpath.is_file():
        raise Exception(fullpath)

    size: int = fullpath.stat().st_size
    curr_size: int = 0
    if hash_algorithm is HashAlgorithm.CRC32:
        buffer_size = 64 * 1024  # FIXME: random number
        callback_hashing_started()
        with open(f'{fullpath}', 'rb') as fh_in:
            buffer = fh_in.read(buffer_size)
            crc32_value = 0
            while buffer:
                crc32_value = zlib.crc32(buffer, crc32_value)
                buffer = fh_in.read(buffer_size)

                callback_hashing_progress(curr_size * 100.0 / size)
                curr_size += buffer_size

            callback_hashing_progress(100.0)

        callback_hashing_ended()

        return hex(crc32_value & 0xFF_FF_FF_FF)[2:]

    else:
        buffer_size = 1024 * 1024  # FIXME: just pretty number
        h = {
            HashAlgorithm.SHA1:   hashlib.sha1,
            HashAlgorithm.SHA224: hashlib.sha224,
            HashAlgorithm.SHA256: hashlib.sha256,
            HashAlgorithm.SHA384: hashlib.sha384,
            HashAlgorithm.SHA512: hashlib.sha512,
            HashAlgorithm.MD5:    hashlib.md5,
        }.get(hash_algorithm)()
        b = bytearray(buffer_size)
        mv = memoryview(b)
        callback_hashing_started()
        with open(f'{fullpath}', 'rb', buffering=0) as fh_in:
            for n in iter(lambda: fh_in.readinto(mv), 0):
                h.update(mv[:n])

                callback_hashing_progress(curr_size * 100.0 / size)
                curr_size += buffer_size

            callback_hashing_progress(100.0)

        callback_hashing_ended()

        return h.hexdigest()


def main():
    for hash_algorithm in HashAlgorithm:
        print(
            hash_file(
                __file__,
                hash_algorithm,
                callback_hashing_started=lambda: print('hashing_started'),
                callback_hashing_ended=lambda: print('hashing_ended'),
                callback_hashing_progress=lambda p: print(p)
            ),
            hash_algorithm
        )


if __name__ == '__main__':
    main()
