board = {
    '0': ' ', '1': ' ', '2': ' ',
    '3': ' ', '4': ' ', '5': ' ',
    '6': ' ', '7': ' ', '8': ' '
}

player = 1          # to initialise first player
total_moves = 0     # to count the moves
end_check = 0


def check():
    # checking the moves of player one
    # for horizontal(start)
    if board['0'] == 'X' and board['1'] == 'X' and board['2'] == 'X':
        print('Player one won !')
        return 1
    if board['3'] == 'X' and board['4'] == 'X' and board['5'] == 'X':
        print('Player One Won!!')
        return 1
    if board['6'] == 'X' and board['7'] == 'X' and board['8'] == 'X':
        print('Player One Won!!')
        return 1
    # for horizontal(end)
    # for diagonal(start)
    if board['1'] == 'X' and board['4'] == 'X' and board['8'] == 'X':
        print('Player One Won!!')
        return 1
    # for diagonal(end)
    # for vertical(start)
    if board['0'] == 'X' and board['3'] == 'X' and board['6'] == 'X':
        print('Player One Won!!')
        return 1
    if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Player One Won!!')
        return 1
    if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Player One Won!!')
        return 1
    # for vertical(end)

    # checking the moves of player two
    if board['0'] == 'O' and board['1'] == 'O' and board['2'] == 'O':
        print('Player Two Won!!')
        return 1  # used to end the game
    if board['3'] == 'O' and board['4'] == 'O' and board['5'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['6'] == 'O' and board['7'] == 'O' and board['8'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['0'] == 'O' and board['4'] == 'O' and board['8'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['0'] == 'O' and board['3'] == 'O' and board['6'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0


print('0|1|2')
print('- +- +-')
print('3|4|5')
print('- +- +-')
print('6|7|8')
print('***************************')

while True:
    print(board['0']+'|'+board['1']+'|'+board['2'])
    print('-+-+-')
    print(board['3'] + '|' + board['4'] + '|' + board['5'])
    print('-+-+-')
    print(board['6'] + '|' + board['7'] + '|' + board['8'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     # input from players
        if player == 1:  # choose player
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            # on wrong input
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:  # on wrong input
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print('***************************')
    print()



#Tic_Tac_Toe

