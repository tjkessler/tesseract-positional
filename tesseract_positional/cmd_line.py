# Stdlib includes
from argparse import ArgumentParser
from sys import argv

# tesseract_positional include
from tesseract_positional import positional_ocr


def parse_args():

    ap = ArgumentParser()
    ap.add_argument(
        'input_file',
        type=str,
        help='Image to run positional OCR on'
    )
    ap.add_argument(
        'output_file',
        type=str,
        help='Text file to save extracted positional data'
    )
    return vars(ap.parse_args(argv[1:]))


def main():

    args = parse_args()
    positional_ocr(args['input_file'], output_file=args['output_file'])
