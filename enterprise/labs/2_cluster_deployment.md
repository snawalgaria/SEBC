{
  "timestamp" : "2019-02-14T14:12:37.523Z",
  "clusters" : [ {
    "name" : "snawalgaria",
    "version" : "CDH5",
    "services" : [ {
      "name" : "hive",
      "type" : "HIVE",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "HIVEMETASTORE",
          "items" : [ {
            "name" : "hive_enable_db_notification",
            "value" : "true"
          }, {
            "name" : "hive_metastore_java_heapsize",
            "value" : "1059061760"
          }, {
            "name" : "hive_metastore_server_max_message_size",
            "value" : "105906176"
          } ]
        }, {
          "roleType" : "HIVESERVER2",
          "items" : [ {
            "name" : "hiveserver2_enable_impersonation",
            "value" : "false"
          }, {
            "name" : "hiveserver2_java_heapsize",
            "value" : "1059061760"
          }, {
            "name" : "hiveserver2_spark_driver_memory",
            "value" : "966367641"
          }, {
            "name" : "hiveserver2_spark_executor_cores",
            "value" : "4"
          }, {
            "name" : "hiveserver2_spark_executor_memory",
            "value" : "912680550"
          }, {
            "name" : "hiveserver2_spark_yarn_driver_memory_overhead",
            "value" : "102"
          }, {
            "name" : "hiveserver2_spark_yarn_executor_memory_overhead",
            "value" : "153"
          } ]
        } ],
        "items" : [ {
          "name" : "hive_metastore_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal"
        }, {
          "name" : "hive_metastore_database_password",
          "value" : "sebc"
        }, {
          "name" : "hive_proxy_user_groups_list",
          "value" : "hue,hive,sentry"
        }, {
          "name" : "mapreduce_yarn_service",
          "value" : "yarn"
        }, {
          "name" : "sentry_service",
          "value" : "sentry"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "hive-GATEWAY-4c295c24bb561564fe89fde870e525d6",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-7c486a97fd3992d66490e6d8d6a5ce09",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-8d800fdbd92a4e8cd7115087e2763453",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "a2bbaceb-4dee-4022-a507-3830954716f5"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-b424d1848b728a80118ace82135b2a2f",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-f6b97aa6f19a22b0a57f6c1bc2ecf451",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "beb7ba14-216f-40c7-bb7a-76bf93cd1685"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-HIVEMETASTORE-b424d1848b728a80118ace82135b2a2f",
        "type" : "HIVEMETASTORE",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "1obuj1eoxfas756afxxat23vo"
          } ]
        }
      }, {
        "name" : "hive-HIVESERVER2-b424d1848b728a80118ace82135b2a2f",
        "type" : "HIVESERVER2",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "alij3dv40z6mi2mwx9p2wkmim"
          } ]
        }
      } ],
      "displayName" : "Hive"
    }, {
      "name" : "zookeeper",
      "type" : "ZOOKEEPER",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "SERVER",
          "items" : [ {
            "name" : "zookeeper_server_java_heapsize",
            "value" : "1059061760"
          } ]
        } ],
        "items" : [ {
          "name" : "enableSecurity",
          "value" : "true"
        } ]
      },
      "roles" : [ {
        "name" : "zookeeper-SERVER-4c295c24bb561564fe89fde870e525d6",
        "type" : "SERVER",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "5epz7wqupavfmsmyf6g17jko5"
          }, {
            "name" : "serverId",
            "value" : "2"
          } ]
        }
      }, {
        "name" : "zookeeper-SERVER-8d800fdbd92a4e8cd7115087e2763453",
        "type" : "SERVER",
        "hostRef" : {
          "hostId" : "a2bbaceb-4dee-4022-a507-3830954716f5"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "7x0sum7ckqdipbl8vkfd0an7h"
          }, {
            "name" : "serverId",
            "value" : "3"
          } ]
        }
      }, {
        "name" : "zookeeper-SERVER-b424d1848b728a80118ace82135b2a2f",
        "type" : "SERVER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "8shui05bl2onuwu444dckltl7"
          }, {
            "name" : "serverId",
            "value" : "1"
          } ]
        }
      } ],
      "displayName" : "ZooKeeper"
    }, {
      "name" : "hue",
      "type" : "HUE",
      "config" : {
        "roleTypeConfigs" : [ ],
        "items" : [ {
          "name" : "database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal"
        }, {
          "name" : "database_password",
          "value" : "sebc"
        }, {
          "name" : "database_type",
          "value" : "mysql"
        }, {
          "name" : "hive_service",
          "value" : "hive"
        }, {
          "name" : "hue_webhdfs",
          "value" : "hdfs-NAMENODE-b424d1848b728a80118ace82135b2a2f"
        }, {
          "name" : "oozie_service",
          "value" : "oozie"
        }, {
          "name" : "sentry_service",
          "value" : "sentry"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "hue-HUE_LOAD_BALANCER-b424d1848b728a80118ace82135b2a2f",
        "type" : "HUE_LOAD_BALANCER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "1370aw8ixj9z4zi6oy1yfgyi"
          } ]
        }
      }, {
        "name" : "hue-HUE_SERVER-b424d1848b728a80118ace82135b2a2f",
        "type" : "HUE_SERVER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "navmetadataserver_cmdb_password",
            "value" : "c6451ab4-44ec-4c59-bc91-b582f077cda5"
          }, {
            "name" : "role_jceks_password",
            "value" : "3h51j8es42wyihbzfdm1winpv"
          }, {
            "name" : "secret_key",
            "value" : "7eiGDDhT1iJyoYV3qGbeDEwXnCaEvv"
          } ]
        }
      }, {
        "name" : "hue-KT_RENEWER-b424d1848b728a80118ace82135b2a2f",
        "type" : "KT_RENEWER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "23k6daqcve2mp5ljdmpgwujo4"
          } ]
        }
      } ],
      "displayName" : "Hue"
    }, {
      "name" : "oozie",
      "type" : "OOZIE",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "OOZIE_SERVER",
          "items" : [ {
            "name" : "oozie_database_host",
            "value" : "ip-172-32-1-71.eu-west-1.compute.internal"
          }, {
            "name" : "oozie_database_password",
            "value" : "sebc"
          }, {
            "name" : "oozie_database_type",
            "value" : "mysql"
          }, {
            "name" : "oozie_database_user",
            "value" : "oozie"
          }, {
            "name" : "oozie_java_heapsize",
            "value" : "1059061760"
          } ]
        } ],
        "items" : [ {
          "name" : "hive_service",
          "value" : "hive"
        }, {
          "name" : "mapreduce_yarn_service",
          "value" : "yarn"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "oozie-OOZIE_SERVER-b424d1848b728a80118ace82135b2a2f",
        "type" : "OOZIE_SERVER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "9xydxrm3k0giax4fqkwl5bsog"
          } ]
        }
      } ],
      "displayName" : "Oozie"
    }, {
      "name" : "yarn",
      "type" : "YARN",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "GATEWAY",
          "items" : [ {
            "name" : "mapred_reduce_tasks",
            "value" : "8"
          }, {
            "name" : "mapred_submit_replication",
            "value" : "3"
          } ]
        }, {
          "roleType" : "JOBHISTORY",
          "items" : [ {
            "name" : "mr2_jobhistory_java_heapsize",
            "value" : "1059061760"
          } ]
        }, {
          "roleType" : "NODEMANAGER",
          "items" : [ {
            "name" : "yarn_nodemanager_heartbeat_interval_ms",
            "value" : "100"
          }, {
            "name" : "yarn_nodemanager_local_dirs",
            "value" : "/yarn/nm"
          }, {
            "name" : "yarn_nodemanager_log_dirs",
            "value" : "/yarn/container-logs"
          }, {
            "name" : "yarn_nodemanager_resource_cpu_vcores",
            "value" : "4"
          }, {
            "name" : "yarn_nodemanager_resource_memory_mb",
            "value" : "4247"
          } ]
        }, {
          "roleType" : "RESOURCEMANAGER",
          "items" : [ {
            "name" : "resource_manager_java_heapsize",
            "value" : "1059061760"
          }, {
            "name" : "yarn_scheduler_maximum_allocation_mb",
            "value" : "5578"
          }, {
            "name" : "yarn_scheduler_maximum_allocation_vcores",
            "value" : "4"
          } ]
        } ],
        "items" : [ {
          "name" : "hdfs_service",
          "value" : "hdfs"
        }, {
          "name" : "rm_dirty",
          "value" : "true"
        }, {
          "name" : "zk_authorization_secret_key",
          "value" : "jO6YtBdt0d8VTMZyvtg32qHo0nvmbR"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "yarn-JOBHISTORY-b424d1848b728a80118ace82135b2a2f",
        "type" : "JOBHISTORY",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "c423cs5k24xnvlg96gvvp432a"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-4c295c24bb561564fe89fde870e525d6",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "71d2k0m33n5hel2deo230asqp"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-7c486a97fd3992d66490e6d8d6a5ce09",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "ewfipbjca2bg1yogyb6tha043"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-8d800fdbd92a4e8cd7115087e2763453",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "a2bbaceb-4dee-4022-a507-3830954716f5"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "580xzx1o605pw9qbwctz5a0tg"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-f6b97aa6f19a22b0a57f6c1bc2ecf451",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "beb7ba14-216f-40c7-bb7a-76bf93cd1685"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "asbx1fe9iua4rb2jnhfblao75"
          } ]
        }
      }, {
        "name" : "yarn-RESOURCEMANAGER-b424d1848b728a80118ace82135b2a2f",
        "type" : "RESOURCEMANAGER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "rm_id",
            "value" : "81"
          }, {
            "name" : "role_jceks_password",
            "value" : "c9j5uuea1uuoj8o6mjp4qh6s7"
          } ]
        }
      } ],
      "displayName" : "YARN (MR2 Included)"
    }, {
      "name" : "hdfs",
      "type" : "HDFS",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "BALANCER",
          "items" : [ {
            "name" : "balancer_java_heapsize",
            "value" : "1059061760"
          } ]
        }, {
          "roleType" : "DATANODE",
          "items" : [ {
            "name" : "dfs_data_dir_list",
            "value" : "/dfs/dn"
          }, {
            "name" : "dfs_datanode_data_dir_perm",
            "value" : "700"
          }, {
            "name" : "dfs_datanode_du_reserved",
            "value" : "5367448780"
          }, {
            "name" : "dfs_datanode_http_port",
            "value" : "1006"
          }, {
            "name" : "dfs_datanode_port",
            "value" : "1004"
          } ]
        }, {
          "roleType" : "GATEWAY",
          "items" : [ {
            "name" : "dfs_client_use_trash",
            "value" : "true"
          } ]
        }, {
          "roleType" : "JOURNALNODE",
          "items" : [ {
            "name" : "dfs_journalnode_edits_dir",
            "value" : "/dfs/jn"
          } ]
        }, {
          "roleType" : "NAMENODE",
          "items" : [ {
            "name" : "dfs_name_dir_list",
            "value" : "/dfs/nn"
          }, {
            "name" : "dfs_namenode_servicerpc_address",
            "value" : "8022"
          }, {
            "name" : "namenode_java_heapsize",
            "value" : "1059061760"
          } ]
        }, {
          "roleType" : "SECONDARYNAMENODE",
          "items" : [ {
            "name" : "fs_checkpoint_dir_list",
            "value" : "/dfs/snn"
          }, {
            "name" : "secondary_namenode_java_heapsize",
            "value" : "1059061760"
          } ]
        } ],
        "items" : [ {
          "name" : "dfs_encrypt_data_transfer_algorithm",
          "value" : "AES/CTR/NoPadding"
        }, {
          "name" : "dfs_ha_fencing_cloudera_manager_secret_key",
          "value" : "aL0dFzGeedAx1sKBdpS89NzaF61vzE"
        }, {
          "name" : "fc_authorization_secret_key",
          "value" : "H3k5rwdYpKEwx48fvhn9P8urexi3NI"
        }, {
          "name" : "hadoop_security_authentication",
          "value" : "kerberos"
        }, {
          "name" : "hadoop_security_authorization",
          "value" : "true"
        }, {
          "name" : "http_auth_signature_secret",
          "value" : "17L1I23x9MIRlo9E7UFrTbTnZuB8jS"
        }, {
          "name" : "rm_dirty",
          "value" : "true"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "hdfs-BALANCER-b424d1848b728a80118ace82135b2a2f",
        "type" : "BALANCER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hdfs-DATANODE-4c295c24bb561564fe89fde870e525d6",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "pmgke8s1f3k6jre3amgot8yv"
          } ]
        }
      }, {
        "name" : "hdfs-DATANODE-7c486a97fd3992d66490e6d8d6a5ce09",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "eum9kywupoasi05d9uzudgony"
          } ]
        }
      }, {
        "name" : "hdfs-DATANODE-8d800fdbd92a4e8cd7115087e2763453",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "a2bbaceb-4dee-4022-a507-3830954716f5"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "ce09aoamjm87v4dcezbpoyrf6"
          } ]
        }
      }, {
        "name" : "hdfs-DATANODE-f6b97aa6f19a22b0a57f6c1bc2ecf451",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "beb7ba14-216f-40c7-bb7a-76bf93cd1685"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "1doom0xsi7afuo7wrw547k5y7"
          } ]
        }
      }, {
        "name" : "hdfs-FAILOVERCONTROLLER-4c295c24bb561564fe89fde870e525d6",
        "type" : "FAILOVERCONTROLLER",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "88zwskrbk1rwc3xp1oaurunky"
          } ]
        }
      }, {
        "name" : "hdfs-FAILOVERCONTROLLER-b424d1848b728a80118ace82135b2a2f",
        "type" : "FAILOVERCONTROLLER",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "e079ucd8svwyl8lbau2qd6hax"
          } ]
        }
      }, {
        "name" : "hdfs-JOURNALNODE-7c486a97fd3992d66490e6d8d6a5ce09",
        "type" : "JOURNALNODE",
        "hostRef" : {
          "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "4f4e7j9sev3u92ii0reegdxtk"
          } ]
        }
      }, {
        "name" : "hdfs-JOURNALNODE-8d800fdbd92a4e8cd7115087e2763453",
        "type" : "JOURNALNODE",
        "hostRef" : {
          "hostId" : "a2bbaceb-4dee-4022-a507-3830954716f5"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "bwz4gzh133bvvl83gnx49ycll"
          } ]
        }
      }, {
        "name" : "hdfs-JOURNALNODE-f6b97aa6f19a22b0a57f6c1bc2ecf451",
        "type" : "JOURNALNODE",
        "hostRef" : {
          "hostId" : "beb7ba14-216f-40c7-bb7a-76bf93cd1685"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "cnnpl594ll4jrrec5fvz6hqi0"
          } ]
        }
      }, {
        "name" : "hdfs-NAMENODE-4c295c24bb561564fe89fde870e525d6",
        "type" : "NAMENODE",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ {
            "name" : "autofailover_enabled",
            "value" : "true"
          }, {
            "name" : "dfs_federation_namenode_nameservice",
            "value" : "nameservice1"
          }, {
            "name" : "dfs_namenode_quorum_journal_name",
            "value" : "nameservice1"
          }, {
            "name" : "namenode_id",
            "value" : "89"
          }, {
            "name" : "role_jceks_password",
            "value" : "2ly947edn3x3asok1ixr14y3j"
          } ]
        }
      }, {
        "name" : "hdfs-NAMENODE-b424d1848b728a80118ace82135b2a2f",
        "type" : "NAMENODE",
        "hostRef" : {
          "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548"
        },
        "config" : {
          "items" : [ {
            "name" : "autofailover_enabled",
            "value" : "true"
          }, {
            "name" : "dfs_federation_namenode_nameservice",
            "value" : "nameservice1"
          }, {
            "name" : "dfs_namenode_quorum_journal_name",
            "value" : "nameservice1"
          }, {
            "name" : "namenode_id",
            "value" : "83"
          }, {
            "name" : "role_jceks_password",
            "value" : "dkx3zn5c58tmk3jyd4y2qp23s"
          } ]
        }
      } ],
      "displayName" : "HDFS"
    }, {
      "name" : "sentry",
      "type" : "SENTRY",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "SENTRY_SERVER",
          "items" : [ {
            "name" : "sentry_server_java_heapsize",
            "value" : "268435456"
          } ]
        } ],
        "items" : [ {
          "name" : "hdfs_service",
          "value" : "hdfs"
        }, {
          "name" : "sentry_server_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal"
        }, {
          "name" : "sentry_server_database_password",
          "value" : "sebc"
        }, {
          "name" : "sentry_service_admin_group",
          "value" : "hive,hdfs,admin,impala,hue,solr,kafka,hbase"
        }, {
          "name" : "sentry_service_allow_connect",
          "value" : "hive,hdfs,impala,hue,hdfs,solr,kafka,hbase,admin"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "sentry-GATEWAY-4c295c24bb561564fe89fde870e525d6",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "sentry-SENTRY_SERVER-7c486a97fd3992d66490e6d8d6a5ce09",
        "type" : "SENTRY_SERVER",
        "hostRef" : {
          "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "dt5y6pchs5u5msjcktqil5nht"
          } ]
        }
      } ],
      "displayName" : "Sentry"
    } ]
  } ],
  "hosts" : [ {
    "hostId" : "b2f98ba6-2aa9-40b3-9bd0-a377775335e7",
    "ipAddress" : "172.32.1.156",
    "hostname" : "ip-172-32-1-156.eu-west-1.compute.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "65f27ce7-ed87-4dcd-815b-8ba6f7987548",
    "ipAddress" : "172.32.1.185",
    "hostname" : "ip-172-32-1-185.eu-west-1.compute.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "a2bbaceb-4dee-4022-a507-3830954716f5",
    "ipAddress" : "172.32.1.230",
    "hostname" : "ip-172-32-1-230.eu-west-1.compute.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "beb7ba14-216f-40c7-bb7a-76bf93cd1685",
    "ipAddress" : "172.32.1.235",
    "hostname" : "ip-172-32-1-235.eu-west-1.compute.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb",
    "ipAddress" : "172.32.1.71",
    "hostname" : "ip-172-32-1-71.eu-west-1.compute.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  } ],
  "users" : [ {
    "name" : "__cloudera_internal_user__c0cf1b49-52ee-4137-a5be-41324cbf946b",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "67e6ef07cb810d4dfba796589b864e92ad2309f0a2e3d2cafa0cb0d6d62613d4",
    "pwSalt" : 1121087499110047489,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__hue-HUE_SERVER-b424d1848b728a80118ace82135b2a2f",
    "roles" : [ "ROLE_NAVIGATOR_ADMIN" ],
    "pwHash" : "d47d11c4cfc13e6d97b969856baea6ee61d9055e0a5ca7293527df7384da542d",
    "pwSalt" : 7170275721420826837,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-ACTIVITYMONITOR-7c486a97fd3992d66490e6d8d6a5ce09",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "ada4a194cfd2f98e1925b4a4409f69dd96d3cdb3e53a596b66aacea093d201c7",
    "pwSalt" : 7471365962415594725,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-EVENTSERVER-7c486a97fd3992d66490e6d8d6a5ce09",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "9a34172ff19e1fc4d4647bac83baa961744a875c41191a425d3bd4bc1d0ce19b",
    "pwSalt" : -8737949364718783639,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-HOSTMONITOR-7c486a97fd3992d66490e6d8d6a5ce09",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "0e7238083636e6dc52248637af73760836909ec41a0ba63f64b8ec8b52e52567",
    "pwSalt" : 1460758791003975399,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-REPORTSMANAGER-7c486a97fd3992d66490e6d8d6a5ce09",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "291e9cb24d7755e55991b92ec179a6113f5c0113d313040ad29e558af5d4381a",
    "pwSalt" : -4453930881480957248,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-SERVICEMONITOR-7c486a97fd3992d66490e6d8d6a5ce09",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "e74e61970bebf0b886460ac3214cb71e5ecff88ab2946fe0fe7e94a4eeffa727",
    "pwSalt" : -5701972103187575105,
    "pwLogin" : true
  }, {
    "name" : "admin",
    "roles" : [ "ROLE_LIMITED" ],
    "pwHash" : "6a98d4e36f5681e53df847d0872fcbd8e46089eb8c24d98995388f3bd20ea52b",
    "pwSalt" : 2200424225760269913,
    "pwLogin" : true
  }, {
    "name" : "minotaur",
    "roles" : [ "ROLE_CONFIGURATOR" ],
    "pwHash" : "df6d6e12a58566e4148e70d0200ceb82321ece4faadf388ce7407344a539e761",
    "pwSalt" : 8323689065367620797,
    "pwLogin" : true
  }, {
    "name" : "snawalgaria",
    "roles" : [ "ROLE_ADMIN" ],
    "pwHash" : "37d16ff1d7edf1df06ba6801617bac8475781aa5b31532adbeab3f749d845a20",
    "pwSalt" : 5464411073982915704,
    "pwLogin" : true
  } ],
  "versionInfo" : {
    "version" : "5.15.2",
    "buildUser" : "jenkins",
    "buildTimestamp" : "20181111-0722",
    "gitHash" : "bb8bf45c81fd454610b53e4945ceb482361f7568",
    "snapshot" : false
  },
  "managementService" : {
    "name" : "mgmt",
    "type" : "MGMT",
    "config" : {
      "roleTypeConfigs" : [ {
        "roleType" : "ACTIVITYMONITOR",
        "items" : [ {
          "name" : "firehose_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal"
        }, {
          "name" : "firehose_database_name",
          "value" : "amon"
        }, {
          "name" : "firehose_database_password",
          "value" : "sebc"
        }, {
          "name" : "firehose_database_user",
          "value" : "amon"
        } ]
      }, {
        "roleType" : "HOSTMONITOR",
        "items" : [ {
          "name" : "firehose_non_java_memory_bytes",
          "value" : "1610612736"
        } ]
      }, {
        "roleType" : "REPORTSMANAGER",
        "items" : [ {
          "name" : "headlamp_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal"
        }, {
          "name" : "headlamp_database_name",
          "value" : "rman"
        }, {
          "name" : "headlamp_database_password",
          "value" : "sebc"
        }, {
          "name" : "headlamp_database_user",
          "value" : "rman"
        } ]
      }, {
        "roleType" : "SERVICEMONITOR",
        "items" : [ {
          "name" : "firehose_non_java_memory_bytes",
          "value" : "1610612736"
        } ]
      } ],
      "items" : [ ]
    },
    "roles" : [ {
      "name" : "mgmt-ACTIVITYMONITOR-7c486a97fd3992d66490e6d8d6a5ce09",
      "type" : "ACTIVITYMONITOR",
      "hostRef" : {
        "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "4gfoxodwvjxygkrtx7fptkigx"
        } ]
      }
    }, {
      "name" : "mgmt-ALERTPUBLISHER-7c486a97fd3992d66490e6d8d6a5ce09",
      "type" : "ALERTPUBLISHER",
      "hostRef" : {
        "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "204rquxcqnlubayv13tybayyr"
        } ]
      }
    }, {
      "name" : "mgmt-EVENTSERVER-7c486a97fd3992d66490e6d8d6a5ce09",
      "type" : "EVENTSERVER",
      "hostRef" : {
        "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "5w1caxiy7pep1i18on0ifhvae"
        } ]
      }
    }, {
      "name" : "mgmt-HOSTMONITOR-7c486a97fd3992d66490e6d8d6a5ce09",
      "type" : "HOSTMONITOR",
      "hostRef" : {
        "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "erbuah6whmpr3dmssf196juz7"
        } ]
      }
    }, {
      "name" : "mgmt-REPORTSMANAGER-7c486a97fd3992d66490e6d8d6a5ce09",
      "type" : "REPORTSMANAGER",
      "hostRef" : {
        "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "710bwjpzh6p5w37kno5uk272l"
        } ]
      }
    }, {
      "name" : "mgmt-SERVICEMONITOR-7c486a97fd3992d66490e6d8d6a5ce09",
      "type" : "SERVICEMONITOR",
      "hostRef" : {
        "hostId" : "47a8a62a-4d5a-4e98-a8f7-c6b5eb8d2dbb"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "8pykx4ojg8vxsnguj3b74hlkm"
        } ]
      }
    } ],
    "displayName" : "Cloudera Management Service"
  },
  "managerSettings" : {
    "items" : [ {
      "name" : "AD_USE_SIMPLE_AUTH",
      "value" : "false"
    }, {
      "name" : "CLUSTER_STATS_START",
      "value" : "10/28/2012 0:10"
    }, {
      "name" : "KDC_ADMIN_HOST",
      "value" : "172.32.1.71"
    }, {
      "name" : "KDC_ADMIN_PASSWORD",
      "value" : "BQIAAABOAAEAC1NBVVJBQkguQ09NAAxjbG91ZGVyYS1zY20AAAABXGUwcAEAEgAg7NvbVBZHvkMpNfoc+3NVzzRxrW2xVvj1Itta7N1erTQAAAAB"
    }, {
      "name" : "KDC_ADMIN_USER",
      "value" : "cloudera-scm@SAURABH.COM"
    }, {
      "name" : "KDC_HOST",
      "value" : "172.32.1.71"
    }, {
      "name" : "KRB_DOMAIN",
      "value" : "SAURABH.COM"
    }, {
      "name" : "KRB_ENC_TYPES",
      "value" : "aes256-cts-hmac-sha1-96"
    }, {
      "name" : "KRB_MANAGE_KRB5_CONF",
      "value" : "true"
    }, {
      "name" : "MAX_RENEW_LIFE",
      "value" : "604800"
    }, {
      "name" : "PUBLIC_CLOUD_STATUS",
      "value" : "ON_PUBLIC_CLOUD"
    }, {
      "name" : "REMOTE_PARCEL_REPO_URLS",
      "value" : "https://archive.cloudera.com/cdh5/parcels/{latest_supported}/,https://archive.cloudera.com/cdh4/parcels/latest/,https://archive.cloudera.com/impala/parcels/latest/,https://archive.cloudera.com/search/parcels/latest/,https://archive.cloudera.com/accumulo/parcels/1.4/,https://archive.cloudera.com/accumulo-c5/parcels/latest/,https://archive.cloudera.com/kafka/parcels/latest/,http://archive.cloudera.com/kudu/parcels/latest/,https://archive.cloudera.com/spark/parcels/latest/,https://archive.cloudera.com/sqoop-connectors/parcels/latest/"
    }, {
      "name" : "SECURITY_REALM",
      "value" : "SAURABH.COM"
    } ]
  }
}

