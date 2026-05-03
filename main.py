from participant import Participant
from captain import Captain
from tournament import Tournament


def main():
    tournament = Tournament()

    while True:
        print("\n1. Добавить обычного участника")
        print("2. Добавить капитана команды")
        print("3. Просмотр всех участников")
        print("4. Начислить баллы участнику")
        print("5. Снять баллы участника")
        print("6. Показать рейтинг")
        print("7. Определить победителя")
        print("8. Показать debug информацию")
        print("9. Показать количество участников")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            print("\n--- Добавление обычного участника ---")
            name = input("Введите имя: ")
            school_class = input("Введите класс: ")
            participant = Participant(name, school_class)
            tournament.add_participant(participant)
            print(f"Участник {name} добавлен!")

        elif choice == "2":
            print("\n--- Добавление капитана команды ---")
            name = input("Введите имя: ")
            school_class = input("Введите класс: ")
            team_name = input("Введите название команды: ")
            captain = Captain(name, school_class, team_name)
            tournament.add_participant(captain)
            print(f"Капитан {name} команды {team_name} добавлен!")

        elif choice == "3":
            print("\n--- Список участников ---")
            tournament.show_participants()

        elif choice == "4":
            print("\n--- Начисление баллов ---")
            name = input("Введите имя участника: ")
            points = int(input("Введите количество баллов: "))
            tournament.add_points_to_participant(name, points)

        elif choice == "5":
            print("\n--- Снятие баллов ---")
            name = input("Введите имя участника: ")
            points = int(input("Введите количество баллов для снятия: "))
            tournament.remove_points_from_participant(name, points)

        elif choice == "6":
            tournament.show_rating()

        elif choice == "7":
            tournament.get_winner()

        elif choice == "8":
            tournament.show_debug_info()

        elif choice == "9":
            print(f"Количество участников: {len(tournament)}")

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова!")


if __name__ == "__main__":
    main()