# -*- coding: utf-8 -*-

import os
from . import BASE_DIR


def make_dirs_for_file(pathname):
    try:
        os.makedirs(os.path.split(pathname)[0])
    except:
        pass


def exist(pathname, overwrite=False, display_info=True):
    def __path_type(pathname):
        if os.path.isfile(pathname):
            return 'File'
        if os.path.isdir(pathname):
            return 'Directory'
        if os.path.islink(pathname):
            return 'Symbolic Link'
        if os.path.ismount(pathname):
            return 'Mount Point'
        return 'Path'
    if os.path.exists(pathname):
        if overwrite:
            if display_info:
                print(f'{__path_type(pathname)}: {pathname} exists. Overwrite.')
            os.remove(pathname)
            return False
        else:
            if display_info:
                print(f'{__path_type(pathname)}: {pathname} exists.')
            return True
    else:
        if display_info:
            print(f'{__path_type(pathname)}: {pathname} does not exist.')
        return False
