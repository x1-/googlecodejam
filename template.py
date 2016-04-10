import sys
import time

"""
"""
T = int( raw_input() )
ts = []
for i in xrange( T ):
    ts.append( int( raw_input() ) )

#----------------------------
start = time.clock()



end = time.clock()
print end - start
sys.exit(0)
