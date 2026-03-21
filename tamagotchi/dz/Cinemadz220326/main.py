from Movie import Movie
from Session import Session
from Cinema import Cinema

cinema = Cinema("Кинотеатр")

movie1 = Movie("Интерстеллар", 169, 16)
movie2 = Movie("Оппенгеймер", 180, 18)

cinema.add_session(Session(movie1, "18:30", 350, 30))
cinema.add_session(Session(movie1, "21:45", 400, 30))
cinema.add_session(Session(movie2, "19:00", 450, 25))

while True:
    print("\n=== Меню ===")
    print("1. Показать все сеансы")
    print("2. Посмотреть свободные места на сеансе")
    print("3. Забронировать место")
    print("4. Отменить бронь")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        sessions_info = cinema.show_sessions()
        if sessions_info:
            for info in sessions_info:
                print(info)
        else:
            print("Нет доступных сеансов")

    elif choice == "2":
        sessions_info = cinema.show_sessions()
        if not sessions_info:
            print("Нет доступных сеансов")
            continue

        for info in sessions_info:
            print(info)

        try:
            session_num = int(input("\nВведите номер сеанса: "))
            session = cinema.find_session_by_number(session_num)
            if session:
                free_seats = session.show_free_seats()
                if free_seats:
                    print(f"Свободные места: {free_seats}")
                else:
                    print("Свободных мест нет")
            else:
                print("Сеанс не найден")
        except ValueError:
            print("Ошибка. Введите число")

    elif choice == "3":
        sessions_info = cinema.show_sessions()
        if not sessions_info:
            print("Нет доступных сеансов")
            continue

        for info in sessions_info:
            print(info)

        try:
            session_num = int(input("\nВведите номер сеанса: "))
            seat_num = int(input("Введите номер места: "))

            if cinema.book_ticket(session_num, seat_num):
                print(f"Место {seat_num} успешно забронировано")
            else:
                print("Ошибка. Место не существует или уже занято")
        except ValueError:
            print("Ошибка. Введите число")

    elif choice == "4":
        sessions_info = cinema.show_sessions()
        if not sessions_info:
            print("Нет доступных сеансов")
            continue

        for info in sessions_info:
            print(info)

        try:
            session_num = int(input("\nВведите номер сеанса: "))
            seat_num = int(input("Введите номер места: "))

            if cinema.cancel_ticket(session_num, seat_num):
                print(f"Бронь места {seat_num} отменена")
            else:
                print("Ошибка. Место не существует или не было забронировано")
        except ValueError:
            print("Ошибка. Введите число")

    elif choice == "5":
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова")