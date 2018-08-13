__author__ = 'grizzly'

import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
num = 0
for i in range(a1,a2+1):
    added ="0"*(6-len(str(i)))+str(i)
    if (int(added[0])+int(added[1])+int(added[2])) == (int(added[5])+int(added[4])+int(added[3])):
        num += 1
        print added
print num
