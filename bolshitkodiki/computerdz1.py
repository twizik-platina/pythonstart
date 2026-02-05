from dataclasses import dataclass

@dataclass
class Computer:
    id: int
    manufacturer: str
    processor: str
    video_card: str
    ram: int
    ssd: int
    weight: int
    price: int
    amount: int

computers = []
next_id = 1


def search_computers():
    print("Поиск компьютеров:")
    ram_min = int(input("Мин. ОЗУ (0 - не важно): ") or 0)
    price_max = int(input("Макс. цена (0 - не важно): ") or 0)
    
    print("Результаты поиска:")
    found = False
    for comp in computers:
        if ram_min > 0 and comp.ram < ram_min:
            continue
        if price_max > 0 and comp.price > price_max:
            continue
        
        print(f"ID {comp.id}: {comp.manufacturer}, {comp.processor}, ОЗУ: {comp.ram}ГБ, Цена: {comp.price}руб.")
        found = True
    
    if not found:
        print("Компьютеры не найдены")


def sort_computers():
    print("Сортировка:")
    print("1 - по цене (дешевые сверху)")
    print("2 - по цене (дорогие сверху)")
    print("3 - по сумме ОЗУ+SSD")
    
    choice = input("Выберите: ")
    
    if choice == "1":
        for i in range(len(computers)):
            for j in range(i+1, len(computers)):
                if computers[j].price < computers[i].price:
                    computers[i], computers[j] = computers[j], computers[i]
    elif choice == "2":
        for i in range(len(computers)):
            for j in range(i+1, len(computers)):
                if computers[j].price > computers[i].price:
                    computers[i], computers[j] = computers[j], computers[i]
    elif choice == "3":
        for i in range(len(computers)):
            for j in range(i+1, len(computers)):
                sum_i = computers[i].ram + computers[i].ssd
                sum_j = computers[j].ram + computers[j].ssd
                if sum_j > sum_i:
                    computers[i], computers[j] = computers[j], computers[i]
    else:
        print("Отмена")
        return
    
    print("Отсортированный список:")
    for comp in computers:
        print(f"ID {comp.id}: {comp.price}руб., ОЗУ: {comp.ram}ГБ, SSD: {comp.ssd}ГБ")


def add_computer():
    global next_id
    
    print("Добавление компьютера:")
    manufacturer = input("Производитель: ")
    processor = input("Процессор: ")
    video_card = input("Видеокарта: ")
    ram = int(input("ОЗУ (ГБ): "))
    ssd = int(input("SSD (ГБ): "))
    weight = int(input("Вес: "))
    price = int(input("Цена: "))
    amount = int(input("Количество: "))
    
    computer = Computer(next_id, manufacturer, processor, video_card, ram, ssd, weight, price, amount)
    computers.append(computer)
    next_id += 1
    print(f"Добавлен компьютер ID {computer.id}")


def delete_computer():
    print("Удаление:")
    choice = input("Удалить по ID? (да/нет): ")
    
    if choice.lower() == "да":
        id_to_delete = int(input("Введите ID: "))
        for i in range(len(computers)):
            if computers[i].id == id_to_delete:
                computers.pop(i)
                print(f"Удален компьютер ID {id_to_delete}")
                return
    else:
        print("Список компьютеров:")
        for i, comp in enumerate(computers):
            print(f"{i+1}. ID {comp.id}: {comp.manufacturer} {comp.processor}")
        
        index = int(input("Введите номер для удаления: ")) - 1
        if index >= 0 and index < len(computers):
            deleted = computers.pop(index)
            print(f"Удален компьютер ID {deleted.id}")
            return
    
    print("Компьютер не найден")


def increase_ram():
    comp_id = int(input("Введите ID компьютера: "))
    add_ram = int(input("Сколько ГБ добавить: "))
    
    for comp in computers:
        if comp.id == comp_id:
            comp.ram += add_ram
            print(f"ОЗУ увеличено до {comp.ram} ГБ")
            return
    
    print("Компьютер не найден")


def show_all():
    print("Все компьютеры:")
    if not computers:
        print("Список пуст")
        return
    
    for comp in computers:
        print(f"ID {comp.id}: {comp.manufacturer} {comp.processor}, ОЗУ: {comp.ram}ГБ, SSD: {comp.ssd}ГБ, Цена: {comp.price}руб., В наличии: {comp.amount}шт.")




while True:
    print("УПРАВЛЕНИЕ КОМПЬЮТЕРАМИ")
    print("1. Поиск компьютеров")
    print("2. Сортировка")
    print("3. Добавить компьютер")
    print("4. Удалить компьютер")
    print("5. Увеличить ОЗУ")
    print("6. Показать все")
    print("0. Выход")
    
    choice = input("Выберите: ")
    
    if choice == "1":
        search_computers()
    elif choice == "2":
        sort_computers()
    elif choice == "3":
        add_computer()
    elif choice == "4":
        delete_computer()
    elif choice == "5":
        increase_ram()
    elif choice == "6":
        show_all()
    elif choice == "0":
        print("Выход")
        break
    else:
        print("Неверный выбор")


computers.append(Computer(1, "Dell", "Intel i5", "GTX 1650", 8, 512, 2000, 50000, 5))
computers.append(Computer(2, "HP", "AMD Ryzen 7", "RTX 3060", 16, 1000, 2500, 120000, 3))
next_id = 3