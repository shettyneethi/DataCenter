#!/usr/bin/env python
"""mapper.py"""

import sys
import re

for line in sys.stdin:
	line = line.strip()
	urls = re.findall("(href=\"[^#].*?\")",line);
	for url in urls:
		print '%s\t%s' % (url.split("=")[1], 1)
