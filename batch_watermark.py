# -*- coding: utf-8 -*-

import os
from toolkit import DATA_DIR, INPUT_DATA_DIR, OUTPUT_DATA_DIR
from toolkit.utils import make_dirs_for_file, exist
from toolkit.tools import watermark


def batch_watermark():
    watermark_file = os.path.join(DATA_DIR, 'watermark.png')

    for root, dirs, files in os.walk(INPUT_DATA_DIR):
        for filename_with_ext in files:
            filename, file_ext = os.path.splitext(filename_with_ext)
            if file_ext in ['.mp4', '.MP4']:
                input_file = os.path.join(root, filename_with_ext)
                output_file = os.path.join(root.replace(INPUT_DATA_DIR, f'{OUTPUT_DATA_DIR}/watermark'), f'{filename}{file_ext.lower()}')
                print(f'Watermarking: {input_file} -> {output_file}')
                if not exist(pathname=output_file, overwrite=True):
                    make_dirs_for_file(pathname=output_file)
                watermark(input_file=input_file, watermark_file=watermark_file, output_file=output_file)
                print('----')


if __name__ == '__main__':
    batch_watermark()
