# What is ubertask optimization?
Ubertask optimization runs "sufficiently small" jobs sequentially within a single JVM. The size (how "small" the job has to be) is defined by the mapreduce.job.ubertask.maxmaps, mapreduce.job.ubertask.maxreduces, and mapreduce.job.ubertask.maxbytes settings.

# Where in CM is the Kerberos Security Realm value displayed?
Administration -> Settings -> Kerberos -> Kerberos Security Realm (default_realm)

# Which CDH service(s) host a property for enabling Kerberos authentication?
All the core services (HDFS, YARN, Zookeeper, Hive, Hue, Oozie, Cloudera Management Service) can enable Kerberos authentication.

# How do you upgrade the CM agents?
CM agents can be upgraded using Cloudera Manager wizard or manually (install new version on the OS on each node).

To upgrade through Cloudera Manager run: Hosts -> All Hosts -> Re-run Upgrade Wizard.
To upgrade manually:
-> Modify cloudera-manager.repo file on each node to point to the new version
-> Stop the agent (cloudera-scm-agent)
-> Upgrade agent packages (using f.ex yum)
-> Verify the version and start the agent

# Give the tsquery statement used to chart Hue's CPU utilization?
Available Hue metrics: https://www.cloudera.com/documentation/enterprise/5-8-x/topics/cm_metrics_hue_server.html
Hue's CPU utilization chart uses: cpu_system_rate + cpu_user_rate
tsquery:
```
select (cpu_system_rate+cpu_user_rate) where serviceName=hue
```

# Name all the roles that make up the Hive service
* Hive metastore - Provides metastore services when Hive is configured with a remote metastore.
* HiveServer2 - Enables remote clients to run Hive queries
* WebHCat - HCatalog is a table and storage management layer for Hadoop that makes the same table information available to Hive, Pig, MapReduce, and Sqoop.
* Hive gateway

# What steps must be completed before integrating Cloudera Manager with Kerberos?

* Working KDC needs to be available. Cloudera Manager supports MIT KDC and Active Directory.
* The KDC should be configured to have non-zero ticket lifetime and renewal lifetime.
* Kerberos client libraries (krb5-workstation, krb5-libs for RHEL) should be installed on ALL hosts.
* Cloudera Manager needs an account that has permissions to create other accounts in the KDC.
* If AES-256 Encryption is used, install the JCE Policy File.
* Get or create a Kerberos Principal for the Cloudera Manager Server.
