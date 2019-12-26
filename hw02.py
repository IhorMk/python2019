import random

board = list(range(1, 10))
def gameboard(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
def move_input(badge):
    valid = False
    while not valid:
        player_move = input ("Where to put: " + badge+"? ")
        try:
            player_move = int(player_move)
        except:
            print ("Invalid input. Are you sure you entered the number?")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(board[player_move-1]) not in "XO"):
                board[player_move-1] = badge
                valid = True
            else:
                print ("This box is already taken")
        else:
            print ("Invalid input. Enter a valid number from 1 to 9")
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        gameboard(board)
        if counter % 2 == 0:
            move_input("X")
        else:
            move_input("0")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "WIN!")
                win = True
                break
        if counter == 9:
            print ("You played a draw!")
            break
main(board)