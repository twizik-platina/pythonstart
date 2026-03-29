from courier import Courier

class FootCourier(Courier):
    _max_distance: float
    _speed: float

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int, 
                 balance: float, is_busy: bool, max_distance: float, speed: float) -> None:
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        
        if max_distance <= 0:
            raise ValueError("Максимальная дистанция должна быть больше 0")
        if speed <= 0:
            raise ValueError("Скорость должна быть больше 0")
        
        self._max_distance = max_distance
        self._speed = speed

    def print_info(self) -> None:
        super().print_info()
        print(f"Максимальная дистанция: {self._max_distance} км")
        print(f"Скорость: {self._speed} км/ч")

    def deliver_order(self, distance: float) -> None:
        if distance <= 0:
            print("Ошибка: расстояние должно быть больше 0")
            return
        
        if distance > self._max_distance:
            print(f"Пеший курьер {self._name} не может взять заказ на {distance} км (максимум {self._max_distance} км)")
            return
        
        if self._is_busy:
            print(f"Курьер {self._name} занят, не может взять заказ")
            return
        
        self._is_busy = True
        self._completed_orders += 1
        salary = self.calculate_salary_for_order(distance)
        self._balance += salary
        
        if distance > self._max_distance * 0.8:
            self._rating = max(0.0, self._rating - 0.1)
            print(f"Длинный маршрут! Рейтинг снижен до {self._rating:.1f}")
        
        print(f"Пеший курьер {self._name} доставил заказ на {distance} км. Заработано: {salary} руб.")
        self._is_busy = False

    def calculate_salary_for_order(self, distance: float) -> float:
        return 120.0 + (25.0 * distance)