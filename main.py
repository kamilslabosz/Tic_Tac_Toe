game_board = []

move_count = 0


def tictactoe():
    global game_board
    game_board = [" ", " ", " "], \
                 [" ", " ", " "], \
                 [" ", " ", " "]
    print("\nWelcome to tic tac toe!\nLet's play. First symbol is X.")
    global move_count
    move_count = 1
    place_mark(move_count)


def print_board():
    print("  A   B   C")
    print(f"1 {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} ")
    print(" -----------")
    print(f"2 {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} ")
    print(" -----------")
    print(f"3 {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} ")


def place_mark(mark):

    if mark % 2 == 0:
        player = "2nd player"
    else:
        player = "1st player"

    print_board()
    where = input(f"{player}, where do you want do place your mark? (e.g. B1, C2): ").upper()
    y = mark_y(where[0])
    x = mark_x(where[1])

    if mark % 2 == 0:
        game_board[x][y] = "O"
    else:
        game_board[x][y] = "X"

    if check_win():
        print_board()
        print(f"Congratulations {player}, you won!")
        should_continue = input("Want to play again? Y or N?: ").upper()
        if should_continue == 'Y':
            tictactoe()
    else:
        mark += 1
        place_mark(mark)


def mark_x(x):
    if x == '1':
        return 0
    elif x == '2':
        return 1
    elif x == '3':
        return 2


def mark_y(y):

    if y == 'A':
        return 0
    elif y == 'B':
        return 1
    elif y == 'C':
        return 2


def check_win():

    for row in game_board:
        if row[0] == row[1] == row[2] != " ":
            return True

    if game_board[0][0] == game_board[1][1] == game_board[2][2] != " " \
            or game_board[0][2] == game_board[1][1] == game_board[2][0] != " ":
        return True

    elif game_board[0][0] == game_board[1][0] == game_board[2][0] != " " \
            or game_board[0][1] == game_board[1][1] == game_board[2][1] != " " \
            or game_board[0][2] == game_board[1][2] == game_board[2][2] != " ":
        return True

    else:
        return False


tictactoe()
