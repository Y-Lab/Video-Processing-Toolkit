# -*- coding: utf-8 -*-

import os
import shutil
from toolkit import INPUT_DATA_DIR, OUTPUT_DATA_DIR
from toolkit.utils import make_dirs_for_file, exist
from toolkit.tools import concatentate


def batch_concatenate():
    for root, dirs, files in os.walk(INPUT_DATA_DIR):
        input_files = []
        output_file = f"{root.replace(INPUT_DATA_DIR, f'{OUTPUT_DATA_DIR}/concatenate')}.mp4"
        for filename_with_ext in files:
            filename, file_ext = os.path.splitext(filename_with_ext)
            if file_ext in ['.mp4', '.MP4']:
                input_files.append(filename_with_ext)
        if len(input_files):
            input_files.sort(key=lambda x: (int(x.split('-')[0].replace('总论 Day ', '').replace('L', '')), int(x.split('-')[-1].replace('.mp4', '').replace('.MP4', ''))))
            input_files = [os.path.join(root, input_file) for input_file in input_files]
            print(f'Concatenate: {output_file}')
            if not exist(pathname=output_file, overwrite=True):
                make_dirs_for_file(pathname=output_file)
            if len(input_files) > 1:
                concatentate(input_files=input_files, output_file=output_file)
            else:
                shutil.copyfile(input_files[0], output_file)
            print('----')


if __name__ == '__main__':
    batch_concatenate()
