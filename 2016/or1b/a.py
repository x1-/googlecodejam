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

digits_list = map( lambda x: list(x), digits )
checks = [
  {"Z": "ZERO", "W": "TWO", "X": "SIX", "G": "EIGHT"},
  {"S": "SEVEN"},
  {"V": "FIVE"},
  {"F": "FOUR"},
  {"O": "ONE"},
  {"T": "THREE"},
  {"N": "NINE"}
]
dmap = {
    "Z": "0",
    "W": "2",
    "X": "6",
    "G": "8",
    "S": "7",
    "V": "5",
    "F": "4",
    "O": "1",
    "T": "3",
    "N": "9"
}

checks_list = [ dict([(k, list(v)) for k,v in check.items()]) for check in checks ]

def drain( ss, cs ):
    s = ss
    tmp = ''
    for c in cs:
        if len(s) == 1:
            if c == s:
                return ''
        else:
            pos = s.find(c)
            if pos >= 0:
                tmp = s[0:pos]
                if len(s) > (pos + 1):
                    tmp += s[(pos+1):]
        s = tmp
    return s

#----------------------------
start = time.clock()


for t in xrange(T):
    S = ts[t]
    xs = list(S)
    numbers = []
    wk = S

    for i in xrange(7):
        check = checks_list[i]
        check_s = checks[i]
        while (True):
            found = False
            for c in check.keys():
                if c in wk:
                    # print(c, check[c])
                    found = True
                    numbers.append(dmap[c])
                    wk = drain(wk, check[c])
            if not found:
                break

    numbers.sort()
    print( "Case #{0}: {1}".format( t + 1, "".join(numbers) ) )

#end = time.clock()
#print end - start
sys.exit(0)
