[snawalgaria@ip-172-32-1-71 ec2-user]$  time hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-examples.jar teragen -Dmapred.map.tasks=4 -Ddfs.block.size=33554432 100000000 /user/snawalgaria/teragen
19/02/13 08:07:52 INFO client.RMProxy: Connecting to ResourceManager at ip-172-32-1-185.eu-west-1.compute.internal/172.32.1.185:8032s=4 -Ddfs.block.size=3355443[snawalgaria@ip-172-32-1-71 ec2-user]$  time hadoop19/02/13 08:07:53 INFO terasort.TeraGen: Generating 100000000 using 4
19/02/13 08:07:53 INFO mapreduce.JobSubmitter: number of splits:4
19/02/13 08:07:53 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
19/02/13 08:07:53 INFO Configuration.deprecation: dfs.block.size is deprecated. Instead, use dfs.blocksize
19/02/13 08:07:53 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1549984636723_0004
19/02/13 08:07:53 INFO impl.YarnClientImpl: Submitted application application_1549984636723_0004
19/02/13 08:07:53 INFO mapreduce.Job: The url to track the job: http://ip-172-32-1-185.eu-west-1.compute.internal:8088/proxy/application_1549984636723_0004/
19/02/13 08:07:53 INFO mapreduce.Job: Running job: job_1549984636723_0004
19/02/13 08:07:58 INFO mapreduce.Job: Job job_1549984636723_0004 running in uber mode : false
19/02/13 08:07:58 INFO mapreduce.Job:  map 0% reduce 0%
19/02/13 08:08:14 INFO mapreduce.Job:  map 12% reduce 0%
19/02/13 08:08:16 INFO mapreduce.Job:  map 35% reduce 0%
19/02/13 08:08:20 INFO mapreduce.Job:  map 40% reduce 0%
19/02/13 08:08:22 INFO mapreduce.Job:  map 52% reduce 0%
19/02/13 08:08:26 INFO mapreduce.Job:  map 56% reduce 0%
19/02/13 08:08:28 INFO mapreduce.Job:  map 67% reduce 0%
19/02/13 08:08:32 INFO mapreduce.Job:  map 71% reduce 0%
19/02/13 08:08:34 INFO mapreduce.Job:  map 80% reduce 0%
19/02/13 08:08:40 INFO mapreduce.Job:  map 87% reduce 0%
19/02/13 08:08:46 INFO mapreduce.Job:  map 94% reduce 0%
19/02/13 08:08:50 INFO mapreduce.Job:  map 95% reduce 0%
19/02/13 08:08:51 INFO mapreduce.Job:  map 98% reduce 0%
19/02/13 08:08:52 INFO mapreduce.Job:  map 100% reduce 0%
19/02/13 08:08:52 INFO mapreduce.Job: Job job_1549984636723_0004 completed successfully
19/02/13 08:08:52 INFO mapreduce.Job: Counters: 31
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=606448
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=344
		HDFS: Number of bytes written=10000000000
		HDFS: Number of read operations=16
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=8
	Job Counters 
		Launched map tasks=4
		Other local map tasks=4
		Total time spent by all maps in occupied slots (ms)=187634
		Total time spent by all reduces in occupied slots (ms)=0
		Total time spent by all map tasks (ms)=187634
		Total vcore-milliseconds taken by all map tasks=187634
		Total megabyte-milliseconds taken by all map tasks=192137216
	Map-Reduce Framework
		Map input records=100000000
		Map output records=100000000
		Input split bytes=344
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=1516
		CPU time spent (ms)=122790
		Physical memory (bytes) snapshot=893370368
		Virtual memory (bytes) snapshot=6316834816
		Total committed heap usage (bytes)=973602816
	org.apache.hadoop.examples.terasort.TeraGen$Counters
		CHECKSUM=214760662691937609
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=10000000000

real	1m2.255s
user	0m4.311s
sys	0m0.219s
[snawalgaria@ip-172-32-1-71 ec2-user]$  time hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-examples.jar terasort /user/snawalgaria/teragen /user/snawalgaria/terasort
19/02/13 08:10:07 INFO terasort.TeraSort: starting
19/02/13 08:10:08 INFO input.FileInputFormat: Total input paths to process : 4
Spent 148ms computing base-splits.
Spent 3ms computing TeraScheduler splits.
Computing input splits took 151ms
Sampling 10 splits of 300
Making 8 from 100000 sampled records
Computing parititions took 547ms
Spent 699ms computing partitions.
19/02/13 08:10:09 INFO client.RMProxy: Connecting to ResourceManager at ip-172-32-1-185.eu-west-1.compute.internal/172.32.1.185:8032
19/02/13 08:10:09 INFO mapreduce.JobSubmitter: number of splits:300
19/02/13 08:10:09 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1549984636723_0005
19/02/13 08:10:09 INFO impl.YarnClientImpl: Submitted application application_1549984636723_0005
19/02/13 08:10:09 INFO mapreduce.Job: The url to track the job: http://ip-172-32-1-185.eu-west-1.compute.internal:8088/proxy/application_1549984636723_0005/
19/02/13 08:10:09 INFO mapreduce.Job: Running job: job_1549984636723_0005
19/02/13 08:10:14 INFO mapreduce.Job: Job job_1549984636723_0005 running in uber mode : false
19/02/13 08:10:14 INFO mapreduce.Job:  map 0% reduce 0%
19/02/13 08:10:24 INFO mapreduce.Job:  map 1% reduce 0%
19/02/13 08:10:25 INFO mapreduce.Job:  map 4% reduce 0%
19/02/13 08:10:34 INFO mapreduce.Job:  map 5% reduce 0%
19/02/13 08:10:35 INFO mapreduce.Job:  map 7% reduce 0%
19/02/13 08:10:36 INFO mapreduce.Job:  map 8% reduce 0%
19/02/13 08:10:43 INFO mapreduce.Job:  map 9% reduce 0%
19/02/13 08:10:44 INFO mapreduce.Job:  map 11% reduce 0%
19/02/13 08:10:45 INFO mapreduce.Job:  map 12% reduce 0%
19/02/13 08:10:52 INFO mapreduce.Job:  map 14% reduce 0%
19/02/13 08:10:53 INFO mapreduce.Job:  map 15% reduce 0%
19/02/13 08:10:55 INFO mapreduce.Job:  map 16% reduce 0%
19/02/13 08:11:00 INFO mapreduce.Job:  map 17% reduce 0%
19/02/13 08:11:02 INFO mapreduce.Job:  map 19% reduce 0%
19/02/13 08:11:03 INFO mapreduce.Job:  map 20% reduce 0%
19/02/13 08:11:09 INFO mapreduce.Job:  map 21% reduce 0%
19/02/13 08:11:10 INFO mapreduce.Job:  map 22% reduce 0%
19/02/13 08:11:11 INFO mapreduce.Job:  map 23% reduce 0%
19/02/13 08:11:12 INFO mapreduce.Job:  map 24% reduce 0%
19/02/13 08:11:18 INFO mapreduce.Job:  map 25% reduce 0%
19/02/13 08:11:19 INFO mapreduce.Job:  map 26% reduce 0%
19/02/13 08:11:20 INFO mapreduce.Job:  map 27% reduce 0%
19/02/13 08:11:21 INFO mapreduce.Job:  map 28% reduce 0%
19/02/13 08:11:27 INFO mapreduce.Job:  map 29% reduce 0%
19/02/13 08:11:28 INFO mapreduce.Job:  map 30% reduce 0%
19/02/13 08:11:29 INFO mapreduce.Job:  map 31% reduce 0%
19/02/13 08:11:30 INFO mapreduce.Job:  map 32% reduce 0%
19/02/13 08:11:35 INFO mapreduce.Job:  map 33% reduce 0%
19/02/13 08:11:37 INFO mapreduce.Job:  map 34% reduce 0%
19/02/13 08:11:38 INFO mapreduce.Job:  map 35% reduce 0%
19/02/13 08:11:39 INFO mapreduce.Job:  map 36% reduce 0%
19/02/13 08:11:45 INFO mapreduce.Job:  map 37% reduce 0%
19/02/13 08:11:46 INFO mapreduce.Job:  map 38% reduce 0%
19/02/13 08:11:47 INFO mapreduce.Job:  map 39% reduce 0%
19/02/13 08:11:48 INFO mapreduce.Job:  map 40% reduce 0%
19/02/13 08:11:54 INFO mapreduce.Job:  map 41% reduce 0%
19/02/13 08:11:55 INFO mapreduce.Job:  map 42% reduce 0%
19/02/13 08:11:56 INFO mapreduce.Job:  map 43% reduce 0%
19/02/13 08:11:57 INFO mapreduce.Job:  map 44% reduce 0%
19/02/13 08:12:02 INFO mapreduce.Job:  map 45% reduce 0%
19/02/13 08:12:04 INFO mapreduce.Job:  map 46% reduce 0%
19/02/13 08:12:05 INFO mapreduce.Job:  map 47% reduce 0%
19/02/13 08:12:06 INFO mapreduce.Job:  map 48% reduce 0%
19/02/13 08:12:11 INFO mapreduce.Job:  map 49% reduce 0%
19/02/13 08:12:13 INFO mapreduce.Job:  map 50% reduce 0%
19/02/13 08:12:14 INFO mapreduce.Job:  map 51% reduce 0%
19/02/13 08:12:15 INFO mapreduce.Job:  map 52% reduce 0%
19/02/13 08:12:20 INFO mapreduce.Job:  map 53% reduce 0%
19/02/13 08:12:22 INFO mapreduce.Job:  map 54% reduce 0%
19/02/13 08:12:23 INFO mapreduce.Job:  map 55% reduce 0%
19/02/13 08:12:25 INFO mapreduce.Job:  map 56% reduce 0%
19/02/13 08:12:28 INFO mapreduce.Job:  map 57% reduce 0%
19/02/13 08:12:31 INFO mapreduce.Job:  map 58% reduce 0%
19/02/13 08:12:32 INFO mapreduce.Job:  map 59% reduce 0%
19/02/13 08:12:34 INFO mapreduce.Job:  map 60% reduce 0%
19/02/13 08:12:38 INFO mapreduce.Job:  map 61% reduce 0%
19/02/13 08:12:40 INFO mapreduce.Job:  map 63% reduce 0%
19/02/13 08:12:42 INFO mapreduce.Job:  map 64% reduce 0%
19/02/13 08:12:46 INFO mapreduce.Job:  map 65% reduce 0%
19/02/13 08:12:49 INFO mapreduce.Job:  map 67% reduce 0%
19/02/13 08:12:51 INFO mapreduce.Job:  map 68% reduce 0%
19/02/13 08:12:55 INFO mapreduce.Job:  map 69% reduce 0%
19/02/13 08:12:58 INFO mapreduce.Job:  map 70% reduce 0%
19/02/13 08:12:59 INFO mapreduce.Job:  map 71% reduce 0%
19/02/13 08:13:00 INFO mapreduce.Job:  map 72% reduce 0%
19/02/13 08:13:04 INFO mapreduce.Job:  map 73% reduce 0%
19/02/13 08:13:06 INFO mapreduce.Job:  map 74% reduce 0%
19/02/13 08:13:08 INFO mapreduce.Job:  map 75% reduce 0%
19/02/13 08:13:10 INFO mapreduce.Job:  map 76% reduce 0%
19/02/13 08:13:13 INFO mapreduce.Job:  map 77% reduce 0%
19/02/13 08:13:15 INFO mapreduce.Job:  map 78% reduce 0%
19/02/13 08:13:16 INFO mapreduce.Job:  map 79% reduce 0%
19/02/13 08:13:17 INFO mapreduce.Job:  map 80% reduce 0%
19/02/13 08:13:22 INFO mapreduce.Job:  map 81% reduce 0%
19/02/13 08:13:24 INFO mapreduce.Job:  map 82% reduce 0%
19/02/13 08:13:25 INFO mapreduce.Job:  map 83% reduce 0%
19/02/13 08:13:26 INFO mapreduce.Job:  map 84% reduce 0%
19/02/13 08:13:34 INFO mapreduce.Job:  map 85% reduce 0%
19/02/13 08:13:37 INFO mapreduce.Job:  map 86% reduce 0%
19/02/13 08:13:39 INFO mapreduce.Job:  map 86% reduce 4%
19/02/13 08:13:41 INFO mapreduce.Job:  map 86% reduce 7%
19/02/13 08:13:43 INFO mapreduce.Job:  map 87% reduce 14%
19/02/13 08:13:44 INFO mapreduce.Job:  map 87% reduce 17%
19/02/13 08:13:45 INFO mapreduce.Job:  map 87% reduce 21%
19/02/13 08:13:46 INFO mapreduce.Job:  map 88% reduce 21%
19/02/13 08:13:49 INFO mapreduce.Job:  map 89% reduce 22%
19/02/13 08:13:51 INFO mapreduce.Job:  map 90% reduce 22%
19/02/13 08:13:54 INFO mapreduce.Job:  map 91% reduce 22%
19/02/13 08:13:56 INFO mapreduce.Job:  map 91% reduce 23%
19/02/13 08:13:58 INFO mapreduce.Job:  map 92% reduce 23%
19/02/13 08:14:00 INFO mapreduce.Job:  map 93% reduce 23%
19/02/13 08:14:04 INFO mapreduce.Job:  map 94% reduce 23%
19/02/13 08:14:07 INFO mapreduce.Job:  map 95% reduce 23%
19/02/13 08:14:09 INFO mapreduce.Job:  map 96% reduce 24%
19/02/13 08:14:13 INFO mapreduce.Job:  map 97% reduce 24%
19/02/13 08:14:16 INFO mapreduce.Job:  map 98% reduce 24%
19/02/13 08:14:19 INFO mapreduce.Job:  map 99% reduce 24%
19/02/13 08:14:21 INFO mapreduce.Job:  map 99% reduce 25%
19/02/13 08:14:22 INFO mapreduce.Job:  map 100% reduce 25%
19/02/13 08:14:25 INFO mapreduce.Job:  map 100% reduce 33%
19/02/13 08:14:26 INFO mapreduce.Job:  map 100% reduce 38%
19/02/13 08:14:27 INFO mapreduce.Job:  map 100% reduce 47%
19/02/13 08:14:29 INFO mapreduce.Job:  map 100% reduce 52%
19/02/13 08:14:31 INFO mapreduce.Job:  map 100% reduce 54%
19/02/13 08:14:32 INFO mapreduce.Job:  map 100% reduce 56%
19/02/13 08:14:33 INFO mapreduce.Job:  map 100% reduce 60%
19/02/13 08:14:34 INFO mapreduce.Job:  map 100% reduce 68%
19/02/13 08:14:35 INFO mapreduce.Job:  map 100% reduce 70%
19/02/13 08:14:37 INFO mapreduce.Job:  map 100% reduce 74%
19/02/13 08:14:38 INFO mapreduce.Job:  map 100% reduce 75%
19/02/13 08:14:39 INFO mapreduce.Job:  map 100% reduce 78%
19/02/13 08:14:40 INFO mapreduce.Job:  map 100% reduce 86%
19/02/13 08:14:43 INFO mapreduce.Job:  map 100% reduce 89%
19/02/13 08:14:44 INFO mapreduce.Job:  map 100% reduce 90%
19/02/13 08:14:46 INFO mapreduce.Job:  map 100% reduce 97%
19/02/13 08:14:52 INFO mapreduce.Job:  map 100% reduce 99%
19/02/13 08:14:54 INFO mapreduce.Job:  map 100% reduce 100%
19/02/13 08:14:54 INFO mapreduce.Job: Job job_1549984636723_0005 completed successfully
19/02/13 08:14:55 INFO mapreduce.Job: Counters: 50
	File System Counters
		FILE: Number of bytes read=4443659300
		FILE: Number of bytes written=8833739141
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=10000036600
		HDFS: Number of bytes written=10000000000
		HDFS: Number of read operations=924
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=16
	Job Counters 
		Launched map tasks=300
		Launched reduce tasks=8
		Data-local map tasks=298
		Rack-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=2211347
		Total time spent by all reduces in occupied slots (ms)=520134
		Total time spent by all map tasks (ms)=2211347
		Total time spent by all reduce tasks (ms)=520134
		Total vcore-milliseconds taken by all map tasks=2211347
		Total vcore-milliseconds taken by all reduce tasks=520134
		Total megabyte-milliseconds taken by all map tasks=2264419328
		Total megabyte-milliseconds taken by all reduce tasks=532617216
	Map-Reduce Framework
		Map input records=100000000
		Map output records=100000000
		Map output bytes=10200000000
		Map output materialized bytes=4342875515
		Input split bytes=36600
		Combine input records=0
		Combine output records=0
		Reduce input groups=100000000
		Reduce shuffle bytes=4342875515
		Reduce input records=100000000
		Reduce output records=100000000
		Spilled Records=200000000
		Shuffled Maps =2400
		Failed Shuffles=0
		Merged Map outputs=2400
		GC time elapsed (ms)=44904
		CPU time spent (ms)=1141560
		Physical memory (bytes) snapshot=158027747328
		Virtual memory (bytes) snapshot=486713552896
		Total committed heap usage (bytes)=178044010496
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=10000000000
	File Output Format Counters 
		Bytes Written=10000000000
19/02/13 08:14:55 INFO terasort.TeraSort: done

real	4m48.511s
user	0m6.619s
sys	0m0.289s


