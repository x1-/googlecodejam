import sys
import time

"""
2015 Problem A. Mushroom Monster
"""

T = int( raw_input() )
ts = []
for i in xrange( T ):
    n = int( raw_input() )
    m = map( int, raw_input().split() )
    ts.append( ( n, m ) )

#----------------------------
start = time.clock()

res = []
for n, m in ts:
    c1 = m[-2] - m[-1]
    c2 = c1
    for i in xrange( n - 2 ):
        if m[i] > m[i+1]:
            c1 += ( m[i] - m[i+1] )
        c2 += m[i]
    res.append( ( c1, c2 ) )

for i in xrange( T ):
    ( x, y ) = res[i]
    print( "Case #{0}: {1} {2}".format( i, x, y ) )

end = time.clock()
#print end - start
sys.exit(0)
