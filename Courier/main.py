from foot_courier import FootCourier
from bike_courier import BikeCourier
from car_courier import CarCourier

def main():
    print("=" * 50)
    print("Создание курьеров")
    print("=" * 50)
    

    foot_courier = FootCourier(
        name="Иван Петров",
        experience=12,
        rating=4.5,
        completed_orders=45,
        balance=5400.0,
        is_busy=False,
        max_distance=5.0,
        speed=5.0
    )
    

    bike_courier = BikeCourier(
        name="Алексей Смирнов",
        experience=24,
        rating=4.8,
        completed_orders=120,
        balance=15600.0,
        is_busy=False,
        bike_type="Горный велосипед",
        stamina=85
    )
    

    car_courier = CarCourier(
        name="Дмитрий Козлов",
        experience=36,
        rating=4.9,
        completed_orders=280,
        balance=45200.0,
        is_busy=False,
        car_model="Toyota Camry",
        fuel=45.0,
        fuel_consumption=8.5
    )
    
  
    print("\nИнформация о пешем курьере:")
    print("-" * 30)
    foot_courier.print_info()
    
    print("\nИнформация о велокурьере:")
    print("-" * 30)
    bike_courier.print_info()
    
    print("\nИнформация об автокурьере:")
    print("-" * 30)
    car_courier.print_info()
    
    print("\n" + "=" * 50)
    print("Тестирование доставок")
    print("=" * 50)
    
  
    print("\n--- Пеший курьер ---")
    foot_courier.deliver_order(2.5)  
    foot_courier.deliver_order(6.0)  
    
  
    print("\n--- Велокурьер ---")
    bike_courier.deliver_order(8.0)  
    bike_courier.deliver_order(5.0)  
    

    print("\n--- Автокурьер ---")
    car_courier.deliver_order(50.0)  
    
    print("\n--- Попытка доставки с недостатком топлива ---")
    car_courier.deliver_order(200.0)  
    print("\n--- Заправка автомобиля ---")
    car_courier.refuel(30.0)
    car_courier.deliver_order(200.0)  
    
    print("\n" + "=" * 50)
    print("Информация после доставок")
    print("=" * 50)
    
    print("\nИнформация о пешем курьере:")
    print("-" * 30)
    foot_courier.print_info()
    
    print("\nИнформация о велокурьере:")
    print("-" * 30)
    bike_courier.print_info()
    
    print("\nИнформация об автокурьере:")
    print("-" * 30)
    car_courier.print_info()
    
    print("\n" + "=" * 50)
    print("Завершение смен")
    print("=" * 50)
    
    print("\n--- Завершение смены пешего курьера ---")
    foot_courier.finish_shift()
    
    print("\n--- Завершение смены велокурьера ---")
    bike_courier.finish_shift()
    
    print("\n--- Завершение смены автокурьера ---")
    car_courier.finish_shift()


if __name__ == "__main__":
    main()