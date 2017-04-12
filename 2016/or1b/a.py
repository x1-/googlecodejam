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
checks = []
checks[0] = {"Z": "ZERO", "W": "TWO", "X": "SIX", "G": "EIGHT"}
checks[1] = {"S": "SEVEN"}
checks[2] = {"V": "FIVE"}
checks[3] = {"F": "FOUR"}
checks[4] = {"O": "ONE"}
checks[5] = {"T": "THREE"}
checks[6] = {"N": "NINE"}



def drain( i, s, numbers ):
    keys = checks[i].keys()
    found = 0
    for k in keys:
        pos = s.find(k)
        if pos >= 0:
            tmp = s[0:pos] + s[(pos+1):]
            found += 1
    if found > 0:
        return drain(i, s, numbers)

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
