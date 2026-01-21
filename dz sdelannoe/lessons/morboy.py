import random


ALIVE_SHIP = "K"
DEAD_SHIP = "X"
MISS_CELL = "O"
EMPTY_CELL = "."

COLS = 10
ROWS = 10

COUNT_SHIPS = 10

USER_STEP = "USER"
COMP_STEP = "COMP"

USER_WINNER = "USER"
COMP_WINNER = "COMP"

def create_empty_field():

    field = []
    for i in range(ROWS):
        field.append([])
        for j in range(COLS):
            field[i].append(EMPTY_CELL)
    return field

def place_ships_randomly(field):

    ships_placed = 0
    while ships_placed < COUNT_SHIPS:
        i_rand = random.randint(0, ROWS - 1)
        j_rand = random.randint(0, COLS - 1)
        
        if field[i_rand][j_rand] == EMPTY_CELL:
            field[i_rand][j_rand] = ALIVE_SHIP
            ships_placed += 1
    return field

def print_fields(user_field, comp_field, show_comp_ships=False):

    print("\nПоле человека:")
    for i in range(ROWS):
        for j in range(COLS):
            print(user_field[i][j], end=" ")
        print()

    print("\nПоле компьютера:")
    for i in range(ROWS):
        for j in range(COLS):
            if comp_field[i][j] == ALIVE_SHIP and not show_comp_ships:
                print(EMPTY_CELL, end=" ")
            else:
                print(comp_field[i][j], end=" ")
        print()