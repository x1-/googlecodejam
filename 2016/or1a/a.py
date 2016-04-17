import sys
import time

"""
2016 Problem A. The Last Word
"""

sys.setrecursionlimit(10000)

def rec( S, one, i, j, stop_i, memo ):
    if i >= stop_i:
        return one
    # if memo.has_key( one ):
    #     if memo[ one ].has_key( i ):
    #         return memo[ one ][ i ]

    if memo[i][j] <> "":
        return memo[i][j]

    r = max(
        rec( S, one + S[i], i + 1, 0, stop_i, memo ),
        rec( S, S[i] + one, i + 1, 1, stop_i, memo ) )
#    memo[ one ] = { i: r }
    # print( one )
    # print( i, r )
    memo[i][j] = r
    print( i, j)
    print r
    return r

def calc( S ):
    memo = [ [ "" for x in xrange( 2 ) ] for x in xrange( len(S) + 1 ) ]
    return rec( S, S[0], 1, 0, len(S), memo )

def calc2( S ):
    N = len(S)
    dp = [ [ "" for x in xrange( 2 ) ] for x in xrange( N + 1 ) ]
    #for i in xrange( len(S) - 1, -1, -1 ):
    for i in xrange( len(S) ):
        for j in xrange( 2 ):
            dp[i][j] = max(
                dp[i - 1][0] + S[i],
                S[i] + dp[i - 1][1] )
    return max( dp[N-1][0], dp[N-1][1] )

T = int( raw_input() )
xs = []
for i in xrange( T ):
    xs.append( raw_input() )


#----------------------------
start = time.clock()

n = 1
for s in xs:
    r = calc2( s )
    print( "Case #{0}: {1}".format( n, r ) )
    n += 1

#end = time.clock()
#print end - start
sys.exit(0)
