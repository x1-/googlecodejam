import sys
import time
import itertools

"""
Problem C. Minesweeper Master
"""

T = int( raw_input() )
TS = [];
for i in xrange( T ):
    x = map(int, raw_input().split())
    TS.append(x)

def is_zero(R, C, r, c, masu, emp):

    cs = [c]
    if c > 0:
        cs.append(c-1)

    rs = [r]
    if r > 0:
        rs.append(r-1)

    combi = list(itertools.product(rs, cs))
    if c < (C - 1) and r > 0:
        combi.append((r-1, c+1))

    for (r1, c1) in combi:
        if r1 == r and c1 == c:
            continue
        if masu[r1][c1] == '*':
            return False
    return True

def dig(R, C, masu, decr):
    r = 0
    c = 0
    while ( r < R ):
        while ( c < C ):
            if decr == 0:
                break

            decr -= 1
            if is_zero(R, C, r, c, masu, decr):
                masu[r][c] = '.'

                cs = [c]
                if c < (C - 1):
                    cs.append(c+1)

                rs = [r]
                if r < (R - 1):
                    rs.append(r+1)

                combi = list(itertools.product(rs, cs))
                if c > 0 and r < (R - 1):
                    combi.append((r+1, c-1))

                if len(combi) > decr:
                    return masu

                for (r1, c1) in combi:
                    if decr == 0:
                        masu[r1][c1] = '1'
                        print('stop', r1, c1)
                        break
                    masu[r1][c1] = '.'
                    decr -= 1

            else:
                masu[r][c] = '1'
                c += 1
                break
            c += 1
        r += 1
    print( masu )
    return masu

#----------------------------
start = time.clock()

for t in xrange( T ):

    R = TS[i][0]
    C = TS[i][1]
    M = TS[i][2]

    empties = R * C - M
    decr = empties

    masu = [ [ None for _ in xrange(C) ] for _ in xrange(R) ]
    impossible = False

    if M == 0:
        masu = [ [ '.' for _ in xrange(C) ] for _ in xrange(R) ]
    if R == 1 or C == 1:
        for r in xrange(R):
            for c in xrange(C):
                if decr > 0:
                    masu[r][c] = '.'
                    decr -= 1
                else:
                    masu[r][c] = '*'
    else:
        masu = dig(R, C, masu, decr)
        mm = 0
        for r in xrange(R):
            for c in xrange(C):
                if masu[r][c] == '1':
                    masu[r][c] = '.'
                elif masu[r][c] is None or masu[r][c] == '*':
                    mm += 1
                    masu[r][c] = '*'

        if mm != M:
            impossible = True

    masu[0][0] = 'C'
    print( "Case #{0}:".format( t + 1 ) )
    if impossible:
        print("Impossible")
    else:
        for row in masu:
            print("".join(row))

end = time.clock()
print end - start
sys.exit(0)
