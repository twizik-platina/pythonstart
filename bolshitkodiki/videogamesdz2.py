
from dataclasses import dataclass

@dataclass
class Game:
    id: int
    title: str
    genre: str
    platform: str
    age_rating: int
    price: int
    player_rating: float
    status: str
    copies: int

games = []
next_id = 1


def search_games(games_list):
    print("ПОИСК ИГР")

    substring = input("Часть названия: ")
    substring = substring.lower()
    
    found = False
    
    for game in games_list:
        if substring in game.title.lower():
            print(f"ID {game.id}: {game.title} - {game.genre}, {game.platform}, {game.price}руб.")
            found = True
    
    if not found:
        print("Игры не найдены")


def filter_games(games_list):
    print("ФИЛЬТР")
    print("1 - по возрастному рейтингу")
    print("2 - по платформе")
    
    choice = input("Выберите: ")

    if choice == "1":
        max_age = input("Максимальный возрастной рейтинг: ")
        max_age = int(max_age)
        
        for game in games_list:
            if game.age_rating <= max_age:
                print(f"ID {game.id}: {game.title} - {game.age_rating}+")
    

    elif choice == "2":
        platform = input("Платформа: ")
        platform = platform.lower()
        
        for game in games_list:
            if game.platform.lower() == platform:
                print(f"ID {game.id}: {game.title} - {game.genre}, {game.age_rating}+")
    else:
        print("Отмена")


def sort_games(games_list):
    print("СОРТИРОВКА")
    print("1 - по оценке игроков (от лучших к худшим)")
    print("2 - по оценке игроков (от худших к лучшим)")
    print("3 - по названию (А-Я)")
    print("4 - по названию (Я-А)")
    
    choice = input("Выберите: ")
    
    if choice == "1":
        for i in range(len(games_list)):
            for j in range(i + 1, len(games_list)):
                if games_list[j].player_rating > games_list[i].player_rating:
                    temp = games_list[i]
                    games_list[i] = games_list[j]
                    games_list[j] = temp
    
    elif choice == "2":
        for i in range(len(games_list)):
            for j in range(i + 1, len(games_list)):
                if games_list[j].player_rating < games_list[i].player_rating:
                    temp = games_list[i]
                    games_list[i] = games_list[j]
                    games_list[j] = temp

    elif choice == "3":
        for i in range(len(games_list)):
            for j in range(i + 1, len(games_list)):
                if games_list[j].title.lower() < games_list[i].title.lower():
                    temp = games_list[i]
                    games_list[i] = games_list[j]
                    games_list[j] = temp

    elif choice == "4":
        for i in range(len(games_list)):
            for j in range(i + 1, len(games_list)):
                if games_list[j].title.lower() > games_list[i].title.lower():
                    temp = games_list[i]
                    games_list[i] = games_list[j]
                    games_list[j] = temp


    else:
        print("Отмена")
        return games_list

    print("ОТСОРТИРОВАННЫЙ СПИСОК:")
    for game in games_list:
        print(f"ID {game.id}: {game.title} - Оценка: {game.player_rating}, Платформа: {game.platform}")
    
    return games_list

def change_price_by_genre(genre,new_sale):
    for i in range(len(games)):
        if games[i].genre==genre:
            games[i].price*=(int(new_sale[:-1])/100)

def find_average_price():
    k=0
    summ=0

    for i in range(len(games)):
        summ+=games[i].price
        k+=1
    return summ/k

def find_max_player_rating():
    max=games[0].player_rating
    for i in range(len(games)):
        if max<games[i].player_rating:
            max=games[i].player_rating
            game=games[i]
    return game

def set_hit_flag():
    for i in range(len(games)):
        if games[i].player_rating >= 8.5:
            games[i].status="hit"

def del_null_copies_games():
    for i in range(len(games)):
        if games[i].copies==0:
            games.pop(i)

def count_number_copies():
    for i in range(len(games)):
        num+=games[i].copies
    return num

def sort_games_by_price(game_price):
    for i in range(len(games)):
        if games[i].price<game_price:
            print(games[i])

def increase_age_rating_by_id(game_id,new_age_rating):
    for i in range(len(games)):
        if games[i].id==game_id:
            games[i].age_rating=new_age_rating
            break

def get_unique_genres():
    genres=[]
    for i in range(len(games)):
        if games[i].genre not in genres:
            genres.append(games[i].genre)
    return genres

def check_hit_status():
    for i in range(len(games)):
        if games[i].status=="hit":
            return True
    return False

def add_game_to_list():
    global next_id
    
    print("Добавление игры:")
    name = input("Название: ")
    genre = input("Жанр: ")
    platform = input("Платформа: ")
    age_rating = int(input("Возрастной рейтинг: "))
    price = int(input("Цена: "))
    player_rating = float(input("Оценка игроков: "))
    status = input("Статус: ")
    amount = int(input("Количество копий: "))
    
    game = Game(next_id, name, genre, platform, age_rating, price, player_rating, status, amount)
    games.append(game)
    next_id += 1
    print(f"Добавлен компьютер ID {game.id}")

while True:
    print("УПРАВЛЕНИЕ ИГРАМИ")
    print("1. поиск игр по части названия (подстрока)")
    print("2. фильтрация игр")
    print("3. сортировка игр")
    print("4. изменить цену всех игр выбранного жанра (например, скидка −20%)")
    print("5. подсчитать среднюю цену всех игр")
    print("6. найти игру с максимальной оценкой")
    print("7. пометить игру как «хит», если оценка ≥ 8.5")
    print("8. удалить все игры, у которых количество копий равно 0")
    print("9. подсчитать общее количество копий всех игр")
    print("10. вывести список игр дешевле указанной суммы")
    print("11. увеличить возрастной рейтинг игры по ИД")
    print("12. вывести все уникальные жанры, присутствующие в списке")
    print("13. проверить, есть ли игры со статусом «хит»")
    print("14. добавить игру")
    print("0. Выход")
    
    choice = input("Выберите: ")
    
    if choice == "1":
        search_games()
        input()
    elif choice == "2":
        filter_games()
        input()
    elif choice == "3":
        sort_games()
        input()
    elif choice == "4":
        change_price_by_genre(input("Введите жанр игры: "),input("Введите скидку: "))
        input()
    elif choice == "5":
        print(f"Средняя цена: {find_average_price()}")
        input()
    elif choice == "6":
        print(find_max_player_rating())
        input()
    elif choice == "7":
        set_hit_flag()
        input()
    elif choice == "8":
        del_null_copies_games()
        input()
    elif choice == "9":
        print(count_number_copies())
        input()
    elif choice == "10":
        sort_games_by_price(input("Введите цену: "))
        input()
    elif choice == "11":
        increase_age_rating_by_id(input("Введите id: "),input("Введите новую цену: "))
        input()
    elif choice == "12":
        print(get_unique_genres())
        input()
    elif choice == "13":
        if check_hit_status() == True:
            print("В списке есть игры с хит статусом")
        else:
            print("В списке нет игры с хит статусом")
        input()
    elif choice == "14":
        add_game_to_list()
    elif choice == "0":
        print("Выход")
        break
    else:
        print("Неверный выбор")
        input()
