__author__ = 'grizzly'

import sys

x = sys.argv[1]
if x[0]==")":
    print('NO')
else:
    bool_list = []
    for i in range(0,len(x)):
        if x[i] == '(':
            bool_list.append(False)
        else:
          if bool_list.count(False) != 0:
              bool_list[bool_list.index(False)] = True
          else:
              bool_list.append(None)
    if (bool_list.count(False) == 0) and (bool_list.count(None) == 0):
        print('YES')
    else : print('NO')
