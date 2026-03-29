from courier import Courier

class BikeCourier(Courier):
    _bike_type: str
    _stamina: int

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int,
                 balance: float, is_busy: bool, bike_type: str, stamina: int) -> None:
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        
        if not bike_type or len(bike_type.strip()) == 0:
            raise ValueError("Тип велосипеда не может быть пустой строкой")
        if stamina < 0 or stamina > 100:
            raise ValueError("Выносливость должна быть от 0 до 100")
        
        self._bike_type = bike_type
        self._stamina = stamina

    def print_info(self) -> None:
        super().print_info()
        print(f"Тип велосипеда: {self._bike_type}")
        print(f"Выносливость: {self._stamina}")

    def deliver_order(self, distance: float) -> None:
        if distance <= 0:
            print("Ошибка: расстояние должно быть больше 0")
            return
        
        if self._stamina < 10:
            print(f"Велокурьер {self._name} слишком устал (выносливость {self._stamina}) и не может выполнить заказ")
            return
        
        if self._is_busy:
            print(f"Курьер {self._name} занят, не может взять заказ")
            return
        
        self._is_busy = True
        self._completed_orders += 1
        salary = self.calculate_salary_for_order(distance)
        self._balance += salary
        self._stamina = max(0, self._stamina - 15)
        
        print(f"Велокурьер {self._name} доставил заказ на {distance} км на {self._bike_type}. Заработано: {salary} руб. Выносливость: {self._stamina}")
        self._is_busy = False

    def calculate_salary_for_order(self, distance: float) -> float:
        return 150.0 + (30.0 * distance)