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
    results = computers.copy()
    
    ram_min = int(input("Минимальное ОЗУ (0 если не важно): ") or 0)
    price_max = int(input("Максимальная цена (0 если не важно): ") or 0)
    
    if ram_min > 0:
        results = [c for c in results if c.ram >= ram_min]
    if price_max > 0:
        results = [c for c in results if c.price <= price_max]
    
    print_computers(results)


def sort_computers():
    print("1 - по цене")
    print("2 - по сумме ОЗУ+SSD")
    choice = input("Выберите: ")
    
    if choice == "1":
        sorted_list = sorted(computers, key=lambda x: x.price)
    elif choice == "2":
        sorted_list = sorted(computers, key=lambda x: x.ram + x.ssd)
    else:
        print("Неверный выбор")
        return
    
    print_computers(sorted_list)


def add_computer():
    global next_id
    
    print("Добавление компьютера:")
    manufacturer = input("Производитель: ")[:15]
    processor = input("Процессор: ")[:20]
    video_card = input("Видеокарта: ")[:20]
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
    print("Удалить по: 1 - ID, 2 - номеру в списке")
    choice = input("Выберите: ")
    
    if choice == "1":
        id_to_delete = int(input("Введите ID: "))
        for i, comp in enumerate(computers):
            if comp.id == id_to_delete:
                computers.pop(i)
                print(f"Удален компьютер ID {id_to_delete}")
                return
    elif choice == "2":
        index = int(input("Введите номер: ")) - 1
        if 0 <= index < len(computers):
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