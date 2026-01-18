import random

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = "."

ROWS = 3
COLS = 3

HUMAN_TURN = "ЧЕЛОВЕК"
COMPUTER_TURN = "КОМПЬЮТЕР"

HUMAN_WINS = "ЧЕЛОВЕК"
COMPUTER_WINS = "КОМПЬЮТЕР"
NO_WINNER = "НИЧЬЯ"

def main():
    board = []
    for i in range(ROWS):
        board.append([])
        for j in range(COLS):
            board[i].append(EMPTY)

    if random.randint(1, 100) <= 50:
        current_turn = HUMAN_TURN
        human_sign = PLAYER_X
        computer_sign = PLAYER_O
        print("Вы ходите первыми (X)")
    else:
        current_turn = COMPUTER_TURN
        computer_sign = PLAYER_X
        human_sign = PLAYER_O
        print("Компьютер ходит первым (X)")

    game_active = True
    winner = NO_WINNER
    moves_count = 0

    while game_active:
        print()
        for i in range(ROWS):
            print(" ".join(board[i]))

        if current_turn == HUMAN_TURN:
            print(f"Ваш ход (вы играете {human_sign}):")
            
            valid_move = False
            while not valid_move:
                try:
                    row = int(input("Введите номер строки (1-3): ")) - 1
                    col = int(input("Введите номер столбца (1-3): ")) - 1
                    
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                        print("Ошибка! Введите числа от 1 до 3!")
                    elif board[row][col] != EMPTY:
                        print("Эта клетка уже занята! Выберите другую.")
                    else:
                        valid_move = True
                except ValueError:
                    print("Ошибка! Введите целые числа!")
            
            board[row][col] = human_sign
            moves_count += 1
            current_turn = COMPUTER_TURN
        
        else:
            print("Ход компьютера (нажмите Enter)")
            input()
            
            empty_cells = []
            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == EMPTY:
                        empty_cells.append((i, j))
            
            if empty_cells:
                row, col = random.choice(empty_cells)
                board[row][col] = computer_sign
                moves_count += 1
                print(f"Компьютер поставил {computer_sign} в клетку ({row+1}, {col+1})")
            
            current_turn = HUMAN_TURN

        for i in range(ROWS):
            if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
                game_active = False
                if board[i][0] == human_sign:
                    winner = HUMAN_WINS
                else:
                    winner = COMPUTER_WINS

        for j in range(COLS):
            if (board[0][j] == board[1][j] == board[2][j]) and board[0][j] != EMPTY:
                game_active = False
                if board[0][j] == human_sign:
                    winner = HUMAN_WINS
                else:
                    winner = COMPUTER_WINS

        if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
            game_active = False
            if board[0][0] == human_sign:
                winner = HUMAN_WINS
            else:
                winner = COMPUTER_WINS

        if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
            game_active = False
            if board[0][2] == human_sign:
                winner = HUMAN_WINS
            else:
                winner = COMPUTER_WINS

        if moves_count == 9 and game_active:
            game_active = False
            winner = NO_WINNER

    print()
    for i in range(ROWS):
        print(" ".join(board[i]))

    if winner == HUMAN_WINS:
        print("ПОЗДРАВЛЯЮ! ВЫ ПОБЕДИЛИ!")
    elif winner == COMPUTER_WINS:
        print("КОМПЬЮТЕР ПОБЕДИЛ!")
    else:
        print("НИЧЬЯ!")

if __name__ == "__main__":
    main()