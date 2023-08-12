import json

import pytest

from utils import utils

PATH_TO_TEST_FILE = "/home/stanislav/skypro_project/last_five_surgeries /tests/operations.json"

test_list_by_key = [{"state": "EXECUTED"},
                    {"state": "EXECUTED"},
                    {"bug": "EXECUTED"},
                    {"state": "EXECUTED"},
                    {"frog": "EXECUTED"},
                    {"state": "EXECUTED"},
                    {"state": "executed"},
                    {"state": "EXECUTED"},
                    {"state": "EXECUTED"}
                    ]

test_list_by_sort = [{"date": "2020-08-26T10:50:58.294041"},
                     {"no_date": "2019-07-03T18:35:29.512364"},
                     {"no_date": "2018-06-30T02:08:58.425572"},
                     {"date": "2016-12-20T16:43:26.929246"},
                     {"date": "2017-03-23T10:45:06.972075"}]


@pytest.fixture
def read():
    with open(PATH_TO_TEST_FILE) as file:
        result_test = json.load(file)
    return result_test


def test_read_file(read):
    assert utils.read_file(PATH_TO_TEST_FILE) == read


def test_format_date():
    assert utils.format_date("2018-12-20T16:43:26.929246") == "20.12.2018"


def test_last_transactions():
    assert utils.last_transactions(test_list_by_key) == [{"state": "EXECUTED"},
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


def test_sort_transactions_by_date():
    assert utils.sort_transactions_by_date(test_list_by_sort) == [{"date": "2020-08-26T10:50:58.294041"},
                                                                  {"date": "2017-03-23T10:45:06.972075"},
                                                                  {"date": "2016-12-20T16:43:26.929246"}]
