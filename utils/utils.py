import json

from constants import PATH


def read_file(path=PATH):
    with open(path, "r") as file:
        result = json.load(file)
    return result


def format_date(date: str):
    date_operation = date.split('T')[0].split("-")
    return ".".join(date_operation[::-1])
