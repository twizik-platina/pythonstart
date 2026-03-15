import random


class Robot:
    __energy_level: int
    __parts_level: int
    __is_working: bool

    __MIN_LEVEL = 0
    __MAX_LEVEL = 100

    __MIN_INCREASE = 5
    __MAX_INCREASE = 15

    __MIN_DECREASE = 5
    __MAX_DECREASE = 15

    __EVENT_CHANCE = 30

    def __init__(self):
        self.__energy_level = random.randint(50, 100)
        self.__parts_level = random.randint(50, 100)
        self.__is_working = True

    def charge(self) -> None:
        if not self.__is_working:
            print("Робот не работает и не может заряжаться")
            return

        increase_energy = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)

        self.__energy_level += increase_energy

        if self.__energy_level > self.__MAX_LEVEL:
            self.__energy_level = self.__MAX_LEVEL
            print("Робот полностью заряжен. Уровень энергии максимальный.")

        print(f"Робот заряжен. Энергия увеличена на {increase_energy}.")

    def repair(self) -> None:
        if not self.__is_working:
            print("Робот не работает и не может быть отремонтирован")
            return

        increase_parts = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)

        self.__parts_level += increase_parts

        if self.__parts_level > self.__MAX_LEVEL:
            self.__parts_level = self.__MAX_LEVEL
            print("Робот полностью отремонтирован. Уровень запчастей максимальный.")

        print(f"Робот отремонтирован. Запчасти увеличены на {increase_parts}.")

    def work(self) -> None:
        if not self.__is_working:
            print("Робот сломан и не может работать")
            return

        decrease_energy = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)
        decrease_parts = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)

        self.__energy_level -= decrease_energy
        self.__parts_level -= decrease_parts

        print(f"Робот работает. Потрачено энергии: {decrease_energy}, запчастей: {decrease_parts}")

        if self.__energy_level <= self.__MIN_LEVEL:
            self.__energy_level = self.__MIN_LEVEL
            self.__is_working = False
            print("Энергия закончилась. Робот перестал работать.")

        if self.__parts_level <= self.__MIN_LEVEL:
            self.__parts_level = self.__MIN_LEVEL
            self.__is_working = False
            print("Запчасти закончились. Робот перестал работать.")

    def random_event(self) -> None:
        event_percent = random.randint(1, 100)
        if 1 <= event_percent <= self.__EVENT_CHANCE:
            event_number = random.randint(1, 2)

            if event_number == 1:
                self.__is_working = False
                print("Робот сломался! Он больше не работает.")

            elif event_number == 2:
                increase_energy = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)
                self.__energy_level += increase_energy

                if self.__energy_level > self.__MAX_LEVEL:
                    self.__energy_level = self.__MAX_LEVEL

                print(f"Робот нашёл дополнительную энергию! Энергия увеличена на {increase_energy}.")

    def check_status(self) -> None:
        status = "работает" if self.__is_working else "не работает"

        def format_level(level: int) -> str:
            filled = "■" * (level // 10)
            empty = "□" * (10 - (level // 10))
            return f"[{filled}{empty}] ({level})"

        print(
            f"Состояние робота: {status}\n"
            f"Уровень энергии: {format_level(self.__energy_level)}\n"
            f"Уровень запчастей: {format_level(self.__parts_level)}"
        )