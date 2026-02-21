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

def save_to_txt_for_human(filename):

    try:
        file_out = open(filename, "w", encoding="utf-8")
        file_out.write(
            f"{'ИД':<5}{'Производитель':<15}{'Процессор':<20}{'Видеокарта':<15}{'ОЗУ(ГБ)':<8}{'SSD(ГБ)':<8}{'Вес(г)':<8}{'Цена(руб)':<12}{'В наличии':<10}\n"
        )
        
        for item in computers:
            file_out.write(
                f"{item.id:<5}{item.manufacturer:<15}{item.processor:<20}{item.video_card:<15}{item.ram:<8}{item.ssd:<8}{item.weight:<8}{item.price:<12}{item.amount:<10}\n"
            )
        file_out.close()
        print(f"Сохранено в {filename}")
    except:
        print(f"Ошибка сохранения")

def save_to_txt_for_computer(filename):

    try:
        file_out = open(filename, "w", encoding="utf-8")
        global next_id
        file_out.write(f"{next_id}\n")
        file_out.write(f"{len(computers)}\n")

        for item in computers:
            file_out.write(
                f"{item.id}\n{item.manufacturer}\n{item.processor}\n{item.video_card}\n{item.ram}\n{item.ssd}\n{item.weight}\n{item.price}\n{item.amount}\n"
            )
        file_out.close()
        print(f"Сохранено в {filename}")
    except:
        print(f"Ошибка сохранения")

def load_from_txt_for_computer(filename):

    try:
        file_in = open(filename, "r", encoding="utf-8")
        global next_id
        global computers
        
        next_id = int(file_in.readline())
        count = int(file_in.readline())
        
        loaded = []
        for _ in range(count):
            id = int(file_in.readline())
            manufacturer = file_in.readline().strip()
            processor = file_in.readline().strip()
            video_card = file_in.readline().strip()
            ram = int(file_in.readline())
            ssd = int(file_in.readline())
            weight = int(file_in.readline())
            price = int(file_in.readline())
            amount = int(file_in.readline())
            
            loaded.append(Computer(id, manufacturer, processor, video_card, ram, ssd, weight, price, amount))
        
        computers = loaded
        file_in.close()
        print(f"Загружено из {filename}")
    except:
        print(f"Ошибка загрузки")

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

def set_sale():
    comp_id = int(input("Введите ID компьютера: "))
    
    for comp in computers:
        if comp.id == comp_id:
            comp.price = int(comp.price*0.9)
            print(f"Цена со скидкой составляет {comp.price} рублей")
            return
    
    print("Компьютер не найден")

def min_max_price():
    if not computers:
        print("Список компьютеров пуст")
        return
        
    min=10**9
    max=0
    max_index=0
    min_index=0
    for i in range(len(computers)):
        if computers[i].price>max:
            max=computers[i].price
            max_index=i
        if computers[i].price<min:
            min=computers[i].price
            min_index=i
    print("Самый дешевый: ")
    print_comp(min_index)
    print("Самый дорогой: ")
    print_comp(max_index)

def sort_videocard(card_name2):
    num_card_name2=""
    for j in range(len(card_name2)):
        if card_name2[j].isdigit():
            num_card_name2+=card_name2[j]
    
    if not num_card_name2:
        print("В названии видеокарты не найдено цифр")
        return

    found = False
    for i in range(len(computers)):
        num_card_name1=""
        for j in range(len(computers[i].video_card)):
            if computers[i].video_card[j].isdigit():
                num_card_name1+=computers[i].video_card[j]
        
        if num_card_name1 and int(num_card_name2) <= int(num_card_name1):
            print_comp(i)
            found = True
    
    if not found:
        print("Компьютеры с указанной или более мощной видеокартой не найдены")

def print_comp(index):
    print(f"ID: {computers[index].id}")
    print(f"Производитель: {computers[index].manufacturer}")
    print(f"Процессор: {computers[index].processor}")
    print(f"Видео карта: {computers[index].video_card}")
    print(f"ОЗУ: {computers[index].ram}")
    print(f"Вес ссд накопителя: {computers[index].ssd}")
    print(f"Вес: {computers[index].weight}")
    print(f"Цена: {computers[index].price}")
    print(f"Кол-во на складе: {computers[index].amount}")

computers.append(Computer(1, "Dell", "Intel i5", "GTX 1650", 8, 512, 2000, 50000, 5))
computers.append(Computer(2, "HP", "AMD Ryzen 7", "RTX 3060", 16, 1000, 2500, 120000, 3))
next_id = 3

while True:
    print("УПРАВЛЕНИЕ КОМПЬЮТЕРАМИ")
    print("1. Поиск компьютеров")
    print("2. Сортировка")
    print("3. Добавить компьютер")
    print("4. Удалить компьютер")
    print("5. Увеличить ОЗУ")
    print("6. Показать все")
    print("7. Выставить на распродажу (10%)")
    print("8. Вывести самый дорогой и самый дешевый")
    print("9. Сортировка по видеокарте")
    print("10. Сохранить в человекочитаемый файл")
    print("11. Сохранить в машиночитаемый файл")
    print("12. Загрузить из машиночитаемого файла")
    print("0. Выход")
    
    choice = input("Выберите: ")
    
    if choice == "1":
        search_computers()
        input()
    elif choice == "2":
        sort_computers()
        input()
    elif choice == "3":
        add_computer()
        input()
    elif choice == "4":
        delete_computer()
        input()
    elif choice == "5":
        increase_ram()
        input()
    elif choice == "6":
        show_all()
        input()
    elif choice == "7":
        set_sale()
        input()
    elif choice == "8":
        min_max_price()
        input()
    elif choice == "9":
        card_name=input("Введите минимальную видеокарту:")
        sort_videocard(card_name)
        input()
    elif choice == "10":
        filename = input("Введите имя файла для сохранения (человекочитаемый): ")
        save_to_txt_for_human(filename)
        input()
    elif choice == "11":
        filename = input("Введите имя файла для сохранения (машиночитаемый): ")
        save_to_txt_for_computer(filename)
        input()
    elif choice == "12":
        filename = input("Введите имя файла для загрузки: ")
        load_from_txt_for_computer(filename)
        input()
    elif choice == "0":
        print("Выход")
        break
    else:
        print("Неверный выбор")
        input()