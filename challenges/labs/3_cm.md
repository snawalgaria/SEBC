You have mail in /var/spool/mail/root
[root@ip-172-32-1-156 parcels]# sudo hdfs hdfs dfs -ls
Error: Could not find or load main class hdfs
[root@ip-172-32-1-156 parcels]# hdfs dfs -ls
ls: `.': No such file or directory
[root@ip-172-32-1-156 parcels]# hdfs dfs -ls /
Found 2 items
drwxrwxrwt   - hdfs supergroup          0 2019-02-15 10:32 /tmp
drwxr-xr-x   - hdfs supergroup          0 2019-02-15 10:35 /user
[root@ip-172-32-1-156 parcels]# hdfs dfs -mkdir /user/rocky
mkdir: Permission denied: user=root, access=WRITE, inode="/user":hdfs:supergroup:drwxr-xr-x
[root@ip-172-32-1-156 parcels]# su hdfs
[hdfs@ip-172-32-1-156 parcels]$ 
[hdfs@ip-172-32-1-156 parcels]$ 
[hdfs@ip-172-32-1-156 parcels]$ hdfs dfs -mkdir /user/rocky/
[hdfs@ip-172-32-1-156 parcels]$ su denali
Password: 
su: Authentication failure
[hdfs@ip-172-32-1-156 parcels]$ hdfs dfs -mkdir /user/denali/
[hdfs@ip-172-32-1-156 parcels]$ 
[hdfs@ip-172-32-1-156 parcels]$ 
{
  "items" : [ {
    "hostId" : "4643e159-94f3-40b6-b4fa-429bb1a73dca",
    "ipAddress" : "172.32.1.156",
    "hostname" : "ip-172-32-1-156.eu-west-1.compute.internal",
    "rackId" : "/default",
    "hostUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/hostRedirect/4643e159-94f3-40b6-b4fa-429bb1a73dca",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "commissionState" : "COMMISSIONED",
    "numCores" : 4,
    "numPhysicalCores" : 2,
    "totalPhysMemBytes" : 16170377216
  }, {
    "hostId" : "818ae74a-91d8-404e-9ee3-33d1270137f7",
    "ipAddress" : "172.32.1.185",
    "hostname" : "ip-172-32-1-185.eu-west-1.compute.internal",
    "rackId" : "/default",
    "hostUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/hostRedirect/818ae74a-91d8-404e-9ee3-33d1270137f7",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "commissionState" : "COMMISSIONED",
    "numCores" : 4,
    "numPhysicalCores" : 2,
    "totalPhysMemBytes" : 16170377216
  }, {
    "hostId" : "2665dbeb-7a35-433c-98ee-f874c956ad96",
    "ipAddress" : "172.32.1.230",
    "hostname" : "ip-172-32-1-230.eu-west-1.compute.internal",
    "rackId" : "/default",
    "hostUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/hostRedirect/2665dbeb-7a35-433c-98ee-f874c956ad96",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "commissionState" : "COMMISSIONED",
    "numCores" : 4,
    "numPhysicalCores" : 2,
    "totalPhysMemBytes" : 16170369024
  }, {
    "hostId" : "9a47ffcd-977e-41f9-ba53-3c094e10f826",
    "ipAddress" : "172.32.1.235",
    "hostname" : "ip-172-32-1-235.eu-west-1.compute.internal",
    "rackId" : "/default",
    "hostUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/hostRedirect/9a47ffcd-977e-41f9-ba53-3c094e10f826",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "commissionState" : "COMMISSIONED",
    "numCores" : 4,
    "numPhysicalCores" : 2,
    "totalPhysMemBytes" : 16170377216
  }, {
    "hostId" : "b4e21462-869b-4dab-afa5-66163ec1666c",
    "ipAddress" : "172.32.1.71",
    "hostname" : "ip-172-32-1-71.eu-west-1.compute.internal",
    "rackId" : "/default",
    "hostUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/hostRedirect/b4e21462-869b-4dab-afa5-66163ec1666c",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "commissionState" : "COMMISSIONED",
    "numCores" : 4,
    "numPhysicalCores" : 2,
    "totalPhysMemBytes" : 16170369024
  } ]
}

  "items" : [ {
    "name" : "zookeeper",
    "type" : "ZOOKEEPER",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/zookeeper",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "ZOOKEEPER_CANARY_HEALTH",
      "summary" : "GOOD"
    }, {
      "name" : "ZOOKEEPER_SERVERS_HEALTHY",
      "summary" : "GOOD"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "ZooKeeper"
  }, {
    "name" : "oozie",
    "type" : "OOZIE",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/oozie",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "OOZIE_OOZIE_SERVERS_HEALTHY",
      "summary" : "GOOD"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "Oozie"
  }, {
    "name" : "hue",
    "type" : "HUE",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/hue",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "HUE_HUE_SERVERS_HEALTHY",
      "summary" : "GOOD"
    }, {
      "name" : "HUE_LOAD_BALANCER_HEALTHY",
      "summary" : "GOOD"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "Hue"
  }, {
    "name" : "hdfs",
    "type" : "HDFS",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/hdfs",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "HDFS_BLOCKS_WITH_CORRUPT_REPLICAS",
      "summary" : "GOOD"
    }, {
      "name" : "HDFS_CANARY_HEALTH",
      "summary" : "GOOD"
    }, {
      "name" : "HDFS_DATA_NODES_HEALTHY",
      "summary" : "GOOD"
    }, {
      "name" : "HDFS_FREE_SPACE_REMAINING",
      "summary" : "GOOD"
    }, {
      "name" : "HDFS_HA_NAMENODE_HEALTH",
      "summary" : "GOOD"
    }, {
      "name" : "HDFS_MISSING_BLOCKS",
      "summary" : "GOOD"
    }, {
      "name" : "HDFS_UNDER_REPLICATED_BLOCKS",
      "summary" : "GOOD"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "HDFS"
  }, {
    "name" : "impala",
    "type" : "IMPALA",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/impala",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "IMPALA_CATALOGSERVER_HEALTH",
      "summary" : "GOOD"
    }, {
      "name" : "IMPALA_IMPALADS_HEALTHY",
      "summary" : "GOOD"
    }, {
      "name" : "IMPALA_STATESTORE_HEALTH",
      "summary" : "GOOD"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "Impala"
  }, {
    "name" : "yarn",
    "type" : "YARN",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/yarn",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "YARN_JOBHISTORY_HEALTH",
      "summary" : "GOOD"
    }, {
      "name" : "YARN_NODE_MANAGERS_HEALTHY",
      "summary" : "GOOD"
    }, {
      "name" : "YARN_RESOURCEMANAGERS_HEALTH",
      "summary" : "GOOD"
    }, {
      "name" : "YARN_USAGE_AGGREGATION_HEALTH",
      "summary" : "DISABLED"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "YARN (MR2 Included)"
  }, {
    "name" : "hive",
    "type" : "HIVE",
    "clusterRef" : {
      "clusterName" : "cluster"
    },
    "serviceUrl" : "http://ip-172-32-1-156.eu-west-1.compute.internal:7180/cmf/serviceRedirect/hive",
    "serviceState" : "STARTED",
    "healthSummary" : "GOOD",
    "healthChecks" : [ {
      "name" : "HIVE_HIVEMETASTORES_HEALTHY",
      "summary" : "GOOD"
    }, {
      "name" : "HIVE_HIVESERVER2S_HEALTHY",
      "summary" : "GOOD"
    } ],
    "configStalenessStatus" : "FRESH",
    "clientConfigStalenessStatus" : "FRESH",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "displayName" : "Hive"
  } ]
}
[hdfs@ip-172-32-1-156 parcels]$ hdfs dfs -ls /user/
Found 8 items
drwxr-xr-x   - admin  admin               0 2019-02-15 10:35 /user/admin
drwxr-xr-x   - hdfs   supergroup          0 2019-02-15 10:38 /user/denali
drwxrwxrwx   - mapred hadoop              0 2019-02-15 10:31 /user/history
drwxrwxr-t   - hive   hive                0 2019-02-15 10:32 /user/hive
drwxrwxr-x   - hue    hue                 0 2019-02-15 10:33 /user/hue
drwxrwxr-x   - impala impala              0 2019-02-15 10:32 /user/impala
drwxrwxr-x   - oozie  oozie               0 2019-02-15 10:33 /user/oozie
drwxr-xr-x   - hdfs   supergroup          0 2019-02-15 10:37 /user/rocky

