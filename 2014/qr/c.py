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


#----------------------------
start = time.clock()

for t in xrange( T ):

    R = TS[i][0]
    C = TS[i][1]
    M = TS[i][2]

    rs = [ i for i in xrange(R) ]
    cs = [ i for i in xrange(C) ]

    combi = list(itertools.product(rs, cs))

    print(combi)

    ms = list(itertools.combinations(combi, M))

    print(ms)

    for m in ms:
        masu = [[None for _ in xrange(C)] for y in xrange(R)]

        r = 0
        c = 0
        while ( r < R ):
            while ( c < C ):
                if (r, c) in m:
                    masu[r][c] = '*'
                else:
                    masu[r][c] = '*'
                c += 1
            r += 1
            for c in xrange(C):
    print( "Case #{0}: {1}".format( t + 1, 0 ) )

#end = time.clock()
#print end - start
sys.exit(0)
