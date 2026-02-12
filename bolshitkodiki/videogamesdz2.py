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
