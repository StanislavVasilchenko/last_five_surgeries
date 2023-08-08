import json

from utils.utils import read_file, format_date
from constants import PATH


def test_read_file():
    with open(PATH, "r") as file:
        result_test = json.load(file)
    assert read_file() == result_test


def test_format_date():
    assert format_date("2018-12-20T16:43:26.929246") == "20.12.2018"
