##LAB2
Print out URL references and the count of those references in the given input file similar to what we did for word count.

##SOLUTION:
For changing the program from word count to url count, I have changed the Mapper.py to URLMapper.py such that instead of splitting the lines to words, I defined a regular expression that gets all the patterns that start with 'href="' until it finds another double quote(").All such patterns are stored in a list and iterated over to split that pattern by "=" and print out the second part of the split, which is just the url, with 1 as its value/ count. By doing this I was able to get each url with 1 as its count. When reducer picks this up it will be sorted. Hence, the same urls apper together. The reducer then counts the occurence of each url and prints out all the unique urls with its corresponding frequency. so when i ran make stream command, it generated stream output file that had multiple parts in it. As counting entries in multiple file would be more tedious, I merged all of them to 1 file called output.txt by running: hdfs dfs -getmerge stream-output output.txt. Now that I have all the urls in 1 file, I wrote a python script to count the number of entries in the file. So by running this script, the number of urls were found to be 1144.

I have also made changes in my MakeFie to rename mapper and reducer to URLMapper.py and URLReducer.py. 

For this assignment I refered the regex from geeksforgeeks suggested for this assignment and colaborated with Priyanka Sundaram.
