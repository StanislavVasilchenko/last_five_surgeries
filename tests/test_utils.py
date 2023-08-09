import json

import pytest

from utils import utils
from constants import PATH

test_list = [{"state": "EXECUTED"},
             {"state": "EXECUTED"},
             {"bug": "EXECUTED"},
             {"state": "EXECUTED"},
             {"frog": "EXECUTED"},
             {"state": "EXECUTED"},
             {"state": "executed"},
             {"state": "EXECUTED"},
             {"state": "EXECUTED"}
             ]


@pytest.fixture
def read():
    with open(PATH) as file:
        result_test = json.load(file)
    return result_test


def test_read_file(read):
    assert utils.read_file() == read


def test_format_date():
    assert utils.format_date("2018-12-20T16:43:26.929246") == "20.12.2018"


def test_last_transactions():
    assert utils.last_transactions(test_list) == [{"state": "EXECUTED"},
                                                  {"state": "EXECUTED"},
                                                  {"state": "EXECUTED"},
                                                  {"state": "EXECUTED"},
                                                  {"state": "EXECUTED"}
                                                  ]


def test_hide_number():
    assert utils.hide_number("Счет 44812258784861134719") == "Счет **4719"
    assert utils.hide_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert utils.hide_number("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"
    assert utils.hide_number("MasterCard 3152479541115065") == "MasterCard 3152 47** **** 5065"
