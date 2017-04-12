import sys
import time

import string

"""
2016 Round 1B Problem A. Getting the Digits
"""

sys.setrecursionlimit(10000)

T = int( raw_input() )
ts = []
for t in xrange( T ):
    ts.append( raw_input() )

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
dmap = {}
for i in xrange(10):
    dmap[digits[i]] = str(i)

digits_list = map( lambda x: list(x), digits )

def consists( s, xs ):
    candi = [ x for x in digits if s in x ]
    for c in candi:
        remain = [ x for x in xs if x not in c ]
        if len(c) == len(remain):
            return (c, remain)
    return (None, None)

#----------------------------
start = time.clock()


for t in xrange(T):
    S = ts[t]
    xs = list(S)
    numbers = []
    wk = S
    while (wk <> ''):
        for i in xrange(10):
            digit_l = digits_list[i]
            digit = digits[i]
            fail = False
            temp_s = wk
            for d in digit_l:
                idx = temp_s.find(d)
                if idx >= 0:
                    temp_s = temp_s[0:idx] + temp_s[(idx+1):]
                else:
                    fail = True
                    break
            if not fail:
                numbers.append( dmap[digit] )
                wk = temp_s
            if len(wk) == 0:
                break

    numbers.sort()
    print( "Case #{0}: {1}".format( t + 1, "".join(numbers) ) )

#end = time.clock()
#print end - start
sys.exit(0)
