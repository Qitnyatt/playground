#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import enum


class HashAlgorithm(enum.Enum):
    SHA1 = 'SHA1'
    SHA224 = 'SHA224'
    SHA256 = 'SHA256'
    SHA384 = 'SHA384'
    SHA512 = 'SHA512'
    MD5 = 'MD5'
    CRC32 = 'CRC32'
