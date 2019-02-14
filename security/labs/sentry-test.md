```
kadmin.local:  addprinc admin
WARNING: no policy specified for admin@SAURABH.COM; defaulting to no policy
Enter password for principal "admin@SAURABH.COM": 
Re-enter password for principal "admin@SAURABH.COM": 
Principal "admin@SAURABH.COM" created.
kadmin.local:  exit
[root@ip-172-32-1-71 etc]# beeline
Beeline version 1.1.0-cdh5.15.2 by Apache Hive
beeline> connect jdbc:hive2://localhost:10000/default;principal=hive/@SAURABH[root@ip-172-32-1-71 etc]# c^C
[root@ip-172-32-1-71 etc]# 
[root@ip-172-32-1-71 etc]# kinit admin
Password for admin@SAURABH.COM: 
[root@ip-172-32-1-71 etc]# beeline
Beeline version 1.1.0-cdh5.15.2 by Apache Hive

beeline> connect jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
. . . .> ;
No current connection
beeline> !connect jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
scan complete in 1ms
Connecting to jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
Connected to: Apache Hive (version 1.1.0-cdh5.15.2)
Driver: Hive JDBC (version 1.1.0-cdh5.15.2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://172.32.1.185:10000/default> SHOW TABLES
. . . . . . . . . . . . . . . . . . . . . > ;
INFO  : Compiling command(queryId=hive_20190214121414_b13543a7-039b-4b7f-9742-24520f9cf5af): SHOW TABLES
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20190214121414_b13543a7-039b-4b7f-9742-24520f9cf5af); Time taken: 0.464 seconds
INFO  : Executing command(queryId=hive_20190214121414_b13543a7-039b-4b7f-9742-24520f9cf5af): SHOW TABLES
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214121414_b13543a7-039b-4b7f-9742-24520f9cf5af); Time taken: 0.277 seconds
INFO  : OK
+-----------+--+
| tab_name  |
+-----------+--+
+-----------+--+
No rows selected (2.001 seconds)
0: jdbc:hive2://172.32.1.185:10000/default>


[root@ip-172-32-1-71 ~]# groupadd selector
[root@ip-172-32-1-71 ~]# groupadd inserters
[root@ip-172-32-1-71 ~]# sudo useradd -u 1100 -g selector george
[root@ip-172-32-1-71 ~]# sudo useradd -u 1200 -g inserters ferdinand
[root@ip-172-32-1-71 ~]# kadmin.local
Authenticating as principal hdfs/admin@SAURABH.COM with password.
kadmin.local:  addprinc george
WARNING: no policy specified for george@SAURABH.COM; defaulting to no policy
Enter password for principal "george@SAURABH.COM": 
Re-enter password for principal "george@SAURABH.COM": 
Principal "george@SAURABH.COM" created.
kadmin.local:  addprinc ferdinand
WARNING: no policy specified for ferdinand@SAURABH.COM; defaulting to no policy
Enter password for principal "ferdinand@SAURABH.COM": 
Re-enter password for principal "ferdinand@SAURABH.COM": 
Principal "ferdinand@SAURABH.COM" created.
kadmin.local:  exit
[root@ip-172-32-1-71 ~]# exit
logout
[root@ip-172-32-1-71 etc]# exit
logout
[ec2-user@ip-172-32-1-71 etc]$ kinit hdfs
Password for hdfs@SAURABH.COM: 
[ec2-user@ip-172-32-1-71 etc]$ 
[ec2-user@ip-172-32-1-71 etc]$ beeline
Beeline version 1.1.0-cdh5.15.2 by Apache Hive
beeline> !connect jdbc:hive2://localhost:10000/default;principal=hive/fdqn@REALM.COM
scan complete in 2ms
Connecting to jdbc:hive2://localhost:10000/default;principal=hive/fdqn@REALM.COM
Could not open connection to the HS2 server. Please check the server URI and if the URI is correct, then ask the administrator to check the server status.
Error: Could not open client transport with JDBC Uri: jdbc:hive2://localhost:10000/default;principal=hive/fdqn@REALM.COM: java.net.ConnectException: Connection refused (state=08S01,code=0)
beeline> !connect jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
Connecting to jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
Connected to: Apache Hive (version 1.1.0-cdh5.15.2)
Driver: Hive JDBC (version 1.1.0-cdh5.15.2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://172.32.1.185:10000/default> 
0: jdbc:hive2://172.32.1.185:10000/default> 
0: jdbc:hive2://172.32.1.185:10000/default> 
0: jdbc:hive2://172.32.1.185:10000/default> 
0: jdbc:hive2://172.32.1.185:10000/default> 
0: jdbc:hive2://172.32.1.185:10000/default> CREATE ROLE reads;
INFO  : Compiling command(queryId=hive_20190214124242_45eceb2a-ad41-4175-8b9c-8f8ba2ff0c68): CREATE ROLE reads
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124242_45eceb2a-ad41-4175-8b9c-8f8ba2ff0c68); Time taken: 0.057 seconds
INFO  : Executing command(queryId=hive_20190214124242_45eceb2a-ad41-4175-8b9c-8f8ba2ff0c68): CREATE ROLE reads
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124242_45eceb2a-ad41-4175-8b9c-8f8ba2ff0c68); Time taken: 0.022 seconds
INFO  : OK
No rows affected (0.116 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> create role writes;
INFO  : Compiling command(queryId=hive_20190214124242_850813df-64eb-43a5-8d05-b2af5e384d7c): create role writes
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124242_850813df-64eb-43a5-8d05-b2af5e384d7c); Time taken: 0.048 seconds
INFO  : Executing command(queryId=hive_20190214124242_850813df-64eb-43a5-8d05-b2af5e384d7c): create role writes
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124242_850813df-64eb-43a5-8d05-b2af5e384d7c); Time taken: 0.007 seconds
INFO  : OK
No rows affected (0.065 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> grant select on database default to role reads;
INFO  : Compiling command(queryId=hive_20190214124242_7648794c-8602-4dab-b8c5-5807d4c3d226): grant select on database default to role reads
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124242_7648794c-8602-4dab-b8c5-5807d4c3d226); Time taken: 0.056 seconds
INFO  : Executing command(queryId=hive_20190214124242_7648794c-8602-4dab-b8c5-5807d4c3d226): grant select on database default to role reads
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124242_7648794c-8602-4dab-b8c5-5807d4c3d226); Time taken: 0.011 seconds
INFO  : OK
No rows affected (0.077 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> grant role reads to group selector;
INFO  : Compiling command(queryId=hive_20190214124242_cfa1ddc5-dd55-4a53-816b-ba49a0e5dbf4): grant role reads to group selector
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124242_cfa1ddc5-dd55-4a53-816b-ba49a0e5dbf4); Time taken: 0.061 seconds
INFO  : Executing command(queryId=hive_20190214124242_cfa1ddc5-dd55-4a53-816b-ba49a0e5dbf4): grant role reads to group selector
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124242_cfa1ddc5-dd55-4a53-816b-ba49a0e5dbf4); Time taken: 0.009 seconds
INFO  : OK
No rows affected (0.078 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> revoke all on database default from role writes;
INFO  : Compiling command(queryId=hive_20190214124343_7c3f1853-9d0e-49b0-89ed-ddf0707088ae): revoke all on database default from role writes
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124343_7c3f1853-9d0e-49b0-89ed-ddf0707088ae); Time taken: 0.049 seconds
INFO  : Executing command(queryId=hive_20190214124343_7c3f1853-9d0e-49b0-89ed-ddf0707088ae): revoke all on database default from role writes
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124343_7c3f1853-9d0e-49b0-89ed-ddf0707088ae); Time taken: 0.034 seconds
INFO  : OK
No rows affected (0.093 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> grant insert on default.sample_07 to role writes;
INFO  : Compiling command(queryId=hive_20190214124343_21ee6214-7fea-4b80-bc6f-c02d73e06272): grant insert on default.sample_07 to role writes
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124343_21ee6214-7fea-4b80-bc6f-c02d73e06272); Time taken: 0.05 seconds
INFO  : Executing command(queryId=hive_20190214124343_21ee6214-7fea-4b80-bc6f-c02d73e06272): grant insert on default.sample_07 to role writes
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124343_21ee6214-7fea-4b80-bc6f-c02d73e06272); Time taken: 0.01 seconds
INFO  : OK
No rows affected (0.069 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> grant role writes to group inserters;
INFO  : Compiling command(queryId=hive_20190214124444_793230e3-dbdc-4c18-a520-8207a60ae399): grant role writes to group inserters
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20190214124444_793230e3-dbdc-4c18-a520-8207a60ae399); Time taken: 0.048 seconds
INFO  : Executing command(queryId=hive_20190214124444_793230e3-dbdc-4c18-a520-8207a60ae399): grant role writes to group inserters
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214124444_793230e3-dbdc-4c18-a520-8207a60ae399); Time taken: 0.008 seconds
INFO  : OK



[ec2-user@ip-172-32-1-71 etc]$ kinit george
Password for george@SAURABH.COM: 
[ec2-user@ip-172-32-1-71 etc]$ beeline
Beeline version 1.1.0-cdh5.15.2 by Apache Hive
beeline> !connect jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
scan complete in 1ms
Connecting to jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
Connected to: Apache Hive (version 1.1.0-cdh5.15.2)
Driver: Hive JDBC (version 1.1.0-cdh5.15.2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://172.32.1.185:10000/default> show tables;
INFO  : Compiling command(queryId=hive_20190214131313_b667cd8d-6b08-447b-8300-98d313ebbabe): show tables
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20190214131313_b667cd8d-6b08-447b-8300-98d313ebbabe); Time taken: 0.057 seconds
INFO  : Executing command(queryId=hive_20190214131313_b667cd8d-6b08-447b-8300-98d313ebbabe): show tables
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214131313_b667cd8d-6b08-447b-8300-98d313ebbabe); Time taken: 0.08 seconds
INFO  : OK
+------------+--+
|  tab_name  |
+------------+--+
| sample_07  |
| sample_08  |
+------------+--+
2 rows selected (0.206 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> [ec2-user@ip-172-32-1-71 etc]$ 
[ec2-user@ip-172-32-1-71 etc]$ kinit ferdinand
Password for ferdinand@SAURABH.COM: 
[ec2-user@ip-172-32-1-71 etc]$ beeline
Beeline version 1.1.0-cdh5.15.2 by Apache Hive
beeline> !connect jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
scan complete in 2ms
Connecting to jdbc:hive2://172.32.1.185:10000/default;principal=hive/ip-172-32-1-185.eu-west-1.compute.internal@SAURABH.COM
Connected to: Apache Hive (version 1.1.0-cdh5.15.2)
Driver: Hive JDBC (version 1.1.0-cdh5.15.2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://172.32.1.185:10000/default> show tables
. . . . . . . . . . . . . . . . . . . . . > ;
INFO  : Compiling command(queryId=hive_20190214131515_0fcb0347-910a-461a-8c08-48b6e6adc7d0): show tables
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20190214131515_0fcb0347-910a-461a-8c08-48b6e6adc7d0); Time taken: 0.077 seconds
INFO  : Executing command(queryId=hive_20190214131515_0fcb0347-910a-461a-8c08-48b6e6adc7d0): show tables
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20190214131515_0fcb0347-910a-461a-8c08-48b6e6adc7d0); Time taken: 0.089 seconds
INFO  : OK
+------------+--+
|  tab_name  |
+------------+--+
| sample_07  |
+------------+--+
1 row selected (0.244 seconds)
0: jdbc:hive2://172.32.1.185:10000/default> 

 

