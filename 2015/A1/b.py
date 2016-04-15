import sys
import time

"""
2015 Problem B. Haircut
"""
def euclidean( a, b ):
    b = max( a, b )
    s = min( a, b )
    r = b % s
    while r > 0:
        b = s
        s = r
        r = b % s
        print( b, s, r )
    return b

def calc( B, N, ms ):
    total = sum( ms )
    m = N % B
    s = N / B
    ( s * total )


# T = int( raw_input() )
# ts = []
# for i in xrange( T ):
#     bn = map( int, raw_input().split() )
#     ms = map( int, raw_input().split() )
#     ts.append( ( bn, m ) )

#----------------------------
start = time.clock()

# res = []
# for bn, ms in ts:
#     calc( bn[0], bn[1], ms )
#     res.append( ( c1, c2 ) )

# for i in xrange( T ):
#     ( x, y ) = res[i]
#     print( "Case #{0}: {1} {2}".format( i+1, x, y ) )


print( euclidean( 3, 5 ) )

end = time.clock()
#print end - start
sys.exit(0)
