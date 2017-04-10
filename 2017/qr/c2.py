import sys
import time

import math

"""
Problem C. Bathroom Stalls
"""

def incr_dict(memo, key):
    if key not in memo:
        memo[key] = 0
    memo[key] += 1
    return memo

def append_dict(memo, key, value):
    if key not in memo:
        memo[key] = []
    memo[key].append(value)
    return memo

def pop_dict(memo, key):
    if key in memo:
        memo[key] -= 1
        if memo[key] == 0:
            del memo[key]

    return memo


def longest(memo):
    if len(memo) == 0:
        return None
    items = memo.keys()
    return max(items)



#----------------------------

T = int( raw_input() )
TS = [];
for t in xrange( T ):
    xs = map(int, raw_input().split())
    TS.append(xs)

#----------------------------
start = time.clock()

for t in xrange( T ):

    ts = TS[t]

    N = ts[0]
    K = ts[1]

    k = K
    start = 0
    end = N + 1

    rooms = [ 0 for _ in xrange(N+2) ]
    memo = {}

    midp = int(math.ceil(N / 2))

    if N == K:
        print( "Case #{0}: {1} {2}".format( t + 1, 0, 0 ) )
        continue

    # if (N - 1) == K:
    #      print( "Case #{0}: {1} {2}".format( t + 1, 0, 0 ) )
    #      continue

    # if midp < K:
    #     print( "Case #{0}: {1} {2}".format( t + 1, 0, 0 ) )
    #     continue

    rooms[0] = 1
    rooms[-1] = 1

    l = None
    r = None
    memo = incr_dict(memo, N)


    for i in xrange(K):
        mlong = longest(memo)
        memo = pop_dict(memo, mlong)
        # print(mlong)
        # print(memo)
        pos = int(math.floor(mlong / 2))
        m = mlong % 2
        if m == 0:
            l = mlong - 1 - pos
            r = mlong - pos
        else:
            l = mlong - 1 - pos
            r = mlong - 1 - pos

        # print(pos, m, l, r)

        memo = incr_dict(memo, l)
        memo = incr_dict(memo, r)

    mx = r if r > l else l
    mn = r if r < l else l

    print( "Case #{0}: {1} {2}".format( t + 1, mx, mn) )

#end = time.clock()
#print end - start
sys.exit(0)
