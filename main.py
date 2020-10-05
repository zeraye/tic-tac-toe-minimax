import random
import math

board = [i for i in range(9)]

def draw():
    for i in range(3):
        print(board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2])
        print('-' * 10)

def check(board, player):
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player or board[i] == board[i + 3] == board[i + 6] == player: return True
    return True if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player else False

def exact_check(board):
    if check(board, 'O'): return -1
    elif check(board, 'X'): return 1
    return None if check(board, 'O') == check(board, 'X') else 0

def possible_moves(board):
    return [i for i in range(9) if type(board[i]) is int]

def make_best_move():
    best_score = -math.inf
    best_move = None
    for move in possible_moves(board):
        board[move] = 'X'
        score = minimax(True, board)
        print('move ', move, ' -> score', score)
        board[move] = move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax(is_max, board):
    if exact_check(board) != None: return exact_check(board)
    player = 'O' if is_max else 'X'

    score = []

    if is_max:
        max_eval = -math.inf
        for move in possible_moves(board):
            board[move] = player
            eval = minimax(not is_max, board)
            board[move] = move
            max_eval = max(max_eval, eval)
        score.append(max_eval)
        # return max_eval
    else:
        min_eval = math.inf
        for move in possible_moves(board):
            board[move] = player
            eval = minimax(not is_max, board)
            board[move] = move
            min_eval = min(min_eval, eval)
        score.append(min_eval)
        # return min_eval

    return max(score) if is_max else min(score)

while True:
    if exact_check(board) != None: break
    draw()

    turn = int(input('Your move: '))
    board[turn] = 'O'

    if exact_check(board) != None: break

    board[make_best_move()] = 'X'

draw()
