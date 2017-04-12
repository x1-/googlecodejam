import sys
import time

"""
Problem C. BFFs
"""

def calc(N, fs, occupied, i, num):
    print(i, occupied)
    if num == N:
        return num

    bff = fs[i] - 1
    if occupied[bff] == 1:
        return num + 1
    elif occupied[bff] == 2:
        print("occupied[bff]", bff, i, fs[bff])
        if i == (fs[bff] - 1):
            print("i == bff", i, fs[bff])
            f = search(N, fs, i)
            print("search", f)
            if len(f) == 0:
                return num
            else:
                for sf in f:
                    print("26: for sf in f", sf, occupied[sf])
                    if occupied[sf] == 0:
                        occupied[i] += 1
                        occupied[sf] += 1
                        return calc(N, fs, occupied, sf, num + 1)
                    elif occupied[sf] == 1:
                        return num + 1
        else:
            return 0
    occupied[i] += 1
    occupied[bff] += 1
    return calc(N, fs, occupied, bff, num + 1)


def search(N, fs, i):
    found = []
    for k in xrange(N):
        if (fs[k] - 1) == i:
            found.append( k )

    return found


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
        c = calc(N, fs, occupied, i, 0)
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
