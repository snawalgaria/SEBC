sudo -u hdfs hadoop distcp hdfs://ec2-18-203-235-248.eu-west-1.compute.amazonaws.com:8020/user/diegomarcheselli/teragen-distcp  hdfs://ec2-34-247-13-48.eu-west-1.compute.amazonaws.com:8020/tmp/snawalgaria/
19/02/13 08:36:54 INFO tools.OptionsParser: parseChunkSize: blocksperchunk false
19/02/13 08:36:55 INFO tools.DistCp: Input Options: DistCpOptions{atomicCommit=false, syncFolder=false, deleteMissing=false, ignoreFailures=false, overwrite=false, append=false, useDiff=false, useRdiff=false, fromSnapshot=null, toSnapshot=null, skipCRC=false, blocking=true, numListstatusThreads=0, maxMaps=20, mapBandwidth=100, sslConfigurationFile='null', copyStrategy='uniformsize', preserveStatus=[], preserveRawXattrs=false, atomicWorkPath=null, logPath=null, sourceFileListing=null, sourcePaths=[hdfs://ec2-18-203-235-248.eu-west-1.compute.amazonaws.com:8020/user/diegomarcheselli/teragen-distcp], targetPath=hdfs://ec2-34-247-13-48.eu-west-1.compute.amazonaws.com:8020/tmp/snawalgaria, targetPathExists=true, filtersFile='null', blocksPerChunk=0, copyBufferSize=8192}
19/02/13 08:36:55 INFO client.RMProxy: Connecting to ResourceManager at ip-172-32-1-185.eu-west-1.compute.internal/172.32.1.185:8032
19/02/13 08:36:55 INFO tools.SimpleCopyListing: Paths (files+dirs) cnt = 4; dirCnt = 1
19/02/13 08:36:55 INFO tools.SimpleCopyListing: Build file listing completed.
19/02/13 08:36:55 INFO Configuration.deprecation: io.sort.mb is deprecated. Instead, use mapreduce.task.io.sort.mb
19/02/13 08:36:55 INFO Configuration.deprecation: io.sort.factor is deprecated. Instead, use mapreduce.task.io.sort.factor
19/02/13 08:36:55 INFO tools.DistCp: Number of paths in the copy list: 4
19/02/13 08:36:55 INFO tools.DistCp: Number of paths in the copy list: 4
19/02/13 08:36:55 INFO client.RMProxy: Connecting to ResourceManager at ip-172-32-1-185.eu-west-1.compute.internal/172.32.1.185:8032
19/02/13 08:36:55 INFO mapreduce.JobSubmitter: number of splits:4
19/02/13 08:36:56 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1549984636723_0007
19/02/13 08:36:56 INFO impl.YarnClientImpl: Submitted application application_1549984636723_0007
19/02/13 08:36:56 INFO mapreduce.Job: The url to track the job: http://ip-172-32-1-185.eu-west-1.compute.internal:8088/proxy/application_1549984636723_0007/
19/02/13 08:36:56 INFO tools.DistCp: DistCp job-id: job_1549984636723_0007
19/02/13 08:36:56 INFO mapreduce.Job: Running job: job_1549984636723_0007
19/02/13 08:37:01 INFO mapreduce.Job: Job job_1549984636723_0007 running in uber mode : false
19/02/13 08:37:01 INFO mapreduce.Job:  map 0% reduce 0%
19/02/13 08:37:07 INFO mapreduce.Job:  map 25% reduce 0%
19/02/13 08:37:08 INFO mapreduce.Job:  map 50% reduce 0%
19/02/13 08:37:10 INFO mapreduce.Job:  map 75% reduce 0%
19/02/13 08:37:11 INFO mapreduce.Job:  map 100% reduce 0%
19/02/13 08:37:11 INFO mapreduce.Job: Job job_1549984636723_0007 completed successfully
19/02/13 08:37:11 INFO mapreduce.Job: Counters: 33
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=621544
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=500002692
		HDFS: Number of bytes written=500000000
		HDFS: Number of read operations=59
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=15
	Job Counters 
		Launched map tasks=4
		Other local map tasks=4
		Total time spent by all maps in occupied slots (ms)=20594
		Total time spent by all reduces in occupied slots (ms)=0
		Total time spent by all map tasks (ms)=20594
		Total vcore-milliseconds taken by all map tasks=20594
		Total megabyte-milliseconds taken by all map tasks=21088256
	Map-Reduce Framework
		Map input records=4
		Map output records=0
		Input split bytes=460
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=230
		CPU time spent (ms)=7230
		Physical memory (bytes) snapshot=969248768
		Virtual memory (bytes) snapshot=6338174976
		Total committed heap usage (bytes)=1479540736
	File Input Format Counters 
		Bytes Read=2232
	File Output Format Counters 
		Bytes Written=0
	DistCp Counters
		Bytes Copied=500000000
		Bytes Expected=500000000
		Files Copied=4



