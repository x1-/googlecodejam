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
    N = int(raw_input())
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
        for x in xs:
            items.setdefault(x, 0)
            items[x] += 1

    numbers = list(items.keys())
    # print(items)
    odds = [ x for x in numbers if items[x] % 2 == 1 ]
    odds.sort()

    # print( odds )
    print( "Case #{0}: {1}".format( t + 1, " ".join(map(str,odds)) ) )

#end = time.clock()
#print end - start
sys.exit(0)
