#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform


def run_sh_via_cmd(command: str) -> None:
    if platform.system() != 'Windows':
        raise Exception()
    base_cmd = r'''""C:\Progra~1\Git\bin\sh.exe" -c "{cmd}"'''
    result_cmd = base_cmd.format(cmd=command)
    print(result_cmd)
    os.system(result_cmd)  # subprocess.Popen for poor


def main():
    run_sh_via_cmd(r'echo \"Hello, World!\"')
    print(os.getcwd())
    run_sh_via_cmd(r"find . -name '*.py' -o -name '*.py'")
    os.chdir('C:/')
    print(os.getcwd())
    run_sh_via_cmd(r"find . -name '*.dll' -o -name '*.dll'")


if __name__ == '__main__':
    main()
