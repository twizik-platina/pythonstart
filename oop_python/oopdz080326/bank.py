from account import Account


class Bank:
    __accounts: list[Account]

    def __init__(self) -> None:
        self.__accounts = []

    def add_account(self, account: Account) -> None:
        self.__accounts.append(account)

    def get_account_by_number(self, account_number: int) -> Account | None:
        for item in self.__accounts:
            if item.get_account_number() == account_number:
                return item
        return None

    def print_all_accounts(self) -> None:
        for item in self.__accounts:
            print(item.get_info())