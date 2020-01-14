import collections
import re
import sys
spys=[]
with open("/Book.txt", "r") as f:
    spys=collections.Counter(sorted(re.findall(r'(\w+[\'\-\w+]\w+)', f.read().lower())))
    for i in spys:
        print ('Word', i, 'is placed in text', str(spys[i]), 'times')