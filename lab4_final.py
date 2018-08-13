__author__ = 'grizzly'

import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#sys.argv.pop(0)
string1 = str(sys.argv[1])
string = string1.replace(' ','')
string = string[:-(len(string)%5)]
ablist = ''
newstr = ''
for i in range(1,len(string)+1):
    if string[i-1].islower():
        newstr=newstr+'a'
    else: newstr=newstr+'b'
    if (i%5 == 0)and(i!=0):
        ablist=ablist+alphabet[(key.find(newstr[i-5:i]))]
print ablist
