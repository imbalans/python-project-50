#!/usr/bin/env python3
import json
import argparse
from gendiff.generate_diff import generate_diff

first_file = json.load(open('gendiff/files/json/file1.json'))
second_file = json.load(open('gendiff/files/json/file2.json'))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    return args


def main():
    parse_arguments()
    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
