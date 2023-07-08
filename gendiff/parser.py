import json
import yaml


def read_file(file_path):
    extension = file_path[-4:]
    content = open(file_path)
    return parse(content, extension)


def parse(content, extension):
    if extension == "json":
        return dict((json.load(content)).items())
    if extension == "yaml" or extension == ".yml":
        return dict((yaml.safe_load(content)).items())
    raise ValueError('Unsupported format. '
                     'Next formats are supported: .json .yaml .yml')
