from courier import Courier

class CarCourier(Courier):
    _car_model: str
    _fuel: float
    _fuel_consumption: float

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int,
                 balance: float, is_busy: bool, car_model: str, fuel: float, fuel_consumption: float) -> None:
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        
        if not car_model or len(car_model.strip()) == 0:
            raise ValueError("Модель автомобиля не может быть пустой строкой")
        if fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть больше 0")
        
        self._car_model = car_model
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def print_info(self) -> None:
        super().print_info()
        print(f"Модель автомобиля: {self._car_model}")
        print(f"Топливо: {self._fuel} л")
        print(f"Расход топлива: {self._fuel_consumption} л/100км")

    def deliver_order(self, distance: float) -> None:
        if distance <= 0:
            print("Ошибка: расстояние должно быть больше 0")
            return
        
        fuel_needed = (distance / 100) * self._fuel_consumption
        
        if fuel_needed > self._fuel:
            print(f"Автокурьер {self._name} не может доставить заказ: недостаточно топлива. Нужно: {fuel_needed:.2f} л, есть: {self._fuel:.2f} л")
            return
        
        if self._is_busy:
            print(f"Курьер {self._name} занят, не может взять заказ")
            return
        
        self._is_busy = True
        self._fuel -= fuel_needed
        self._completed_orders += 1
        salary = self.calculate_salary_for_order(distance)
        self._balance += salary
        
        print(f"Автокурьер {self._name} доставил заказ на {distance} км на {self._car_model}. Заработано: {salary} руб. Остаток топлива: {self._fuel:.2f} л")
        self._is_busy = False

    def calculate_salary_for_order(self, distance: float) -> float:
        return 200.0 + (40.0 * distance)

    def refuel(self, liters: float) -> None:
        if liters <= 0:
            print("Ошибка: количество топлива для заправки должно быть больше 0")
            return
        
        self._fuel += liters
        print(f"Автомобиль {self._car_model} заправлен на {liters} л. Теперь топлива: {self._fuel:.2f} л")