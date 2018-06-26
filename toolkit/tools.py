# -*- coding: utf-8 -*-

import subprocess


def watermark(input_file, watermark_file, output_file):
    subprocess.run([
        'ffmpeg',
        '-i',
        input_file,
        '-i',
        watermark_file,
        '-filter_complex',
        'overlay=main_w-overlay_w-10:10',
        output_file,
    ])
