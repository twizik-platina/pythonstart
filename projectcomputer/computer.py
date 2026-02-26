import os
from dataclasses import dataclass

# сущность:
#     Компьютер
# поля:
#     ИД - целое уникальное число
#     Производитель - строка (от 1 до 20 символов)
#     Процессор - строка (от 1 до 30 символов)
#     Видеокарта - строка (от 1 до 20 символов)
#     ОЗУ - целое число (от 1 до 128)
#     SSD - целое число (от 120 до 4000)
#     Вес - целое число (от 500 до 10000)
#     Цена - целое число (от 5000 до 500000)
#     Количество на складе - целое число (от 1 до 1000)


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


GLOBAL_COMPUTER_ID = 0

ASC = "ascending"
DESC = "descending"

MANUFACTURER_MIN_LEN = 1
MANUFACTURER_MAX_LEN = 20

PROCESSOR_MIN_LEN = 1
PROCESSOR_MAX_LEN = 30

VIDEO_CARD_MIN_LEN = 1
VIDEO_CARD_MAX_LEN = 20

RAM_MIN = 1
RAM_MAX = 128

SSD_MIN = 120
SSD_MAX = 4000

WEIGHT_MIN = 500
WEIGHT_MAX = 10000

PRICE_MIN = 5000
PRICE_MAX = 500000

AMOUNT_MIN = 1
AMOUNT_MAX = 1000

FILE_NAME_MIN_LEN = 5
FILE_NAME_MAX_LEN = 40


def clear_console() -> None:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def get_computers_by_manufacturer(computers: list[Computer], manufacturer: str) -> list[Computer]:
    result = []
    for item in computers:
        if item.manufacturer.lower() == manufacturer.lower():
            result.append(item)
    return result


def get_computers_by_processor(computers: list[Computer], processor: str) -> list[Computer]:
    result = []
    for item in computers:
        if item.processor.lower() == processor.lower():
            result.append(item)
    return result


def get_computers_by_video_card(computers: list[Computer], video_card: str) -> list[Computer]:
    result = []
    for item in computers:
        if item.video_card.lower() == video_card.lower():
            result.append(item)
    return result


def sort_computers_by_id(computers: list[Computer], order: str) -> None:
    for i in range(len(computers)):
        for j in range(i+1, len(computers)):
            if order == ASC:
                if computers[j].id < computers[i].id:
                    computers[i], computers[j] = computers[j], computers[i]
            else:
                if computers[j].id > computers[i].id:
                    computers[i], computers[j] = computers[j], computers[i]
    print("список компьютеров по ИД успешно отсортирован")


def sort_computers_by_price(computers: list[Computer], order: str) -> None:
    for i in range(len(computers)):
        for j in range(i+1, len(computers)):
            if order == ASC:
                if computers[j].price < computers[i].price:
                    computers[i], computers[j] = computers[j], computers[i]
            else:
                if computers[j].price > computers[i].price:
                    computers[i], computers[j] = computers[j], computers[i]
    print("список компьютеров по Цене успешно отсортирован")


def sort_computers_by_ram(computers: list[Computer], order: str) -> None:
    for i in range(len(computers)):
        for j in range(i+1, len(computers)):
            if order == ASC:
                if computers[j].ram < computers[i].ram:
                    computers[i], computers[j] = computers[j], computers[i]
            else:
                if computers[j].ram > computers[i].ram:
                    computers[i], computers[j] = computers[j], computers[i]
    print("список компьютеров по ОЗУ успешно отсортирован")

def sort_computers_by_ssd(computers: list[Computer], order: str) -> None:
    for i in range(len(computers)):
        for j in range(i+1, len(computers)):
            if order == ASC:
                if computers[j].ssd < computers[i].ssd:
                    computers[i], computers[j] = computers[j], computers[i]
            else:
                if computers[j].ssd > computers[i].ssd:
                    computers[i], computers[j] = computers[j], computers[i]
    print("список компьютеров по SSD успешно отсортирован")


def input_int(message: str, min_number: int, max_number: int) -> int:
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = int(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_str(message: str, min_length: int, max_length: int) -> str:
    is_correct_input = False

    while is_correct_input == False:
        str_data = input(message).strip()

        if len(str_data) < min_length or len(str_data) > max_length:
            print(
                f"Ошибка ввода. Количество символов должно быть в границах от {min_length} до {max_length}"
            )
            is_correct_input = False
        else:
            is_correct_input = True

    return str_data


def input_computer_data() -> Computer:
    print("Введите данные компьютера")

    manufacturer = input_str("производитель: ", MANUFACTURER_MIN_LEN, MANUFACTURER_MAX_LEN)
    processor = input_str("процессор: ", PROCESSOR_MIN_LEN, PROCESSOR_MAX_LEN)
    video_card = input_str("видеокарта: ", VIDEO_CARD_MIN_LEN, VIDEO_CARD_MAX_LEN)
    ram = input_int("ОЗУ (ГБ): ", RAM_MIN, RAM_MAX)
    ssd = input_int("SSD (ГБ): ", SSD_MIN, SSD_MAX)
    weight = input_int("вес (г): ", WEIGHT_MIN, WEIGHT_MAX)
    price = input_int("цену (руб): ", PRICE_MIN, PRICE_MAX)
    amount = input_int("количество на складе: ", AMOUNT_MIN, AMOUNT_MAX)

    return Computer(
        0, manufacturer, processor, video_card, ram, ssd, weight, price, amount
    )


def add_computer_to_list(computers: list[Computer], computer: Computer) -> None:
    global GLOBAL_COMPUTER_ID
    GLOBAL_COMPUTER_ID += 1

    computer.id = GLOBAL_COMPUTER_ID

    computers.append(computer)

    print("Компьютер успешно добавлен в список")


def find_computer_index_by_id(computers: list[Computer], id: int) -> int:
    for i in range(len(computers)):
        if computers[i].id == id:
            return i
    return -1


def delete_computer_by_id(computers: list[Computer], id: int) -> None:
    delete_index = find_computer_index_by_id(computers, id)

    if delete_index == -1:
        print(f"Компьютер с id = {id} не найден")
        return

    computers.pop(delete_index)
    print(f"Компьютер с id = {id} успешно удалён")


def change_computer_amount(computers: list[Computer], id: int, new_amount: int) -> None:
    change_index = find_computer_index_by_id(computers, id)

    if change_index == -1:
        print(f"Компьютер с id = {id} не найден")
        return

    computers[change_index].amount = new_amount

    print(
        f"Количество на складе у компьютера с id = {id} успешно изменено на {new_amount}"
    )


def change_computer_information(computers: list[Computer], id: int) -> None:
    change_index = find_computer_index_by_id(computers, id)

    if change_index == -1:
        print(f"Компьютер с id = {id} не найден")
        return

    new_computer_data = input_computer_data()

    computers[change_index].manufacturer = new_computer_data.manufacturer
    computers[change_index].processor = new_computer_data.processor
    computers[change_index].video_card = new_computer_data.video_card
    computers[change_index].ram = new_computer_data.ram
    computers[change_index].ssd = new_computer_data.ssd
    computers[change_index].weight = new_computer_data.weight
    computers[change_index].price = new_computer_data.price
    computers[change_index].amount = new_computer_data.amount

    print(f"Параметры у компьютера с id = {id} успешно изменены")


def print_computers(computers: list[Computer]) -> None:
    print(
        f"{'ИД':<5}{'Производитель':<15}{'Процессор':<20}{'Видеокарта':<15}{'ОЗУ(ГБ)':<8}{'SSD(ГБ)':<8}{'Вес(г)':<8}{'Цена(руб)':<12}{'В наличии':<10}"
    )

    if len(computers) == 0:
        print("Список пуст")
        return

    for item in computers:
        print(
            f"{item.id:<5}{item.manufacturer:<15}{item.processor:<20}{item.video_card:<15}{item.ram:<8}{item.ssd:<8}{item.weight:<8}{item.price:<12}{item.amount:<10}"
        )


def print_computer_by_id(computers: list[Computer], id: int) -> None:
    print_index = find_computer_index_by_id(computers, id)

    if print_index == -1:
        print(f"Компьютер с id = {id} не найден")
        return

    print(
        f"{'ИД':<5}{'Производитель':<15}{'Процессор':<20}{'Видеокарта':<15}{'ОЗУ(ГБ)':<8}{'SSD(ГБ)':<8}{'Вес(г)':<8}{'Цена(руб)':<12}{'В наличии':<10}"
    )
    item = computers[print_index]
    print(
        f"{item.id:<5}{item.manufacturer:<15}{item.processor:<20}{item.video_card:<15}{item.ram:<8}{item.ssd:<8}{item.weight:<8}{item.price:<12}{item.amount:<10}"
    )


def save_to_txt_for_human(computers: list[Computer], filename: str) -> None:
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

        print(f"Компьютеры в человекочитаемом виде в файл {filename} успешно сохранены")
    except:
        print(f"Ошибка при сохранении компьютеров в файл {filename}")


def save_to_txt_for_computer(computers: list[Computer], filename: str) -> None:
    try:
        file_out = open(filename, "w", encoding="utf-8")
        global GLOBAL_COMPUTER_ID
        file_out.write(f"{GLOBAL_COMPUTER_ID}\n")
        file_out.write(f"{len(computers)}\n")

        for item in computers:
            file_out.write(
                f"{item.id}\n{item.manufacturer}\n{item.processor}\n{item.video_card}\n{item.ram}\n{item.ssd}\n{item.weight}\n{item.price}\n{item.amount}\n"
            )
        file_out.close()

        print(f"Компьютеры в машиночитаемом виде в файл {filename} успешно сохранены")
    except:
        print(f"Ошибка при сохранении компьютеров в файл {filename}")


def load_from_txt_for_computer(filename: str) -> list[Computer]:
    computers: list[Computer] = []

    try:
        file_in = open(filename, "r", encoding="utf-8")
        global GLOBAL_COMPUTER_ID
        GLOBAL_COMPUTER_ID = int(file_in.readline())
        count_computers = int(file_in.readline())

        for _ in range(count_computers):
            id = int(file_in.readline())
            manufacturer = file_in.readline().strip()
            processor = file_in.readline().strip()
            video_card = file_in.readline().strip()
            ram = int(file_in.readline())
            ssd = int(file_in.readline())
            weight = int(file_in.readline())
            price = int(file_in.readline())
            amount = int(file_in.readline())

            computers.append(
                Computer(
                    id,
                    manufacturer,
                    processor,
                    video_card,
                    ram,
                    ssd,
                    weight,
                    price,
                    amount,
                )
            )

        file_in.close()

        print(f"Компьютеры из файла {filename} успешно загружены")
    except:
        print(f"Ошибка при загрузке компьютеров из файла {filename}")

    return computers


def increase_computer_ram(computers: list[Computer], id: int, add_ram: int) -> None:
    change_index = find_computer_index_by_id(computers, id)

    if change_index == -1:
        print(f"Компьютер с id = {id} не найден")
        return

    computers[change_index].ram += add_ram

    print(
        f"ОЗУ у компьютера с id = {id} успешно увеличено до {computers[change_index].ram} ГБ"
    )


def set_sale_for_computer(computers: list[Computer], id: int) -> None:
    change_index = find_computer_index_by_id(computers, id)

    if change_index == -1:
        print(f"Компьютер с id = {id} не найден")
        return

    computers[change_index].price = int(computers[change_index].price * 0.9)

    print(
        f"Цена со скидкой у компьютера с id = {id} составляет {computers[change_index].price} рублей"
    )


def get_computers_by_video_card_power(computers: list[Computer], card_name: str) -> list[Computer]:
    result = []
    
    num_card_name = ""
    for j in range(len(card_name)):
        if card_name[j].isdigit():
            num_card_name += card_name[j]
    
    if num_card_name == "":
        print("В названии видеокарты не найдено цифр")
        return result
    
    card_power = int(num_card_name)
    
    for i in range(len(computers)):
        num_card = ""
        for j in range(len(computers[i].video_card)):
            if computers[i].video_card[j].isdigit():
                num_card += computers[i].video_card[j]
        
        if num_card != "" and int(num_card) >= card_power:
            result.append(computers[i])
    
    return result


def get_min_max_price_computers(computers: list[Computer]) -> tuple:
    if len(computers) == 0:
        return None, None
    
    min_price = computers[0].price
    max_price = computers[0].price
    min_index = 0
    max_index = 0
    
    for i in range(len(computers)):
        if computers[i].price > max_price:
            max_price = computers[i].price
            max_index = i
        if computers[i].price < min_price:
            min_price = computers[i].price
            min_index = i
    
    return computers[min_index], computers[max_index]


def process_add_computer_menu(computers: list[Computer]) -> None:
    add_computer_to_list(computers, input_computer_data())


def process_delete_computer_menu(computers: list[Computer]) -> None:
    id = input_int("Введите ИД компьютера для удаления: ", 1, GLOBAL_COMPUTER_ID)
    delete_computer_by_id(computers, id)


def process_save_human_menu(computers: list[Computer]) -> None:
    filename = input_str(
        "Введите имя файла для сохранения: ", FILE_NAME_MIN_LEN, FILE_NAME_MAX_LEN
    )
    save_to_txt_for_human(computers, filename)


def process_save_computer_menu(computers: list[Computer]) -> None:
    filename = input_str(
        "Введите имя файла для сохранения: ", FILE_NAME_MIN_LEN, FILE_NAME_MAX_LEN
    )
    save_to_txt_for_computer(computers, filename)


def process_load_computer_menu() -> list[Computer]:
    filename = input_str(
        "Введите имя файла для загрузки: ", FILE_NAME_MIN_LEN, FILE_NAME_MAX_LEN
    )
    return load_from_txt_for_computer(filename)


def process_change_information_menu(computers: list[Computer]) -> None:
    id = input_int("Введите ИД компьютера для обновления: ", 1, GLOBAL_COMPUTER_ID)
    change_computer_information(computers, id)


def process_change_amount_menu(computers: list[Computer]) -> None:
    id = input_int("Введите ИД компьютера для обновления: ", 1, GLOBAL_COMPUTER_ID)
    amount = input_int(
        "Введите новое количество компьютеров на складе: ", AMOUNT_MIN, AMOUNT_MAX
    )
    change_computer_amount(computers, id, amount)


def process_increase_ram_menu(computers: list[Computer]) -> None:
    id = input_int("Введите ИД компьютера: ", 1, GLOBAL_COMPUTER_ID)
    add_ram = input_int("Сколько ГБ добавить: ", 1, RAM_MAX)
    increase_computer_ram(computers, id, add_ram)


def process_set_sale_menu(computers: list[Computer]) -> None:
    id = input_int("Введите ИД компьютера: ", 1, GLOBAL_COMPUTER_ID)
    set_sale_for_computer(computers, id)


def process_print_computer_by_id_menu(computers: list[Computer]) -> None:
    id = input_int("Введите ИД компьютера для вывода: ", 1, GLOBAL_COMPUTER_ID)
    print_computer_by_id(computers, id)


def process_min_max_price_menu(computers: list[Computer]) -> None:
    min_comp, max_comp = get_min_max_price_computers(computers)
    
    if min_comp is None:
        print("Список компьютеров пуст")
        return
    
    print("Самый дешевый компьютер:")
    print(f"ID: {min_comp.id}")
    print(f"Производитель: {min_comp.manufacturer}")
    print(f"Процессор: {min_comp.processor}")
    print(f"Видеокарта: {min_comp.video_card}")
    print(f"ОЗУ: {min_comp.ram}")
    print(f"SSD: {min_comp.ssd}")
    print(f"Вес: {min_comp.weight}")
    print(f"Цена: {min_comp.price}")
    print(f"Кол-во на складе: {min_comp.amount}")
    
    print("\nСамый дорогой компьютер:")
    print(f"ID: {max_comp.id}")
    print(f"Производитель: {max_comp.manufacturer}")
    print(f"Процессор: {max_comp.processor}")
    print(f"Видеокарта: {max_comp.video_card}")
    print(f"ОЗУ: {max_comp.ram}")
    print(f"SSD: {max_comp.ssd}")
    print(f"Вес: {max_comp.weight}")
    print(f"Цена: {max_comp.price}")
    print(f"Кол-во на складе: {max_comp.amount}")


def process_sort_by_video_card_menu(computers: list[Computer]) -> None:
    card_name = input("Введите минимальную видеокарту: ")
    finded_computers = get_computers_by_video_card_power(computers, card_name)
    
    if len(finded_computers) == 0:
        print("Компьютеры с указанной или более мощной видеокартой не найдены")
        return
    
    print("Найденные компьютеры:")
    for comp in finded_computers:
        print(f"ID: {comp.id}")
        print(f"Производитель: {comp.manufacturer}")
        print(f"Процессор: {comp.processor}")
        print(f"Видеокарта: {comp.video_card}")
        print(f"ОЗУ: {comp.ram}")
        print(f"SSD: {comp.ssd}")
        print(f"Вес: {comp.weight}")
        print(f"Цена: {comp.price}")
        print(f"Кол-во на складе: {comp.amount}")
        print()


def process_exit_menu() -> bool:
    print("Для завершения работы программы нажмите <Enter>")
    return False


def process_sort_menu(computers: list[Computer]) -> None:
    print("Выберите первый параметр сортировки")

    print("1. ИД")
    print("2. Цена")
    print("3. ОЗУ")
    print("4. SSD")

    sort_point = input_int("Выберите пункт меню: ", 1, 4)

    print("Выберите второй параметр сортировки")

    print("1. По возрастанию")
    print("2. По убыванию")

    order_point = input_int("Выберите пункт меню: ", 1, 2)

    order = ""
    if order_point == 1:
        order = ASC
    elif order_point == 2:
        order = DESC

    if sort_point == 1:
        sort_computers_by_id(computers, order)
    elif sort_point == 2:
        sort_computers_by_price(computers, order)
    elif sort_point == 3:
        sort_computers_by_ram(computers, order)
    elif sort_point == 4:
        sort_computers_by_ssd(computers, order)


def process_find_menu(computers: list[Computer]) -> None:
    print("Выберите параметр поиска")

    print("1. Производитель")
    print("2. Процессор")
    print("3. Видеокарта")

    find_point = input_int("Выберите пункт меню: ", 1, 3)

    finded_computers: list[Computer] = []

    if find_point == 1:
        manufacturer = input_str("Введите название производителя: ", MANUFACTURER_MIN_LEN, MANUFACTURER_MAX_LEN)
        finded_computers = get_computers_by_manufacturer(computers, manufacturer)
    elif find_point == 2:
        processor = input_str("Введите название процессора: ", PROCESSOR_MIN_LEN, PROCESSOR_MAX_LEN)
        finded_computers = get_computers_by_processor(computers, processor)
    elif find_point == 3:
        video_card = input_str("Введите название видеокарты: ", VIDEO_CARD_MIN_LEN, VIDEO_CARD_MAX_LEN)
        finded_computers = get_computers_by_video_card(computers, video_card)

    print_computers(finded_computers)


def print_main_menu() -> None:
    print("\n============\n")

    print("======МЕНЮ======")
    print("1. Добавить новый компьютер в список")
    print("2. Удалить компьютер из списка по ИД")
    print("3. Сохранить список компьютеров в человекочитаемый файл")
    print("4. Сохранить список компьютеров в машиночитаемый файл")
    print("5. Загрузить список компьютеров из машиночитаемого файла")
    print("6. Обновить информацию о компьютере по ИД")
    print("7. Обновить количество на складе по ИД")
    print("8. Увеличить ОЗУ у компьютера по ИД")
    print("9. Выставить компьютер на распродажу (10%) по ИД")
    print("10. Отсортировать список компьютеров по ...")
    print("11. Найти компьютеры по ...")
    print("12. Вывести компьютер по ИД")
    print("13. Вывести самый дорогой и самый дешевый компьютер")
    print("14. Найти компьютеры по мощности видеокарты")
    print("0. Выйти из программы")


computers: list[Computer] = []


computers.append(Computer(1, "Dell", "Intel i5", "GTX 1650", 8, 512, 2000, 50000, 5))
computers.append(Computer(2, "HP", "AMD Ryzen 7", "RTX 3060", 16, 1000, 2500, 120000, 3))
GLOBAL_COMPUTER_ID = 2

is_run = True
while is_run == True:
    clear_console()

    print_computers(computers)

    print_main_menu()

    menu_point = input_int("Выберите пункт меню: ", 0, 14)

    if menu_point == 1:
        process_add_computer_menu(computers)
    elif menu_point == 2:
        process_delete_computer_menu(computers)
    elif menu_point == 3:
        process_save_human_menu(computers)
    elif menu_point == 4:
        process_save_computer_menu(computers)
    elif menu_point == 5:
        computers = process_load_computer_menu()
    elif menu_point == 6:
        process_change_information_menu(computers)
    elif menu_point == 7:
        process_change_amount_menu(computers)
    elif menu_point == 8:
        process_increase_ram_menu(computers)
    elif menu_point == 9:
        process_set_sale_menu(computers)
    elif menu_point == 10:
        process_sort_menu(computers)
    elif menu_point == 11:
        process_find_menu(computers)
    elif menu_point == 12:
        process_print_computer_by_id_menu(computers)
    elif menu_point == 13:
        process_min_max_price_menu(computers)
    elif menu_point == 14:
        process_sort_by_video_card_menu(computers)
    elif menu_point == 0:
        is_run = process_exit_menu()
    input()