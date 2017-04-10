import sys
import time

import math

"""
Problem D. Fashion Show
"""

MP = {
    'o': { '+': 10000, 'x': 100000, 'c': 999, 'point': 2 },
    'x': { '+': 100, 'x': 1000, 'c': 99, 'point': 1 },
    '+': { '+': 1, 'x': 10, 'c': 9, 'point': 1 },
    '.': { '+': 0, 'x': 0, 'c': 0, 'point': 0 }
}

def check(model, r, c, N):
    for i in xrange(N):
        if (model[r][i] == 'o' or model[r][i] == 'x'):
            for j in xrange(N):
                if (model[r][j] in ['o', 'x']):
                    return False
            for j in xrange(N):
                if (model[j][c] in ['o', 'x']):
                    return False
        if (model[r][i] == 'o' or model[r][i] == '+'):

                model[j]) or abs(queen[i] - queen[j]) == j - i:
                return False
    return True


def search(T, queen, n):
    if n == T:
        if check(queen, T):
            return queen
        else:
            return None

    for k in xrange(T):
        queen[n] = k
        nn = search(T, queen, n+1)
        if nn is not None:
            return nn


        def change_board(N, board, r, c, key):
    num = MP[key]['+']
    for k in xrange(N):
        board[r][k] += num
        board[k][c] += num

    num = MP[key]['x']
    if (r > c):
        for k in xrange(N-(r-c)):
            if num > board[k+(r-c)][k]:
                board[k+(r-c)][k] += num
    else:
        for k in xrange(N-(c-r)):
            if num > board[k][k+(c-r)]:
                board[k][k+(c-r)] += num

    if (r+1 < N):
        for k in xrange(r+c+1):
            if num > board[r+c-k][k]:
                board[r+c-k][k] += num
    else:
        for k in xrange(r+c-N+1, N):
            if num > board[r+c-k][k]:
                board[r+c-k][k] += num

    num = MP[key]['c']
    board[r][c] = num

    return board


def search(N, model, board, r, c, total, counter):
    counter += 1
#    if counter > 20:
#        return (model, total)
    if r == N and c == N:
        return (model, total)

    print("r, c", r, c)

    for i in xrange(N):
        for j in xrange(N):

            print(board)
            print(r,c)
            if c == N:
                r += 1
                c = 0

            if r == N:
                return (model, total)


            o_x = False
            o_c = False
            x_x = False
            x_c = False
            c_x = False
            c_c = False

            unit = board[r][c]
            print("unit", unit)

#            if unit % 9 == 0:
#                c += 1
#                continue

            if (board[r][c] / 100000) > 1.0:
                o_x = True
                unit -= math.floor(board[r][c] / 100000)
            if (board[r][c] / 10000) > 1.0:
                o_c = True
                unit -= math.floor(board[r][c] / 10000)
            if (board[r][c] / 1000) > 1.0:
                x_x = True
                unit -= math.floor(board[r][c] / 1000)
            if (board[r][c] / 100) > 1.0:
                x_c = True
                unit -= math.floor(board[r][c] / 100)
            if (board[r][c] / 10) > 1.0:
                c_x = True
                unit -= math.floor(board[r][c] / 10)
            if unit > 0:
                c_c = True

            board_o = list(board)
            board_x = list(board)
            board_c = list(board)
            board_e = list(board)

            if (o_c or o_x):
                changed_model_o = model
                changed_total_o = total
            else:
                key = 'o'
                model[r][c] = key
                board_o = change_board(N, board_o, r, c, key)
                (changed_model_o, changed_total_o) = search(N, model, board_o, r, c+1, total + MP[key]['point'], counter)

            if (x_c):
                changed_model_x = model
                changed_total_x = total
            else:
                key = 'x'
                model[r][c] = key
                board_x = change_board(N, board_x, r, c, key)
                (changed_model_x, changed_total_x) = search(N, model, board_x, r, c+1, total + MP[key]['point'], counter)

            if (c_x):
                changed_model_c = model
                changed_total_c = total
            else:
                key = '+'
                model[r][c] = key
                board_c = change_board(N, board_c, r, c, key)
                (changed_model_c, changed_total_c) = search(N, model, board_c, r, c+1, total + MP[key]['point'], counter)

            key = '.'
            model[r][c] = key
            board_e = change_board(N, board_e, r, c, key)
            (changed_model_e, changed_total_e) = search(N, model, board_e, r, c+1, total + MP[key]['point'], counter)

            print("total:", changed_total_o, changed_total_x, changed_total_c, changed_total_e)
            if changed_total_e >= changed_total_c and changed_total_e >= changed_total_x and changed_total_e >= changed_total_o:
                total = changed_total_e
                model[r][c] = '.'
                board = board_e
                model = changed_model_e

            if changed_total_c >= changed_total_e and changed_total_c >= changed_total_x and changed_total_c >= changed_total_o:
                total = changed_total_c
                model[r][c] = '+'
                board = board_c
                model = changed_model_c

            if changed_total_x >= changed_total_e and changed_total_x >= changed_total_c and changed_total_x >= changed_total_o:
                total = changed_total_x
                model[r][c] = 'x'
                board = board_x
                model = changed_model_x

            if changed_total_o >= changed_total_e and changed_total_o >= changed_total_c and changed_total_o >= changed_total_x:
                total = changed_total_o
                model[r][c] = 'o'
                board = board_o
                model = changed_model_o

            c += 1
    return (model, total)


T = int( raw_input() )
TS = [];
for t in xrange( T ):
    (N, M) = map(int, raw_input().split())
    models = []
    for m in xrange(M):
        (t, r, c) = raw_input().split()
        models.append({
            't': t,
            'r': int(r),
            'c': int(c)
        })
    TS.append({
        'N': N,
        'M': M,
        'ms': models
    })


#----------------------------
start = time.clock()

for t in xrange( T ):

    h = TS[t]
    N = h['N']

    model = [ [ None for _ in xrange(N) ] for _ in xrange(N) ]
    board = [ [ 0 for _ in xrange(N) ] for _ in xrange(N) ]
    total = 0

    counter = 0
    for m in h['ms']:
        model[m['r']][m['c']] = m['t']
        if m['t'] == 'o':
            board[m['r']][m['c']] = 2
            total += 2
        else:
            board[m['r']][m['c']] = 1
            total += 1

    models = search(N, model, board, 0, 0, total, counter)

print(models)

end = time.clock()
print end - start
sys.exit(0)
