# Tesseract_Positional
A tool to save positional OCR data to a text file

[![GitHub version](https://badge.fury.io/gh/tjkessler%2Ftesseract_positional.svg)](https://badge.fury.io/gh/tjkessler%2Ftesseract_positional)
[![PyPI version](https://badge.fury.io/py/tesseract_positional.svg)](https://badge.fury.io/py/tesseract_positional)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/tjkessler/tesseract_positional/master/LICENSE.txt)

Tesseract_Positional allows positional data extracted using OCR to be saved as plain-text. Positional data includes text spacing and line breaks.

## Installation

Installation via pip:

```
$ pip install tesseract_positional
```

Installation via cloned repository:

```
$ cd tesseract_positional
$ python setup.py install
```

Additional dependencies (pytesseract, Pillow) will be installed during Tesseract_Positional's installation.

## Basic Usage

### Via a Python script

Saving extracted text to a file:

```python
from tesseract_positional import positional_ocr
positional_ocr('image.tiff', 'output.txt')
```

Obtaining extracted text:

```python
from tesseract_positional import positional_ocr
text = positional_ocr('image.tiff')
```

### Via the command line

```
$ tesseract_positional image.tiff output.txt
```

## Contributing, Reporting Issues and Other Support

To contribute to Tesseract_Positional, make a pull request. Contributions should include tests for new features added, as well as extensive documentation.

To report problems with the software or feature requests, file an issue. When reporting problems, include information such as error messages, your OS/environment and Python version.

For additional support/questions, contact Travis Kessler (travis.j.kessler@gmail.com).
