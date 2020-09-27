import random
import math

board = [i for i in range(9)]
last_move = None

def draw():
    for i in range(3):
        print(board[i * 3], '|', board[i * 3 + 1], '|', board[i* 3 + 2])
        print('-' * 10)

def check(item, board):
    if board[0] == board[1] == board[2] == item or board[3] == board[4] == board[5] == item or board[6] == board[7] == board[8] == item: return True
    elif board[0] == board[3] == board[6] == item or board[1] == board[4] == board[7] == item or board[2] == board[5] == board[8] == item: return True
    elif board[0] == board[4] == board[8] == item or board[2] == board[4] == board[6] == item: return True
    return False

def long_check(board):
    if check('X', board): return 'human'
    elif check('O', board): return 'ai'
    elif len(possible_moves(board)) == 0: return 'draw'
    return None

def end():
    if long_check(board) != None: draw()
    if long_check(board) == 'human': print('You have won!')
    elif long_check(board) == 'ai': print('You have lost!')
    elif long_check(board) == 'draw': print('Draw!')
    return long_check(board) != None

def possible_moves(board):
    return [i for i in range(9) if type(board[i]) is int]

def make_best_move():
    best_score = -math.inf
    best_move = None
    for move in possible_moves(board):
        board[move] = 'O'
        score = minimax(False, board)
        board[move] = move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def minimax(is_max_turn, board):
    if long_check(board) == 'draw': return 0
    elif long_check(board) == 'ai': return 1
    elif long_check(board) == 'human': return -1
    if is_max_turn: player = 'O'
    else: player = 'X'
    scores = []
    for move in possible_moves(board):
        board[move] = player
        scores.append(minimax(not is_max_turn, board))
        board[move] = move
    return max(scores) if is_max_turn else min(scores)

while True:
    draw()
    while True:
        turn = int(input('Your move: '))
        if type(board[turn]) is int:
            board[turn] = 'X'
            break
        print('Incorrect move, try again!')
    if end(): break
    board[make_best_move()] = 'O'
    if end(): break
