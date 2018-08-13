__author__ = 'grizzly'

import sys
import math

n = int(sys.argv[1])
fibonachi = [0,1]
for i in range(2,n+1):
    fibonachi.append(fibonachi[i-2]+fibonachi[i-1])
print(fibonachi[n])
