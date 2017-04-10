import sys
import time

"""
Problem A. Oversized Pancake Flipper
"""

sys.setrecursionlimit(10000)

def flipper(xs, c, K):
    newxs = list(xs)
    for n in xrange(c, min(c + K, len(newxs))):
        pancake = '-' if xs[n] == '+' else '+'
        newxs[n] = pancake
    return newxs

def rec(xs, c, K, counter):
    # print("c", c)
    if '-' not in xs:
        return (xs, counter)
    if c == len(xs):
        return (xs, counter)
    if (c + K) > len(xs):
        return (xs, counter)

    newxs = None
    if xs[c] != '+':
        newxs = flipper(xs, c, K)
        counter += 1
        # print(newxs)
    else:
        newxs = xs

    return rec(newxs, c+1, K, counter)


T = int( raw_input() )
TS = [];
for i in xrange( T ):
    (S, K) = raw_input().split()
    TS.append((S, int(K)))


#----------------------------
start = time.clock()

for t in xrange( T ):

    (S, K) = TS[t]

    counter = 0
    xs = list(S)

#    for i in xrange(len(S)):
#        if xs[i] == '-':
    (nxs, counter) = rec(xs, 0, K, counter)

    res = 'IMPOSSIBLE'
    if '-' not in nxs:
        res = counter


    print( "Case #{0}: {1}".format( t + 1, res ) )

#end = time.clock()
#print end - start
sys.exit(0)
