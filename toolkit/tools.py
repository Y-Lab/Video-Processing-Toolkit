# -*- coding: utf-8 -*-

import subprocess


def watermark(input_file, watermark_file, output_file):
    subprocess.run([
        'ffmpeg',
        '-r',
        '30',
        '-i',
        input_file,
        '-i',
        watermark_file,
        '-filter_complex',
        'overlay=main_w-overlay_w-10:10',
        '-r',
        '30',
        '-async',
        '1',
        '-vsync',
        '1',
        output_file,
    ])


def scale(input_file, output_file):
    subprocess.run([
        'ffmpeg',
        '-i',
        input_file,
        '-vf',
        'scale=768:432',
        output_file,
    ])


def pad(input_file, output_file):
    subprocess.run([
        'ffmpeg',
        '-i',
        input_file,
        '-vf',
        'pad=768:576:0:72:black',
        output_file,
    ])
