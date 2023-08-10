from utils.utils import read_file, last_transactions, format_date, hide_number, sort_transactions_by_date


def main():
    print()
    five_exept_transactions = last_transactions(sort_transactions_by_date(read_file()))
    for transaction in five_exept_transactions:
        date = format_date(transaction.get("date"))
        description = transaction.get("description")
        if "from" in transaction:
            from_ = hide_number(transaction.get("from"))
        else:
            from_ = description
        to = hide_number(transaction.get("to"))
        amount = transaction["operationAmount"].get("amount")
        currency_name = transaction["operationAmount"]["currency"].get("name")
        print(f"{date} {description}\n"
              f"{from_} -> {to}\n"
              f"{amount} {currency_name}")
        print()


if __name__ == "__main__":
    main()
