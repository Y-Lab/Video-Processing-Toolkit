# -*- coding: utf-8 -*-

import os
from toolkit import DATA_DIR, INPUT_DATA_DIR, OUTPUT_DATA_DIR
from toolkit.utils import make_dirs_for_file, exist
from toolkit.tools import add_opening


MINOR_OPENING_DATA_DIR = os.path.join(DATA_DIR, 'opening', 'minor')


def batch_add_minor_opening():
    for root, dirs, files in os.walk(INPUT_DATA_DIR):
        for filename_with_ext in files:
            filename, file_ext = os.path.splitext(filename_with_ext)
            if file_ext in ['.mp4', '.MP4']:
                input_file = os.path.join(root, filename_with_ext)
                output_file = os.path.join(root.replace(INPUT_DATA_DIR, f'{OUTPUT_DATA_DIR}/add_opening'), f'{filename}{file_ext.lower()}')
                opening_file = os.path.join(MINOR_OPENING_DATA_DIR, f'{filename}{file_ext.lower()}')
                print(f'Add opening: {input_file} -> {output_file}')
                if not exist(pathname=output_file, overwrite=True):
                    make_dirs_for_file(pathname=output_file)
                add_opening(input_file=input_file, opening_file=opening_file, output_file=output_file)
                print('----')


if __name__ == '__main__':
    batch_add_minor_opening()
