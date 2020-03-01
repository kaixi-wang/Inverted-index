#!/usr/bin/env python

# Mapper reads data from STDIN, split it into words and output a list of linse mapping words to their counts to STDOUT
# Note: mapper will not compute an intermediate sum of a word's ocurrances
# Instead, it will output <word> 1 tuples immediately, and subsequent Reduce step do the final sum count

# Make sure file has execution permission ( chmod +x  ./mapper.py)

import sys
from sys import stdin
import re

data={}
for contents in stdin:
    content=contents.split('\t')
    docID=content[0]
    txts=content[1:]
    for txt in txts:
        words = re.findall(r'\w+', content)
        for word in words:
            print '%s/t%s' % (word, 1)
