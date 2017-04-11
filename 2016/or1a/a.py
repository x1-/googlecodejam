import sys
import time

import string

"""
2016 Problem A. The Last Word
"""

sys.setrecursionlimit(10000)

T = int( raw_input() )
ts = []
for t in xrange( T ):
    ts.append( raw_input() )


alphas = list(string.ascii_uppercase)
adic = {}
for i in xrange(26):
    adic[alphas[i]] = i

#----------------------------
start = time.clock()


for t in xrange(T):
    S = ts[t]
    xs = list(S)
    word = ''
    for s in xs:
         b_temp = s + word
         a_temp = word + s
         if b_temp > a_temp:
             word = b_temp
         else:
             word = a_temp

    print( "Case #{0}: {1}".format( t + 1, word ) )

#end = time.clock()
#print end - start
sys.exit(0)
