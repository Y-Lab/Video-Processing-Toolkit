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
        f'overlay=main_w-overlay_w-{10}:{10+72}',
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


def add_opening(input_file, opening_file, output_file):
    subprocess.run([
        'ffmpeg',
        '-r',
        '30',
        '-i',
        input_file,
        '-i',
        opening_file,
        '-f',
        'lavfi',
        '-t',
        '0.1',
        '-i',
        'anullsrc',
        '-filter_complex',
        '[1:v:0][2:a][0:v:0][0:a:0] concat=n=2:v=1:a=1 [v][a]',
        '-map',
        '[v]',
        '-map',
        '[a]',
        '-r',
        '30',
        '-async',
        '1',
        '-vsync',
        '1',
        output_file,
    ])


def concat_and_add_opening(input_files, opening_file, output_file):
    cmd = ['ffmpeg']
    for input_file in input_files:
        cmd.append('-r')
        cmd.append('30')
        cmd.append('-i')
        cmd.append(input_file)
    cmd += [
        '-i',
        opening_file,
        '-f',
        'lavfi',
        '-t',
        '0.1',
        '-i',
        'anullsrc',
        '-filter_complex',
        f"[{len(input_files)}:v:0][{len(input_files)+1}:a]{''.join([f'[{i}:v:0][{i}:a:0]' for i in range(len(input_files))])} concat=n={len(input_files)+1}:v=1:a=1 [v][a]",
        '-map',
        '[v]',
        '-map',
        '[a]',
        '-r',
        '30',
        '-async',
        '1',
        '-vsync',
        '1',
        output_file,
    ]
    subprocess.run(cmd)


def concatentate(input_files, output_file):
    cmd = ['ffmpeg']
    for input_file in input_files:
        cmd.append('-r')
        cmd.append('30')
        cmd.append('-i')
        cmd.append(input_file)
    cmd += [
        '-filter_complex',
        f"{''.join([f'[{i}:v:0][{i}:a:0]' for i in range(len(input_files))])} concat=n={len(input_files)}:v=1:a=1 [v][a]",
        '-map',
        '[v]',
        '-map',
        '[a]',
        '-r',
        '30',
        '-async',
        '1',
        '-vsync',
        '1',
        output_file,
    ]
    subprocess.run(cmd)
