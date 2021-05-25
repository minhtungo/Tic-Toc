import random
board = [' ']*10

def display_board():
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input(turn):
    maker = ''
    while (maker != 'X' and maker != 'O'):
        maker = input(f"{turn}, choose X or O: ").upper()
    if maker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def get_turn():
    turn = random.randint(0,2)
    if (turn == 0):
        return "Player1"
    else:
        return "Player2"

def check_position(position):
    return board[position] == ' '


def check_result():
    return (board[1] != ' ' and board[1] == board[2] and board[2] == board[3]) or (board[4] != ' ' and board[4] == board[5] and board[5] == board[6]) or (board[7] != ' ' and board[7] == board[8] and board[8] == board[9]) or (board[3] != ' ' and board[3] == board[5] and board[5] == board[7]) or (board[1] != ' ' and board[1] == board[5] and board[5] == board[9]) or (board[1] != ' ' and board[1] == board[4] and board[4] == board[7]) or (board[2] != ' ' and board[2] == board[5] and board[5] == board[8]) or (board[3] != ' ' and board[3] == board[6] and board[6] == board[9])

def place_maker():
    global board
    count = 0
    turn = get_turn()
    if turn == "Player1":
        mark1, mark2 = player_input(turn)
    else:
        mark2, mark1 = player_input(turn)
    position = 0
    while True:
        if turn == "Player1":
            while position not in (1, 2, 3, 4, 5 ,6 ,7 ,8 ,9):
                position = int(input("Player 1, choose a position from 1 to 9: "))
            while not check_position(position):
                position = int(input(f"{position} was chosen. Please pick another position: "))
            board[position] = mark1
            turn = "Player2"
        else:
            while position not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                position = int(input("Player 2, choose a position from 1 to 9: "))
            while not check_position(position):
                position = int(input(f"{position} was chosen. Please pick another position: "))
            board[position] = mark2
            turn = "Player1"
        position = 0
        count += 1
        display_board()
        if count > 4:
            if check_result():
                if board[position] == mark1:
                    print("Player 1 win")
                else:
                    print("Player 2 win")
                break
            elif (count == 9):
                print("No one win. Start a new match.")
                break

def play_again():
    answer = input("Do you want to start a new match: ").upper()
    return answer == 'Y'

if (__name__ =="__main__"):
    while True:
        display_board()
        place_maker()
        if play_again():
                board = [' ']*10
        else:
            break


