#1. Cоздание игрогого поля (перед этим импорт рандом, введение переменных и т.п нужной хрени)
#1.2 Определение, кто первый ходит на рандом

#2 Отображение поля
#2.1 Отобразить, кто ходит(если пк - ентер, если человек, то ввод чисел(строка и столбик)) ---> Проверка на условия победы, ничьи и не поставил ли человек знак в ту же точку, а также не ввел ли какую то хрень(число больше 3 или текстовое сообщение).
#2.2 Если кто-то выигрывает, то вывод поля и сообщения с поздравлениями

import random

PLAYER_SIGN = "X"
COMP_SIGN = "O"
EMPTY_CELL = "."

ROWS = 3
COLS = 3

PLAYER_TURN = "PLAYER"
COMP_TURN = "COMP"

PLAYER_WINNER = "PLAYER"
COMP_WINNER = "COMP"

field = []

for i in range(ROWS):
    field.append([])
    for j in range(COLS):
        field[i].append(EMPTY_CELL)

if random.randint(1, 2) == 1:
    current_turn = PLAYER_TURN
    print("Вы ходите первыми (X)")
else:
    current_turn = COMP_TURN
    print("Компьютер ходит первым (X)")

game_is_running = True
winner = ""

while game_is_running == True:

    print()
    for i in range(ROWS):
        for j in range(COLS):
            print(field[i][j], end=" ")
        print()

    winner_found = False

    for i in range(ROWS):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != EMPTY_CELL:
            winner_found = True
            winner = PLAYER_WINNER if field[i][0] == PLAYER_SIGN else COMP_WINNER

    if not winner_found:
        for j in range(COLS):
            if field[0][j] == field[1][j] == field[2][j] and field[0][j] != EMPTY_CELL:
                winner_found = True
                winner = PLAYER_WINNER if field[0][j] == PLAYER_SIGN else COMP_WINNER

    if not winner_found:
        if field[0][0] == field[1][1] == field[2][2] and field[0][0] != EMPTY_CELL:
            winner_found = True
            winner = PLAYER_WINNER if field[0][0] == PLAYER_SIGN else COMP_WINNER

    if not winner_found:
        if field[0][2] == field[1][1] == field[2][0] and field[0][2] != EMPTY_CELL:
            winner_found = True
            winner = PLAYER_WINNER if field[0][2] == PLAYER_SIGN else COMP_WINNER

    if not winner_found:
        empty_exists = False
        for i in range(ROWS):
            for j in range(COLS):
                if field[i][j] == EMPTY_CELL:
                    empty_exists = True
                    break
            if empty_exists:
                break
        
        if not empty_exists:
            winner_found = True

    if winner_found == True:
        game_is_running = False
        continue

    if current_turn == PLAYER_TURN:
        print("Ваш ход (вы играете X):")

        correct_input = False
        while correct_input == False:
            i_input = int(input("Введите номер строки (1-3): ")) - 1
            j_input = int(input("Введите номер столбца (1-3): ")) - 1

            if 0 <= i_input < ROWS and 0 <= j_input < COLS:
                if field[i_input][j_input] == EMPTY_CELL:
                    field[i_input][j_input] = PLAYER_SIGN
                    correct_input = True
                    current_turn = COMP_TURN
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Ошибка! Введите числа от 1 до 3!")

    elif current_turn == COMP_TURN:
        print("Ход компьютера (нажмите Enter):")
        input()

        empty_cells = []
        for i in range(ROWS):
            for j in range(COLS):
                if field[i][j] == EMPTY_CELL:
                    empty_cells.append((i, j))

        if empty_cells:
            i_rand, j_rand = random.choice(empty_cells)
            field[i_rand][j_rand] = COMP_SIGN

        current_turn = PLAYER_TURN

print()
for i in range(ROWS):
    for j in range(COLS):
        print(field[i][j], end=" ")
    print()

if winner == PLAYER_WINNER:
    print("Поставили компьютер на место. Красавец/ица!")
    print("Жертвы этого проекта: 7 чашек кофе, 3 бутылки чая, 1 тетрадь по алгебре, 4 клавиши Enter и нервная система Тимы. Питон еб#т мозги не по детски...")
elif winner == COMP_WINNER:
    print("Совсем дурак, тебя компьютер обыграл в крести-нолики. Фууу")
    print("Жертвы этого проекта: 7 чашек кофе, 3 бутылки чая, 1 тетрадь по алгебре, 4 клавиши Enter и нервная система Тимы. Питон еб#т мозги не по детски...")
else:
    print("Два дебила - это сила")
    print("Жертвы этого проекта: 7 чашек кофе, 3 бутылки чая, 1 тетрадь по алгебре, 4 клавиши Enter и нервная система Тимы. Питон еб#т мозги не по детски...")