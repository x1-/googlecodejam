import sys
import time

"""
Problem B. Cookie Clicker Alpha
"""

T = int( raw_input() )
TS = [];
for i in xrange( T ):
    x = map(float, raw_input().split())
    TS.append(x)


#----------------------------
start = time.clock()

for i in xrange( T ):

    ts = TS[i]
    C = ts[0]
    F = ts[1]
    X = ts[2]

    sec = 0
    rate = 2.0
    k = X

    if X < C:
        sec = k / 2
        k = 0

    while (k > 0):
        r = C / rate
        st = (k - C) / rate
        ch = k / (rate + F)
        if ch < st:
            rate = rate + F
        else:
            if k < C:
                sec = sec + (k/rate)
                break
            k = k - C
        sec = sec + r


    print( "Case #{0}: {1}".format( i + 1, round(sec, 7) ) )

#end = time.clock()
#print end - start
sys.exit(0)
