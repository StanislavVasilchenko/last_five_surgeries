import json

from utils.utils import read_file
from constants import PATH


def test_read_file():
    with open(PATH, "r") as file:
        result_test = json.load(file)
    assert read_file() == result_test
