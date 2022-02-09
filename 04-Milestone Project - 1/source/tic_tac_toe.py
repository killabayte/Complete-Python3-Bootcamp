import random


def display_board(board):
     print('\n'*10)
     print(board[7]+ "|", board[8] + "|", board[9])
     print("------")
     print(board[4]+ "|", board[5] + "|", board[6])
     print("------")
     print(board[1]+ "|", board[2] + "|", board[3])

def player_input():
    saved_player_input = { "player_one": " ", "player_two": " "}
    while True:
        player_one = input("Player one select the side: X or O: ")
        if player_one == "X":
            saved_player_input["player_one"] = "X"
            saved_player_input["player_two"] = "O"
            return saved_player_input
        elif player_one == "O":
            saved_player_input["player_one"] = "O"
            saved_player_input["player_two"] = "X"
            return saved_player_input
        else:
            print("Wrong input! Input must be X or O")

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

def place_marker(board, marker, position):
    board[int(position)] = marker

def choose_first():
    players_list = ('player_one', 'player_two')
    first_player = players_list[random.randint(0, 1)]
    print(f"Player {first_player} will go first")
    return first_player

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for char in board:
        if char == " ":
            return False
    return True

def player_choice(board):
    while True:
        player_choice = int(input("Next position: "))
        if player_choice in range(1,11):
            if space_check(board, player_choice) is True:
                return player_choice
            else:
                print("This cell is already taken, choose another")
        else:
            print("Board place must be in range between 1-10.")

def replay():
    game_replay = input("Do you want to play one more time? Y or N: ")
    if game_replay in ("Y", "N"):
        if game_replay != "Y":
            return False
        else:
            return True
    else:
        print("Answer must be Y or N\n")
        replay()

def create_new_board():
    board = [" "]*10
    board[0] = "Zero"
    return board

print("Wellcome to Tic Tac Toe!")
while True:

    board = create_new_board()

    current_players = player_input()
    the_first_player = choose_first()
    
    current_marker = current_players[the_first_player]

    game_on = True

    while game_on:
        if full_board_check(board):
            print("Looks like it's a tie. No free cells")
            game_on = replay()
            if game_on:
                board = create_new_board()
                current_players = player_input()
                the_first_player = choose_first()
                current_marker = current_players[the_first_player]
                continue
            else:
                break

        current_move = player_choice(board)
        place_marker(board, current_marker, current_move)
        display_board(board)

        if win_check(board, current_marker):
            print("Congratulations! You win")
            display_board(board)
            game_on = replay()
            if game_on:
                board = create_new_board()
                current_players = player_input()
                the_first_player = choose_first()
                current_marker = current_players[the_first_player]
                continue
            else:
                break

        if current_marker == "X":
            current_marker = "O"
        elif current_marker == "O":
            current_marker = "X"
    break
