__author__ = 'grizzly'

import sys

ispolin = str(sys.argv[1])
if len(ispolin)%2 == 0:
    
    if ispolin[:int(len(ispolin)/2)] == ispolin[int(len(ispolin)/2):][::-1]:

        print('YES')
    else:

        print('NO')
else:

    if ispolin[:int(len(ispolin)/2)] == ispolin[int(len(ispolin)/2)+1:][::-1]:
        print('YES')
    else:
        print('NO')
