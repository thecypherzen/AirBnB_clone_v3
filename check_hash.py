#!/usr/bin/python3
import hashlib
ha = hashlib.new('md5')
mstr = ""
print(mstr is None)
try:
    ha.update(mstr.encode())
    print(ha.hexdigest())
except EOFError:
    print()
