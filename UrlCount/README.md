## UrlCount

`Makefile` :  This provides basic steps to prepare and run the provided UrlCount program.
The makefile is structured assuming you're using Google's `dataproc` Hadoop cluster. You may need to modify paths if you're working in a different environment.

To test and evaluate your system, we download two WikiPedia articles. Hadoop accesses files from the HDFS file system, and we've provided a `make prepare` rule to copy the wikipedia articles to HDFS in the `input` directory. Prior to copying the files, you may need to create an HDFS entry for your user id (`make filesystem`).

Mapper extracts URL references from the documents in the input directory. Mapper will then output URL references and the count of those references in the input file.
