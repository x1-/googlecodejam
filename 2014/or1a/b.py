import sys
import time

import math

"""
Problem B. Rank and File
"""



#----------------------------

T = int( raw_input() )
TS = [];
for t in xrange( T ):
    N = raw_input()
    ns = []
    for x in xrange(N*2 - 1):
        xs = map(int, raw_input().split())
        ns.append(xs)
    TS.append({ 'N': N, 'ns': ns })

#----------------------------
start = time.clock()

for t in xrange( T ):

    ts = TS[t]

    N = ts['N']
    ns = ts['ns']

    items = {}
    for xs in ns:
        items.setdefault(xs[0], [])
        items[xs[0]].append(xs)

    numbers = list(items.keys())
    smallest = min(numbers)
    papers = [ [ None for _ in xrange(N) ] for _ in xrange(N) ]
    board = dict( [ (item, [ [ 0 for _ in xrange(N) ] for _ in xrange(N) ] ) for item in numbers ] )

    if len(items[smallest]) == 1:
        for i in xrange(N):
            papers[0][i] = items[smallest][0][i]
            for j in xrange(N):
                board[items[smallest][0][i]][j][i] = items[smallest][0][i]
    else:
        for i in xrange(N):
            papers[0][i] = items[smallest][0][i]
            papers[i][0] = items[smallest][1][i]
            for j in xrange(N):
                board[items[smallest][0][i]][j][i] = items[smallest][0][i]


    print( "Case #{0}: {1} {2}".format( t + 1, mx, mn) )

#end = time.clock()
#print end - start
sys.exit(0)
