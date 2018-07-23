[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)][python]
[![License](https://img.shields.io/github/license/Y-Lab/Video-Processing-Toolkit.svg)][license]

# Video Processing Toolkit
Y-English Video Processing Toolkit

## Installation
### Requirements
- [macOS][macos] (Recommended)
- [FFmpeg][ffmpeg]
- [Python 3.6+][python]
- [Pip][pip]
- [Virtualenv][virtualenv]

### Get FFmpeg
Please refer to [FFmpeg][ffmpeg] official website.

### Installing with Virtualenv
On Unix, Linux, BSD, macOS, and Cygwin:

```sh
git clone https://github.com/Y-Lab/Video-Processing-Toolkit.git
cd Video-Processing-Toolkit
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Features

### Watermark
```sh
python batch_watermark.py
```

### Scale
```sh
python batch_scale.py
```

### Pad
```sh
python batch_pad.py
```

### Add Minor Opening
```sh
python batch_add_minor_opening.py
```

### Concatenate and Add Major Opening
```sh
python batch_concatenate_and_add_major_opening.py
```

### Concatenate
```sh
python batch_concatenate.py
```

## File Structure
```
├── data/
│   ├── input/
│   │   └── ...
│   └── output/
│       └── ...
├── toolkit/
│   └── __init__.py
├── batch_watermark.py
├── batch_scale.py
├── batch_pad.py
├── batch_add_minor_opening.py
├── batch_concatenate_and_add_major_opening.py
├── batch_concatenate.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

[license]: https://github.com/Y-Lab/Video-Processing-Toolkit/blob/master/LICENSE "License"

[macos]: https://www.apple.com/macos/ "macOS"
[python]: https://docs.python.org/ "Python"
[pip]: https://pypi.python.org/pypi/pip "Pip"
[virtualenv]: https://virtualenv.pypa.io/en/stable/ "Virtualenv"
[ffmpeg]: https://ffmpeg.org/ "FFmpeg"
