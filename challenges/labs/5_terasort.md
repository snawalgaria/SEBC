[200~[hdfs@ip-172-32-1-71 java]$ kinit hdfs
Password for hdfs@SNAWALGARIA: 
[hdfs@ip-172-32-1-71 java]$ pwd
/usr/lib/java
[hdfs@ip-172-32-1-71 java]$ time hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-examples.jar terasort /user/rocky/teragen /user/rocky/terasort
19/02/15 11:54:12 INFO terasort.TeraSort: starting
19/02/15 11:54:13 INFO hdfs.DFSClient: Created token for hdfs: HDFS_DELEGATION_TOKEN owner=hdfs@SNAWALGARIA, renewer=yarn, realUser=, issueDate=1550231653813, maxDate=1550836453813, sequenceNumber=1, masterKeyId=2 on 172.32.1.156:8020
19/02/15 11:54:13 INFO security.TokenCache: Got dt for hdfs://ip-172-32-1-156.eu-west-1.compute.internal:8020; Kind: HDFS_DELEGATION_TOKEN, Service: 172.32.1.156:8020, Ident: (token for hdfs: HDFS_DELEGATION_TOKEN owner=hdfs@SNAWALGARIA, renewer=yarn, realUser=, issueDate=1550231653813, maxDate=1550836453813, sequenceNumber=1, masterKeyId=2)
19/02/15 11:54:13 INFO input.FileInputFormat: Total input paths to process : 8
Spent 241ms computing base-splits.
Spent 3ms computing TeraScheduler splits.
Computing input splits took 244ms
Sampling 10 splits of 160
Making 8 from 100000 sampled records
Computing parititions took 585ms
Spent 831ms computing partitions.
19/02/15 11:54:14 INFO client.RMProxy: Connecting to ResourceManager at ip-172-32-1-156.eu-west-1.compute.internal/172.32.1.156:8032
19/02/15 11:54:14 INFO mapreduce.JobSubmitter: number of splits:160
19/02/15 11:54:14 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1550231484938_0001
19/02/15 11:54:14 INFO mapreduce.JobSubmitter: Kind: HDFS_DELEGATION_TOKEN, Service: 172.32.1.156:8020, Ident: (token for hdfs: HDFS_DELEGATION_TOKEN owner=hdfs@SNAWALGARIA, renewer=yarn, realUser=, issueDate=1550231653813, maxDate=1550836453813, sequenceNumber=1, masterKeyId=2)
19/02/15 11:54:15 INFO impl.YarnClientImpl: Submitted application application_1550231484938_0001
19/02/15 11:54:15 INFO mapreduce.Job: The url to track the job: http://ip-172-32-1-156.eu-west-1.compute.internal:8088/proxy/application_1550231484938_0001/
19/02/15 11:54:15 INFO mapreduce.Job: Running job: job_1550231484938_0001
19/02/15 11:54:17 INFO mapreduce.Job: Job job_1550231484938_0001 running in uber mode : false
19/02/15 11:54:17 INFO mapreduce.Job:  map 0% reduce 0%
19/02/15 11:54:17 INFO mapreduce.Job: Job job_1550231484938_0001 failed with state FAILED due to: Application application_1550231484938_0001 failed 2 times due to AM Container for appattempt_1550231484938_0001_000002 exited with  exitCode: -1000
For more detailed output, check application tracking page:http://ip-172-32-1-156.eu-west-1.compute.internal:8088/proxy/application_1550231484938_0001/Then, click on links to logs of each attempt.
Diagnostics: Application application_1550231484938_0001 initialization failed (exitCode=255) with output: main : command provided 0
main : run as user is hdfs
main : requested yarn user is hdfs
Requested user hdfs is not whitelisted and has id 995,which is below the minimum allowed 1000

Failing this attempt. Failing the application.
19/02/15 11:54:17 INFO mapreduce.Job: Counters: 0
19/02/15 11:54:17 INFO terasort.TeraSort: done

real	0m5.611s
user	0m6.306s
sys	0m0.310s
[hdfs@ip-172-32-1-71 java]$ sudo -i

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for hdfs: 

[hdfs@ip-172-32-1-71 java]$ 
[hdfs@ip-172-32-1-71 java]$ exit

