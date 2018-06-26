# -*- coding: utf-8 -*-

import ffmpeg


def watermark(input_file, watermark_file, output_file):
    watermark_file = ffmpeg.input(watermark_file)
    return (ffmpeg
        .input(input_file)
        .overlay(watermark_file, x=10, y=10)
        .output(output_file)
        .run()
    )
