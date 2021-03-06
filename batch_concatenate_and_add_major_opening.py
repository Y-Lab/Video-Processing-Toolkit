# -*- coding: utf-8 -*-

import os
from toolkit import DATA_DIR, INPUT_DATA_DIR, OUTPUT_DATA_DIR
from toolkit.utils import make_dirs_for_file, exist
from toolkit.tools import concat_and_add_opening


MAJOR_OPENING_DATA_DIR = os.path.join(DATA_DIR, 'opening', 'major')


def batch_concatenate_and_add_major_opening():
    for root, dirs, files in os.walk(INPUT_DATA_DIR):
        input_files = []
        output_file = f"{root.replace(INPUT_DATA_DIR, f'{OUTPUT_DATA_DIR}/concatenate_and_add_opening')}.mp4"
        opening_file = os.path.join(MAJOR_OPENING_DATA_DIR, f'{os.path.split(root)[-1]}.mp4')
        for filename_with_ext in files:
            filename, file_ext = os.path.splitext(filename_with_ext)
            if file_ext in ['.mp4', '.MP4']:
                input_files.append(filename_with_ext)
        if len(input_files):
            input_files.sort(key=lambda x: int(x.split('-')[-1].replace('.mp4', '').replace('.MP4', '')))
            input_files = [os.path.join(root, input_file) for input_file in input_files]
            print(f'Concatenate and add opening: {output_file}')
            if not exist(pathname=output_file, overwrite=True):
                make_dirs_for_file(pathname=output_file)
            concat_and_add_opening(input_files=input_files, opening_file=opening_file, output_file=output_file)
            print('----')


if __name__ == '__main__':
    batch_concatenate_and_add_major_opening()
