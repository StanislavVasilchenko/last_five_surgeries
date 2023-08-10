import json
from constants import PATH


def read_file(path=PATH) -> list:
    """Считывает данные из json файла и возвращает список словарей"""
    with open(path, "r") as file:
        result = json.load(file)
    return result


def sort_transactions_by_date(transactions: list, key="date"):
    """Принимает на вход исходный список словарей с транзакциями,
    проверяет наличие ключа "date", если ключ существует, то добавляет
     словарь в новый список. Сортирует новый список по дате, по убыванию"""
    sorted_list = []
    for transaction in transactions:
        if transaction.get(key):
            sorted_list.append(transaction)
    sorted_list.sort(key=lambda x: x[key], reverse=True)
    return sorted_list


def last_transactions(data: list, key="state", value="EXECUTED") -> list:
    """Принимает на вход список словарей и собирает новый список отфильтрованный
    по определенному ключу (по умолчанию "state") и значению этого ключа (по умодчанию "EXECUTED")
    Возвращает список из пяти словарей с искомым ключ=значение"""
    five_executed_transactions = []
    for transaction in data:
        if transaction.get(key) == value and len(five_executed_transactions) < 5:
            five_executed_transactions.append(transaction)
    return five_executed_transactions


def format_date(date: str) -> str:
    """Принимает на вход строку с датой в полном формате (2018-01-26T15:40:13.413061) и возвращает строку
    в формате день.месяц.год (26.01.2018)"""
    date_operation = date.split('T')[0].split("-")
    return ".".join(date_operation[::-1])


def hide_number(number: str):
    """Принимает на вход строку с платежными данными (Счет 44812258784861134719) и возвращает
    строку со скрытым номером счета или карты:
    Счет **4719
    Visa Classic 6831 98** **** 7658
    """
    broken_number = number.split(" ")
    for digits in broken_number:
        if digits.isdigit() and len(digits) > 16:
            hide_number_check = digits[len(digits) - 4:len(digits)]
            return f'{" ".join(broken_number[0:len(broken_number) - 1])} **{hide_number_check}'
        elif digits.isdigit() and len(digits) == 16:
            number_card = [digits[x:x + 4] for x in range(0, len(digits), 4)]
            hide_number_card = " ".join([number_card[0], number_card[1][0:2] + "**", "*" * 4, number_card[3]])
            return f"{' '.join(broken_number[0:len(broken_number) - 1])} {hide_number_card}"
