import sys
import time

"""
Problem C. BFFs
"""

def calc(N, fs, occupied, i, num):
    if num == N:
        return num
    # j = (i - N) if i >= N else i
    j = i
    bff = fs[j] - 1
    if occupied[bff] == 2:
        return num
    occupied[j] += 1
    occupied[bff] += 1
    print(i, occupied)
    return calc(N, fs, occupied, bff, num + 1)


#----------------------------

T = int( raw_input() )
TS = [];
for t in xrange( T ):
    N = int(raw_input())
    fs = map(int, raw_input().split())
    TS.append({'N': N, 'fs': fs})

#----------------------------
start = time.clock()

for t in xrange( T ):

    N = TS[t]['N']
    fs = TS[t]['fs']

    mx = None
    for i in xrange(N):
        occupied = [ 0 for _ in xrange(N) ]
        c = calc(N, fs, occupied, i, 1)
        print(i, c)
        if mx is None:
            mx = c
        else:
            mx = max(c, mx)
        if mx == N:
            break

    print( "Case #{0}: {1}".format( t + 1, mx ) )

#end = time.clock()
#print end - start
sys.exit(0)
