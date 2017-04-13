import sys
import time

"""
2016 Round 1B Problem C. Technobabble
"""

sys.setrecursionlimit(10000)

T = int( raw_input() )
ts = []
for t in xrange( T ):
    N = int(raw_input())
    words = []
    for i in xrange(N):
        words.append( raw_input().split(" ") )
    ts.append({'N': N, 'ws': words})

#----------------------------
start = time.clock()


for t in xrange(T):
    N = ts[t]['N']
    ws = ts[t]['ws']

    b = [{}, {}]

    for w in ws:
        for k in xrange(2):
            if w[k] not in b[k]:
                b[k][w[k]] = 1
            else:
                b[k][w[k]] += 1

    c = 0
    for w in ws:
        if b[0][w[0]] > 1 and b[1][w[1]] > 1:
            c += 1

    if c == N:
        c -= 1
    print( "Case #{0}: {1}".format( t + 1, c ) )

#end = time.clock()
#print end - start
sys.exit(0)
