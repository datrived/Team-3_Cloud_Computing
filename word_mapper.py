#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    word = line.split()
    for w in word:
        print "%s\t%s" % (w, "1")

