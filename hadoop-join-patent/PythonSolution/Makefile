STREAMING = /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar

prepare:
	 echo "Some of the following commands may fail because your"
	echo "files are already setup"
	echo "====="
	-hdfs dfs -mkdir /user
	-hdfs dfs -mkdir /user/$(USER)
	-hdfs dfs -rm -r -f /user/$(USER)/input
	-hdfs dfs -rm -r -f /user/$(USER)/stream-output        
	-hdfs dfs -mkdir /user/$(USER)/input
	-hdfs dfs -put apat63_99.txt /user/$(USER)/input
	-hdfs dfs -put cite75_99.txt /user/$(USER)/input

stream:
	sh ./RUN-MAP-REDUCE-1
