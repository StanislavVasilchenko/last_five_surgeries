import json

from constants import PATH


def read_file(path=PATH):
    """Читает данные из файла"""
    with open(path, "r") as file:
        result = json.load(file)
    return result


def last_transactions(data: list):
    five_executed_transactions = []
    for transaction in data:
        if transaction.get("state") == "EXECUTED" and len(five_executed_transactions) < 5:
            five_executed_transactions.append(transaction)
    return five_executed_transactions


def format_date(date: str):
    date_operation = date.split('T')[0].split("-")
    return ".".join(date_operation[::-1])


def hide_number(number: str):
    broken_number = number.split(" ")
    for digits in broken_number:
        if digits.isdigit() and len(digits) > 16:
            hide_number_check = digits[len(digits) - 4:len(digits)]
            return f'{" ".join(broken_number[0:len(broken_number) - 1])} **{hide_number_check}'
        elif digits.isdigit() and len(digits) == 16:
            number_card = [digits[x:x+4] for x in range(0, len(digits), 4)]
            hide_number_card = " ".join([number_card[0], number_card[1][0:2] + "**", "*"*4, number_card[3]])
            return f"{' '.join(broken_number[0:len(broken_number) - 1])} {hide_number_card}"
