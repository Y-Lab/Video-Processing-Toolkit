[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)][python]
[![License](https://img.shields.io/github/license/Y-Lab/Video-Processing-Toolkit.svg)][license]

# Video Processing Toolkit
Y-English Video Processing Toolkit

## Installation
### Requirements
- [macOS][macos] (Recommended)
- [Python 2.7/3.5+][python]
- [Pip][pip]
- [Virtualenv][virtualenv]

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
```
python watermark.py
```

### Concatenate
```
python concatenate.py
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
├── watermark.py
├── concatenate.py
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
