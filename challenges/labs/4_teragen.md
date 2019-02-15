[hdfs@ip-172-32-1-156 parcels]$ time hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-examples.jar teragen -Dmapred.map.tasks=8 -Ddfs.block.size=7864320 12345000 /user/rocky/teragen
19/02/15 11:02:20 INFO client.RMProxy: Connecting to ResourceManager at ip-172-32-1-156.eu-west-1.compute.internal/172.32.1.156:8032
19/02/15 11:02:21 INFO terasort.TeraGen: Generating 12345000 using 8
19/02/15 11:02:21 INFO mapreduce.JobSubmitter: number of splits:8
19/02/15 11:02:21 INFO Configuration.deprecation: dfs.block.size is deprecated. Instead, use dfs.blocksize
19/02/15 11:02:21 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
19/02/15 11:02:21 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1550226705818_0003
19/02/15 11:02:21 INFO impl.YarnClientImpl: Submitted application application_1550226705818_0003
19/02/15 11:02:21 INFO mapreduce.Job: The url to track the job: http://ip-172-32-1-156.eu-west-1.compute.internal:8088/proxy/application_1550226705818_0003/
19/02/15 11:02:21 INFO mapreduce.Job: Running job: job_1550226705818_0003
19/02/15 11:02:26 INFO mapreduce.Job: Job job_1550226705818_0003 running in uber mode : false
19/02/15 11:02:26 INFO mapreduce.Job:  map 0% reduce 0%
19/02/15 11:02:35 INFO mapreduce.Job:  map 75% reduce 0%
19/02/15 11:02:36 INFO mapreduce.Job:  map 100% reduce 0%
19/02/15 11:02:36 INFO mapreduce.Job: Job job_1550226705818_0003 completed successfully
19/02/15 11:02:36 INFO mapreduce.Job: Counters: 31
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=1195744
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=677
		HDFS: Number of bytes written=1234500000
		HDFS: Number of read operations=32
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=16
	Job Counters 
		Launched map tasks=8
		Other local map tasks=8
		Total time spent by all maps in occupied slots (ms)=51249
		Total time spent by all reduces in occupied slots (ms)=0
		Total time spent by all map tasks (ms)=51249
		Total vcore-milliseconds taken by all map tasks=51249
		Total megabyte-milliseconds taken by all map tasks=52478976
	Map-Reduce Framework
		Map input records=12345000
		Map output records=12345000
		Input split bytes=677
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=972
		CPU time spent (ms)=26680
		Physical memory (bytes) snapshot=2669117440
		Virtual memory (bytes) snapshot=22508072960
		Total committed heap usage (bytes)=2813329408
	org.apache.hadoop.examples.terasort.TeraGen$Counters
		CHECKSUM=26510014434051487
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=1234500000

real	0m18.010s
user	0m4.926s
sys	0m0.291s

[hdfs@ip-172-32-1-156 parcels]$ hdfs dfs -ls /user/rocky/teragen
Found 9 items
-rw-r--r--   3 hdfs supergroup          0 2019-02-15 11:02 /user/rocky/teragen/_SUCCESS
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00000
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00001
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00002
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00003
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00004
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00005
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00006
-rw-r--r--   3 hdfs supergroup  154312500 2019-02-15 11:02 /user/rocky/teragen/part-m-00007
[hdfs@i

 hadoop fsck -blocks /user/rocky
DEPRECATED: Use of this script to execute hdfs command is deprecated.
Instead use the hdfs command for it.

Connecting to namenode via http://ip-172-32-1-156.eu-west-1.compute.internal:50070/fsck?ugi=hdfs&blocks=1&path=%2Fuser%2Frocky
FSCK started by hdfs (auth:SIMPLE) from /172.32.1.156 for path /user/rocky at Fri Feb 15 11:05:06 UTC 2019
.........Status: HEALTHY
 Total size:	1234500000 B
 Total dirs:	2
 Total files:	9
 Total symlinks:		0
 Total blocks (validated):	160 (avg. block size 7715625 B)
 Minimally replicated blocks:	160 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	3
 Average block replication:	3.0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Number of data-nodes:		4
 Number of racks:		1
FSCK ended at Fri Feb 15 11:05:06 UTC 2019 in 3 milliseconds


The filesystem under path '/user/rocky' is HEALTHY
[hdfs@ip-172-32-1-156 parcels]$ 

