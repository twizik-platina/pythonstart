class Account:
    __account_number: int
    __balance: float
    __interest_rate: float

    def __init__(self, account_number: int, balance: float, interest_rate: float) -> None:
        if balance < 0:
            balance = 0
            
        if interest_rate < 0:
            interest_rate = 0
            
        if account_number < 1_000_000:
            account_number = 1_000_000
            
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        if amount >= 0 and amount <= 1_000_000:
            self.__balance += amount
        else:
            print("Error. Deposit amount must be in range [0; 1000000]")

    def withdraw(self, amount: float) -> None:
        if amount >= 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error. Insufficient funds or invalid amount")

    def calculate_interest(self) -> float:
        interest = self.__balance * (self.__interest_rate / 100)
        return interest

    def get_balance(self) -> float:
        return self.__balance

    def get_account_number(self) -> int:
        return self.__account_number

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    def get_info(self) -> str:
        return f"Account number: {self.__account_number}, Balance: {self.__balance}, Interest rate: {self.__interest_rate}%"