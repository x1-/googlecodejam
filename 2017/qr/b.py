import sys
import time

"""
Problem B. Tidy Numbers
"""

T = int( raw_input() )
TS = [];
for i in xrange( T ):
    x = int(raw_input())
    TS.append(x)


#----------------------------
start = time.clock()

for t in xrange( T ):

    N = TS[t]
    found = None

    nums = list(str(N))
    ln = len(nums)

    if ln == 1:
        found = N
    else:
        x = N
#        debug =0
        m = 0
        k = 0
        while ( k < ln ):
#            if debug == 10:
#                break
            minus = pow(10, k) * m
            x = x - minus
#            print("minus:", minus)
#            print("x:", x)

            nums = list(str(x))

            comp = None
            counter = 0
            for n in nums:
                if comp is None:
                    comp = n
                    counter += 1
#                    print("comp is none:", comp, counter)
                    continue
#                print("n, comp:", n, comp)
                if n < comp:
#                    print("n < comp:", n, comp)
                    break
                comp = n
                counter += 1

#            print("counter:", counter, len(nums))
            if counter == len(nums):
                found = x
                break

            m = 1
#            debug += 1

#            print("k:", -(k+1))

            last = nums[-(k+1)]
#            print("last:", last, nums)
            if last == '9':
                m = 1
                k += 1

    print( "Case #{0}: {1}".format( t + 1, found ) )

#end = time.clock()
#print end - start
sys.exit(0)
