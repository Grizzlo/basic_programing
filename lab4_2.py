__author__ = 'grizzly'

import sys

sys.argv.reverse()
sys.argv.pop()
print(' '.join(sys.argv))
