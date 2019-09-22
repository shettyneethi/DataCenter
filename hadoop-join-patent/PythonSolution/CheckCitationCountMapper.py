#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into CSV fields
    words = line.split(",")

    if len(words) == 2:
        #
        # It's a citation
        #
        try:
            print('%s\t%s' % (words[1].strip(), words[0]))
        except Exception as e:
            # improperly formed citation number
            print("Exception ", e);
            pass
    else:
        #
        # It's patent info 
        #
        try:
            print('%s\t%s' % (words[0], ','.join(words[1:])))
        except Exception as e:
            # improperly formed citation number
            print("Exception ", e);
            pass

