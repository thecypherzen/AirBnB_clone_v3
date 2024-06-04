#!/usr/bin/python3
'''
import hashlib
ha = hashlib.new('md5')
mstr = ""
print(mstr is None)
try:
    ha.update(mstr.encode())
    print(ha.hexdigest())
except EOFError:
    print()
'''
myob = set()
myob.add(1)
ml = [0,1,2,None,3]
#myob.update({x for x in ml if x})
ml = list(filter(lambda x:x, ml))
print(ml)
