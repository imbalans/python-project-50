from gendiff.parser import read_file
from gendiff.formaters import choice_formater
from gendiff.generate import build_diff


def generate_diff(file_path1, file_path2, formater="stylish"):
    file1 = read_file(file_path1)
    file2 = read_file(file_path2)
    content = build_diff(file1, file2)
    return choice_formater.apply_formatter(content, formater)
