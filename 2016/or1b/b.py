import sys
import time

"""
2016 Round 1B Problem B. Close Match
"""

sys.setrecursionlimit(10000)

T = int( raw_input() )
ts = []
for t in xrange( T ):
    ts.append( raw_input().split(" ") )


#----------------------------
start = time.clock()


for t in xrange(T):
    C = ts[t][0]
    J = ts[t][1]

    size = len(C)
    cs = list(C)
    js = list(J)

    tmp_c = list(C)
    tmp_j = list(J)

    p_c = None
    p_j = None

    prev_c = None
    prev_j = None
    for i in xrange(size):
        c = cs[i]
        j = js[i]
        if cs[i] == '?' and js[i] == '?':
            if prev_c == prev_j:
                tmp_c[i] = '0'
                tmp_j[i] = '0'
            elif prev_c > prev_j:
                tmp_c[i] = '0'
                tmp_j[i] = '9'
            else:
                tmp_c[i] = '9'
                tmp_j[i] = '0'
        elif cs[i] == '?' and js[i] != '?':
            if prev_c == prev_j:
                tmp_c[i] = js[i]
            elif prev_c > prev_j:
                tmp_c[i] = '0'
            else:
                tmp_c[i] = '9'

        elif cs[i] != '?' and js[i] == '?':
            if prev_c == prev_j:
                tmp_j[i] = cs[i]
            elif prev_c > prev_j:
                tmp_j[i] = '9'
            else:
                tmp_j[i] = '0'
        else:
            if i > 0:
                pc = int(tmp_c[i-1])
                pj = int(tmp_j[i-1])
                if cs[i-1] == '?':
                    ppj = tmp_j[i-1] + js[i]
                    if cs[i] > js[i] and pc > 0:
                        if abs(int( tmp_c[i-1] + cs[i] ) - int( ppj )) > abs(int( str(pc - 1) + cs[i] ) - int( ppj )):
                            tmp_c[i-1] = str(pc - 1)
                    elif js[i] > cs[i] and pc < 9:
                        if abs(int( tmp_c[i-1] + cs[i] ) - int( ppj )) > abs(int( str(pc + 1) + cs[i] ) - int( ppj )):
                            tmp_c[i-1] = str(pc + 1)
                if js[i-1] == '?':
                    ppc = tmp_c[i-1] + cs[i]
                    if js[i] > cs[i] and pj > 0:
                        if abs(int( tmp_j[i-1] + js[i] ) - int( ppc )) > abs(int( str(pj - 1) + js[i] ) - int( ppc )):
                            tmp_j[i-1] = str(pj - 1)
                    elif cs[i] > js[i] and pj < 9:
                        if abs(int( tmp_j[i-1] + js[i] ) - int( ppc )) > abs(int( str(pj + 1) + js[i] ) - int( ppc )):
                            tmp_j[i-1] = str(pj + 1)

        prev_c = int("".join(tmp_c[0:i+1]))
        prev_j = int("".join(tmp_j[0:i+1]))

    print( "Case #{0}: {1} {2}".format( t + 1, "".join(tmp_c), "".join(tmp_j) ) )

#end = time.clock()
#print end - start
sys.exit(0)
