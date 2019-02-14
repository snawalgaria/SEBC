saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.154.63.86:7180/api/version
> '
curl: (3) Illegal characters found in URL
saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.154.63.86:7180/api/version'
v19saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '554.63.86:7180/api/v19/cm/version'
{
  "version" : "5.16.1",
  "buildUser" : "jenkins",
  "buildTimestamp" : "20181120-1809",
  "gitHash" : "6a13b87a6fcdf4afad6d4474a68a9434b24d6c67",
  "snapshot" : false
}saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.54.63.86:7180/api/v19/users'
{
  "items" : [ {
    "name" : "admin",
    "roles" : [ "ROLE_LIMITED" ]
  }, {
    "name" : "minotaur",
    "roles" : [ "ROLE_CONFIGURATOR" ]
  }, {
    "name" : "snawalgaria",
    "roles" : [ "ROLE_ADMIN" ]
  } ]
}saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.54.63.86:7180/api/v19/cm/deployment' | grep -A 2 database_host
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0          "name" : "hive_metastore_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
          "name" : "database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
            "name" : "oozie_database_host",
            "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
            "sensitive" : false
--
          "name" : "sentry_server_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
          "name" : "firehose_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
100 53822    0--
 538          "name" : "headlamp_database_host",
22          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
           "sensitive" : false
   0     0   242k      0 --:--:-- --:--:-- --:--:--  242k
saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.154.63.86:7180/api/v19/cm/deployment' | grep -A 2 scm
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 53822    0 53822    0     0   383k      "value" : "cloudera-scm@SAURABH.COM",
        "sensitive" : false
     }, {
saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.154.63.86:7180/api/v19/cm/deployment' | grep -A 2 scm
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 53822    0 53822    0     0   357k      0 --      "value" : "cloudera-scm@SAURABH.COM",
:--      "sensitive" : false
:    }, {
-- --:--:-- --:--:--  357k
saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.154.63.86:7180/api/v19/cm/deployment' | grep -A 2 database_host
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0          "name" : "hive_metastore_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
          "name" : "database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
            "name" : "oozie_database_host",
            "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
            "sensitive" : false
--
          "name" : "sentry_server_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
          "name" : "firehose_database_host",
          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
          "sensitive" : false
--
          "name" : "headlamp_database_host",
10          "value" : "ip-172-32-1-71.eu-west-1.compute.internal",
0          "sensitive" : false
 53822    0 53822    0     0   398k      0 --:--:-- --:--:-- --:--:--  398k
saurabh@saurabh-XPS-15-9550:~/SEBC/resources$ curl -u snawalgaria:cloudera '54.154.63.86:7180/api/v19/cm/scmDbInfo'
{
  "scmDbType" : "MYSQL",
  "embeddedDbUsed" : false

