class Courier:
    _name: str
    _experience: int
    _rating: float
    _completed_orders: int
    _balance: float
    _is_busy: bool

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int, balance: float, is_busy: bool) -> None:
        if not name or len(name.strip()) == 0:
            raise ValueError("Имя не может быть пустой строкой")
        if experience < 0:
            raise ValueError("Опыт не может быть отрицательным")
        if rating < 0.0 or rating > 5.0:
            raise ValueError("Рейтинг должен быть от 0.0 до 5.0")
        if completed_orders < 0:
            raise ValueError("Количество заказов не может быть отрицательным")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        
        self._name = name
        self._experience = experience
        self._rating = rating
        self._completed_orders = completed_orders
        self._balance = balance
        self._is_busy = is_busy

    def print_info(self) -> None:
        print(f"Имя: {self._name}")
        print(f"Опыт: {self._experience} мес.")
        print(f"Рейтинг: {self._rating}")
        print(f"Выполнено заказов: {self._completed_orders}")
        print(f"Баланс: {self._balance} руб.")
        print(f"Занят: {'Да' if self._is_busy else 'Нет'}")

    def deliver_order(self, distance: float) -> None:
        raise NotImplementedError("метод deliver_order не определён в текущем классе")

    def calculate_salary_for_order(self, distance: float) -> float:
        raise NotImplementedError("метод calculate_salary_for_order не определён в текущем классе")

    def finish_shift(self) -> None:
        self._is_busy = False
        print(f"Смена завершена. Итог: {self._completed_orders} заказов, баланс: {self._balance} руб.")