'''
Oliver E.
9-23
t - t - t
fun words
'''

print("Play the game, I promise I won't brutally murder you if you don't.")

import random

try:
    player_choice = input("What would you like to be (please choose one character)?")
    print("Great you are", player_choice)
    if player_choice == "X" or "x":
        computer_choice = "O"
    else:
        computer_choice = "X"
    print("The computer is", computer_choice)
except:
    print("Learn your letters.")
    print("Please choose X or O.")

# this is the board 2d-array
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
win_x = [["X","X","X"],["X","X","X"],["X","X","X"]]
win_O = [["O","O","O"],["O","O","O"],["O","O","O"]]
player_win1 = [[player_choice, player_choice, player_choice],[player_choice, player_choice, player_choice],[player_choice, player_choice, player_choice]]

def print_board():
    print("columns 0    1    2")
    print("Row-0",board[0])
    print("Row-1",board[1])
    print("Row-2",board[2])

def computer_move():
    ran_choice_row = random.randint(0,2)
    ran_choice_column = random.randint(0, 2)

    if board[ran_choice_row][ran_choice_column] == "_":
        board[ran_choice_row][ran_choice_column] = computer_choice
        print_board()
    else:
        computer_move()

def user_move():
    user_choice_row = input("What row would you like?")
    user_choice_column = input("What column would you like?")
    int_user_choice_row = int(user_choice_row)
    int_user_choice_column = int(user_choice_column)
    if board[int_user_choice_row][int_user_choice_column] == "_":
        board[int_user_choice_row][int_user_choice_column] = player_choice
        print_board()
    else:
        print("Pick again.")
        user_move()

def gameplay():
    while True:
        computer_move()
        if win_x[0] == board[0]:
            print(computer_choice, "wins")
            break
        if win_x[1] == board[1]:
            print(computer_choice, "wins")
            break
        if win_x[2] == board[2]:
            print(computer_choice, "wins")
            break
        if win_O[0] == board[0]:
            print(computer_choice, "wins")
            break
        if win_O[1] == board[1]:
            print(computer_choice, "wins")
            break
        if win_O[2] == board[2]:
            print(computer_choice, "wins")
            break
        if (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0]) == "X":
            print(computer_choice, "wins")
            break
        if (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1]) == "X":
            print(computer_choice, "wins")
            break
        if (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2]) == "X":
            print(computer_choice, "wins")
            break
        if (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0]) == "O":
            print(computer_choice, "wins")
            break
        if (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1]) == "O":
            print(computer_choice, "wins")
            break
        if (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2]) == "O":
            print(computer_choice, "wins")
            break
        if (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2]) == "X":
            print(computer_choice, "wins")
            break
        if (board[0][2] == "X") and (board[1][1] == "X") and (board[2][0]) == "X":
            print(computer_choice, "wins")
            break
        if (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2]) == "O":
            print(computer_choice, "wins")
            break
        if (board[0][2] == "O") and (board[1][1] == "O") and (board[2][0]) == "O":
            print(computer_choice, "wins")
            break
        user_move()
        if player_win1[0] == board[0]:
            print(player_choice, "wins")
            break
        if player_win1[1] == board[1]:
            print(player_choice, "wins")
            break
        if player_win1[2] == board[2]:
            print(player_choice, "wins")
            break
        if player_win1[0] == board[0]:
            print(player_choice, "wins")
            break
        if player_win1[1] == board[1]:
            print(player_choice, "wins")
            break
        if player_win1[2] == board[2]:
            print(player_choice, "wins")
            break
        if (board[0][0] == player_choice) and (board[1][0] == player_choice) and (board[2][0]) == player_choice:
            print(player_choice, "wins")
            break
        if (board[0][1] == player_choice) and (board[1][1] == player_choice) and (board[2][1]) == player_choice:
            print(player_choice, "wins")
            break
        if (board[0][2] == player_choice) and (board[1][2] == player_choice) and (board[2][2]) == player_choice:
            print(player_choice, "wins")
            break
        if (board[0][0] == player_choice) and (board[1][0] == player_choice) and (board[2][0]) == player_choice:
            print(player_choice, "wins")
            break
        if (board[1][0] == player_choice) and (board[1][1] == player_choice) and (board[1][2]) == player_choice:
            print(player_choice, "wins")
            break
        if (board[0][0] == player_choice) and (board[1][1] == player_choice) and (board[2][2]) == player_choice:
            print(player_choice, "wins")
            break
        if (board[0][2] == player_choice) and (board[1][1] == player_choice) and (board[2][0]) == player_choice:
            print(player_choice, "wins")
            break
        computer_move()
        user_move()


gameplay()

