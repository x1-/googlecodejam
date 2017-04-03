import sys
import time

"""
Problem A. Magic Trick
"""

T = int( raw_input() )
ts = [];
for i in xrange( T ):
    ht = {
        'a1': 0,
        'a2': 0,
        'o1': [],
        'o2': []
    }
    ht['a1'] = int( raw_input() )
    for j in xrange(4):
        x = map(int, raw_input().split())
        ht['o1'].append( set(x) )
    ht['a2'] = int( raw_input() )
    for j in xrange(4):
        x = map(int, raw_input().split())
        ht['o2'].append( set(x) )
    ts.append(ht)


#----------------------------
start = time.clock()

for i in xrange( T ):

    ps = ts[i]

    a1 = ps['a1'] - 1
    c1 = ps['o1'][a1]

    a2 = ps['a2'] - 1
    c2 = ps['o2'][a2]

    ns = c1.intersection(c2)
    ans = ''
    if len(ns) == 1:
        ans = str(ns.pop())
    elif len(ns) == 0:
        ans = 'Volunteer cheated!'
    else:
        ans = 'Bad magician!'

    print( "Case #{0}: {1}".format( i + 1, ans ) )

#end = time.clock()
#print end - start
sys.exit(0)
