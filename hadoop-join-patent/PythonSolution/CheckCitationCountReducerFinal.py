#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
current_patent = None
current_patent_info = None
current_patent_citations = []

def outputPatentInfo():
    global current_patent
    global current_patent_info
    global current_patent_citations

    if current_patent != None and current_patent_info != None:
        try:
            if(current_patent_info[3].strip() == '"US"'):
		count = 0
		#print(current_patent_info[4].strip(), len(current_patent_citations))
       	        for citation in current_patent_citations:
                	#print(citation.split(',')[1].strip() ,current_patent_info[4].strip())
			if citation.split(',')[1].strip() == current_patent_info[4].strip():
				count  = count+1
				#print(current_patent,citation.strip(),current_patent_info[4])
		print('%s, %s, %s' % (current_patent ,', '.join(current_patent_info).strip(), count))
	except ValueError:
            #
            # Something wrong in number format
            #
            pass
        except Exception as e:
            print("Something died", e , current_patent_info)
    current_patent = None
    current_patent_info = None
    current_patent_citations = []

def main():
    global current_patent
    global current_patent_info
    global current_patent_citations
    current_patent = None
    debug = False
    # input comes from STDIN
    for line in sys.stdin:
        # parse the input we got from mapper.py
        try:
		key, value = line.split(', ', 1)
	except Exception as e:
		continue
        # convert count (currently a string) to int
        try:
            patent = long(key)
        except ValueError:
            # key was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_patent != patent:
            outputPatentInfo()
        current_patent = patent
        fields = value.split(', ')
       	if len(fields) > 2:
            current_patent_info = fields
        else:
            current_patent_citations.append(value) 
    # do not forget to output the last word if needed!
    outputPatentInfo()
main()
