import json

from constants import PATH


def read_file(path=PATH):
    with open(path, "r") as file:
        result = json.load(file)
    return result

